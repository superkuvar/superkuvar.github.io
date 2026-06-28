#!/usr/bin/env python3
"""Generate hero image sets per slike.txt from existing originals."""

from __future__ import annotations

import re
import shutil
import subprocess
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPLOADS = ROOT / "wp-content" / "uploads"

# GA4 top #3–#20 (skip #1 pita, #2 rogač done; skip #19 projice done)
RECIPES = [
    ("_posts/2012-09-04-boranija-u-zamrzivacu.md", "boranija.u.zamrzivacu"),
    ("_posts/2011-08-06-sladoled-od-pavlake-i-voca.md", "sladoled.od.pavlake.i.voca"),
    ("_posts/2012-06-29-cuspajz-od-tikvica.md", "cuspajz.od.tikvica"),
    ("_posts/2013-03-25-corbast-pasulj-sa-slaninom.md", "corbast.pasulj.sa.slaninom"),
    ("_posts/2011-05-11-pire-od-blitve.md", "pire.od.blitve"),
    ("_posts/2011-03-25-corba-od-graska-i-krompira.md", "corba.od.graska.i.krompira"),
    ("_posts/2011-06-17-dinstano-meso-sa-povrcem.md", "dinstano.meso.sa.povrcem"),
    ("_posts/2011-12-26-jednostavni-kolac-sa-pudingom-i-visnjama.md", "jednostavni.kolac.sa.pudingom.i.visnjama"),
    ("_posts/2011-06-23-sataras-sa-pirincem.md", "sataras.sa.pirincem"),
    ("_posts/2011-07-19-kolac-sa-makom.md", "kolac.sa.makom"),
    ("_posts/2011-12-22-oblande-sa-mlekom-i-orasima.md", "oblande.sa.mlekom.i.orasima"),
    ("_posts/2015-04-10-salata-od-rotkvica.md", "salata.od.rotkvica"),
    ("_posts/2012-06-27-boranija-sa-krompirom.md", "boranija.sa.krompirom"),
    ("_posts/2013-04-05-kolac-sa-jogurtom-i-orasima.md", "kolac.sa.jogurtom.i.orasima"),
    ("_posts/2012-06-11-mafini-sa-bananama.md", "mafini.sa.bananama"),
    ("_posts/2013-01-14-varivo-od-graska-i-sargarepe.md", "varivo.od.graska.i.sargarepe"),
    ("_posts/2015-10-12-varivo-od-patlidzana-tikvica-paprika-paradajza.md", "varivo.od.patlidzana.tikvica.paprika.paradajza"),
]

SKIP_PARTS = (".korak", ".hero", ".og.", ".kartica", ".master", ".hero.800")
SIZE_SUFFIX = re.compile(r"-\d+x\d+$")
WP_HASH = re.compile(r"-e\d+$")


def ascii_fold(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def image_size(path: Path) -> tuple[int, int]:
    out = subprocess.check_output(
        ["identify", "-format", "%w %h", str(path)], text=True
    ).strip()
    w, h = out.split()
    return int(w), int(h)


def base_stem(path: Path) -> str:
    stem = path.stem
    stem = SIZE_SUFFIX.sub("", stem)
    stem = WP_HASH.sub("", stem)
    return stem


def find_source(current: Path) -> Path | None:
    if not current.exists():
        return None

    target = ascii_fold(base_stem(current))

    def pick(min_height: int) -> Path | None:
        best: Path | None = None
        best_score = 0
        for candidate in current.parent.iterdir():
            if candidate.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
                continue
            name = candidate.name.lower()
            if any(part in name for part in SKIP_PARTS):
                continue
            w, h = image_size(candidate)
            if h < min_height or w / max(h, 1) > 4.5:
                continue
            cand_base = ascii_fold(base_stem(candidate))
            if cand_base != target and candidate != current:
                continue
            score = w * h
            if score > best_score:
                best_score = score
                best = candidate
        return best

    return pick(250) or pick(120)


def run_convert(args: list[str]) -> None:
    subprocess.run(["convert", *args], check=True)


def generate_set(source: Path, slug: str, out_dir: Path) -> dict[str, str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    hero = out_dir / f"{slug}.hero.jpg"
    hero800 = out_dir / f"{slug}.hero.800.jpg"
    og = out_dir / f"{slug}.og.jpg"
    kartica = out_dir / f"{slug}.kartica.jpg"
    master = out_dir / f"{slug}.master.jpg"

    run_convert(
        [
            str(source),
            "-resize",
            "1200x675^",
            "-gravity",
            "center",
            "-extent",
            "1200x675",
            "-quality",
            "82",
            "-strip",
            str(hero),
        ]
    )
    run_convert([str(hero), "-resize", "800x450", "-quality", "82", "-strip", str(hero800)])
    run_convert([str(hero), "-crop", "1200x630+0+35", "+repage", "-quality", "82", "-strip", str(og)])
    run_convert(
        [
            str(hero),
            "-resize",
            "800x600^",
            "-gravity",
            "center",
            "-extent",
            "800x600",
            "-quality",
            "82",
            "-strip",
            str(kartica),
        ]
    )
    if not master.exists():
        shutil.copy2(source, master)

    rel = lambda p: "/wp-content/uploads/" + str(p.relative_to(UPLOADS)).replace("\\", "/")
    return {
        "image": rel(hero),
        "og_image": rel(og),
        "card_image": rel(kartica),
    }


def resize_korak(path: Path) -> None:
    if not path.exists():
        return
    w, h = image_size(path)
    if w == 900 and h == 675:
        return
    tmp = path.with_suffix(".tmp.jpg")
    run_convert(
        [
            str(path),
            "-resize",
            "900x675^",
            "-gravity",
            "center",
            "-extent",
            "900x675",
            "-quality",
            "82",
            "-strip",
            str(tmp),
        ]
    )
    tmp.replace(path)


def update_front_matter(post_path: Path, fields: dict[str, str]) -> None:
    text = post_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError(f"No front matter: {post_path}")

    parts = text.split("---", 2)
    fm = parts[1]

    for key, value in fields.items():
        line = f"{key}: {value}"
        pattern = re.compile(rf"^{re.escape(key)}:.*$", re.MULTILINE)
        if pattern.search(fm):
            fm = pattern.sub(line, fm)
        else:
            fm = fm.rstrip() + "\n" + line + "\n"

    post_path.write_text("---" + fm + "---" + parts[2], encoding="utf-8")


def process_koraks(slug: str) -> list[str]:
    resized: list[str] = []
    for korak in UPLOADS.rglob(f"{slug}.korak*.jpg"):
        resize_korak(korak)
        resized.append(str(korak.relative_to(ROOT)))
    return resized


def read_image_field(post_path: Path) -> str | None:
    text = post_path.read_text(encoding="utf-8")
    m = re.search(r"^image:\s*(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else None


def main() -> None:
    for post_rel, slug in RECIPES:
        post_path = ROOT / post_rel
        image_field = read_image_field(post_path)
        if not image_field:
            print(f"SKIP {slug}: no image field")
            continue
        if f"{slug}.hero.jpg" in image_field:
            print(f"SKIP {slug}: already has hero")
            process_koraks(slug)
            continue

        current = ROOT / image_field.lstrip("/")
        source = find_source(current)
        if not source:
            print(f"FAIL {slug}: no source for {image_field}")
            continue

        out_dir = source.parent
        fields = generate_set(source, slug, out_dir)
        update_front_matter(post_path, fields)
        koraks = process_koraks(slug)
        print(f"OK {slug} <- {source.name}")
        if koraks:
            print(f"   koraks: {', '.join(koraks)}")


if __name__ == "__main__":
    main()