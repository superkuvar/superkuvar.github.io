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

# GA4 top #21–#50 (skip #39 /silicijum/ — nije recept)
RECIPES = [
    ("_posts/2011-08-12-bakini-medenjaci.md", "bakini.medenjaci"),
    ("_posts/2011-03-22-corba-od-blitve-3.md", "corba.od.blitve.3"),
    ("_posts/2011-06-29-przenija.md", "przenija"),
    ("_posts/2012-06-20-dinstana-keleraba.md", "dinstana.keleraba"),
    ("_posts/2011-12-26-socni-kolac-sa-makom.md", "socni.kolac.sa.makom"),
    ("_posts/2012-02-06-jastuk-torta.md", "jastuk.torta"),
    ("_posts/2012-01-06-kolac-sa-visnjama-i-orasima.md", "kolac.sa.visnjama.i.orasima"),
    ("_posts/2011-04-01-varivo-od-tikvica.md", "varivo.od.tikvica"),
    ("_posts/2013-08-23-zapecena-boranija-sa-krompirom.md", "zapecena.boranija.sa.krompirom"),
    ("_posts/2012-12-21-dinstani-grasak.md", "dinstani.grasak"),
    ("_posts/2011-07-19-kolacici-s-belim-vinom.md", "kolacici.s.belim.vinom"),
    ("_posts/2012-05-19-kuvani-mladi-kupus.md", "kuvani.mladi.kupus"),
    ("_posts/2013-01-21-posna-sarma-sa-orasima.md", "posna.sarma.sa.orasima"),
    ("_posts/2015-04-06-salata-od-rotkvica-sa-pavlakom.md", "salata.od.rotkvica.sa.pavlakom"),
    ("_posts/2011-07-15-brzi-kolac-sa-orasima.md", "brzi.kolac.sa.orasima"),
    ("_posts/2013-06-04-kolac-sa-ribizlama.md", "kolac.sa.ribizlama"),
    ("_posts/2015-08-18-posna-sarma-od-blitve.md", "posna.sarma.od.blitve"),
    ("_posts/2020-01-03-projara-sa-pecurkama-i-sirom.md", "projara.sa.pecurkama.i.sirom"),
    ("_posts/2012-07-21-slatka-pita-sa-tikvicama.md", "slatka.pita.sa.tikvicama"),
    ("_posts/2011-06-18-sos-od-sampinjona.md", "sos.od.sampinjona"),
    ("_posts/2011-06-21-dinstana-boranija-sa-sargarepom.md", "dinstana.boranija.sa.sargarepom"),
    ("_posts/2015-08-10-pohovane-tikvice-u-pivskom-testu.md", "pohovane.tikvice.u.pivskom.testu"),
    ("_posts/2012-02-21-rezanci-sa-sirom.md", "rezanci.sa.sirom"),
    ("_posts/2012-07-31-dinstani-plavi-patlidzan.md", "dinstani.plavi.patlidzan"),
    ("_posts/2012-12-13-dinstano-meso-sa-paprikom.md", "dinstano.meso.sa.paprikom"),
    ("_posts/2013-02-23-pilav-sa-pilecim-belim-mesom.md", "pilav.sa.pilecim.belim.mesom"),
    ("_posts/2011-12-13-rolat-od-oblande-sa-keksom-i-kokosom.md", "rolat.od.oblande.sa.keksom.i.kokosom"),
    ("_posts/2011-07-13-slane-galete.md", "slane.galete"),
    ("_posts/2011-06-16-boranija-sa-piletinom.md", "boranija.sa.piletinom"),
]

IMAGE_OVERRIDES: dict[str, str] = {
    "socni.kolac.sa.makom": "/wp-content/uploads/2011/12/kolacmak.jpg",
    "sos.od.sampinjona": "/wp-content/uploads/2015/06/dinstanisampinjoniikrompir.jpg",
    "dinstana.boranija.sa.sargarepom": (
        "/wp-content/uploads/2011/06/Zapečena-boranija-sa-sojom-1024x768.jpg"
    ),
}

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
        image_field = read_image_field(post_path) or IMAGE_OVERRIDES.get(slug)
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