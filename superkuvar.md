# SUPERKUVAR.COM

## Kompletno uputstvo — transformacija jednog recepta

**Verzija:** 2.1 · **Datum:** jul 2026 · **Sajt:** <https://superkuvar.com>

**Repo (logički):** `superkuvar/superkuvar.github.io`, grana `master`
**Repo (lokalno, na vlasnikovoj mašini):** `/home/dj/repos/superkuvar.github.io`
Ako asistent radi u drugom okruženju (cloud agent, sandbox), „root repoa" znači
koren klona ovog repoa — sve putanje u dokumentu su relativne u odnosu na njega.

**Ovaj dokument zamenjuje** `renoviranje.txt` i `slike.txt` — ta dva fajla se
**ne koriste i ne citiraju**. Jedan dokument = sva pravila za recepte.
Za članke (layout `article`) važi `superkuvar.art.md`.

**Changelog:**
- v2.1 (jul 2026): hero set (AI) — zabrana ostataka hrane / mrvica / prosute
  hrane na stolu i oko posude; proširen hero prompt.
- v2.0 (jul 2026): korak slike izmeštene u Appendix A (neaktivno); razrešena
  batch kontradikcija; dodat kompletan YAML šablon i pun primer pre→posle;
  dodata pravila za procenu vremena/kalorija; dodata grana za slike < 400 px;
  uklonjene reference na slike.txt; dodata mašinska provera.
- v1.x (jun 2026): prvobitna verzija.

---

## STATUS PRAVILA (pročitaj prvo)

| Oblast | Status |
| ------ | ------ |
| A. Tekst (YAML + telo, Korak 1…N) | ✅ AKTIVNO |
| B. Hero set (hero, og, kartica, hero.800) | ✅ AKTIVNO |
| C. Korak slike (`slug.korakN.jpg` u telu) | ⛔ NEAKTIVNO — sva pravila u **Appendix A**; NE primenjuj ih |
| D. Commit (bez push) | ✅ AKTIVNO |

Glavni tok ovog dokumenta sadrži **samo aktivna pravila**. Sve o korak slikama
je u Appendix A i primenjuje se tek kada vlasnik u ovom dokumentu promeni
status C u AKTIVNO. Do tada: **ne umeći korak slike, ne generiši ih, ne
ostavljaj HTML komentare o njima u telu recepta.**

---

## 0. Git repo i commit (obavezno)

**Jedini repo za rad:** koren repoa `superkuvar/superkuvar.github.io`
(lokalno: `/home/dj/repos/superkuvar.github.io`).

**Zabranjeno:** rad u drugim klonovima, worktree folderima ili kopijama repoa
(npr. `.grok/worktrees/...`). Lokalni pregled uvek iz root foldera:

```bash
cd <root-repoa>
bundle exec jekyll serve --livereload
# → http://localhost:4000
```

**Commit pre izmene:** pre izmene bilo kog fajla (`_posts/...`, layout, CSS,
slike…) taj fajl mora biti commitovan. **Ako nije commitovan**, asistent ga
prvo commituje ovako, pa tek onda kreće sa izmenom:

```bash
git add <fajl>
git commit -m "backup: <fajl> pre renovacije"
```

**Commit posle izmene:** kada je izmena završena, odmah commituj sve izmenjene
fajlove. Asistent ne ostavlja necommitovane izmene.

**Push na live:** asistent **ne pushuje**. Vlasnik pregleda (`git status`,
`git diff`, localhost) i sam radi `git push origin master`.

**Ova uputstva** (`superkuvar.md`, `superkuvar.art.md`): commituj ih pre i
posle izmene pravila — isti princip kao za recepte. Pri svakoj izmeni pravila
ažuriraj **Changelog** i, ako treba, tabelu **STATUS PRAVILA**.

---

## 1. Šta napišeš asistentu

```
Potpuno renoviraj recept:
URL: https://superkuvar.com/...
```

To je dovoljno. Asistent radi sve ispod i **commituje**; vlasnik pushuje.

**Jedinica posla:** jedan recept = jedan posao = jedan commit. Recepti se
uvek rade **pojedinačno i sekvencijalno** — nikad dva recepta u jednom
commitu i nikad paralelno.

**Kada vlasnik zada listu recepata (batch):** asistent ih radi **redom, jedan
po jedan**, svaki kao zaseban posao sa zasebnim commitom, i **ne čeka „ok"**
između dva recepta. „Batch" znači redosled bez pauze — ne znači spajanje
poslova, preskakanje provera ni zajednički commit.

---

## 2. Šta znači „potpuno renoviran"

Jedan recept = **tekst + hero set + commit**. Tekst bez hero seta **nije gotov**.

| Deo | Rezultat |
| --- | -------- |
| **A. Tekst** | YAML + Korak 1, 2, 3… u telu |
| **B. Hero set** | hero + og + kartica + hero.800 |
| **D. Commit** | `git commit` (push radi vlasnik) |

*(C. Korak slike — ⛔ neaktivno, vidi Appendix A.)*

**Referenca u repou:** `_posts/2011-03-22-jagnjeca-corba.md` (uvek pogledaj
ako imaš pristup repou). **Kompletan primer formata** je i u sekciji 10 ovog
dokumenta — koristi ga ako repo nije pri ruci.

**Redosled:** A → B → D. Nikad obrnuto (hero pre teksta pravi duplikate i
pogrešne slike).

---

## 3. Transformacija — koraci

### Korak 1 — Pročitaj original

- Otvori `_posts/....md` i razumi šta se zaista kuva.
- Ne izmišljaj sastojke. Ne kopiraj fraze iz drugog recepta.
- Proveri postojeće slike: YAML `image:`, `<img>` u članku, fajlovi u
  `wp-content/uploads/GODINA/MESEC/`.

### Korak 2 — Tekst (YAML + telo)

**Originalni tekst — ne menjati.** Sastojci i način pripreme moraju **ostati
kao u originalu** — iste reči, isti redosled, iste formulacije (uključujući
stare pravopisne ili gramatičke greške). **Ne prepisuj, ne lektoriši i ne
„poboljšavaj"** tekst recepta.

**Šta smeš da dodaš (SEO i čitljivost):**

| Dodatak | Gde | Primer |
| ------- | --- | ------ |
| **Uvod** | YAML `description` | vidi Korak 2a |
| **Napomene** | završni pasus | serviranje, varijante, saveti iz originalne napomene |
| **Objašnjenja termina** | kraj članka | dinstanje, zaprška, legir — samo ako postoje u originalu |

SEO se postiže **dodacima**, ne izmenom starog teksta recepta.

**KOMPLETAN YAML ŠABLON** (kopiraj i popuni; postojeća polja `title`,
`permalink`, `date`, `categories`, `tags`, `guid`, `id`, `author` iz starog
fajla **prepiši netaknuta**):

```yaml
---
id: 123
title: NASLOV RECEPTA          # iz originala, ne menjaj
date: 2011-03-22               # iz originala, ne menjaj
author: ime                    # iz originala, ne menjaj
layout: post
permalink: /url-recepta/       # iz originala, ne menjaj
published: true
description: >-
  Uvod od 1–2 rečenice po Koraku 2a. Šta je jelo + kada dobro dođe.
prep_time: PT20M               # ISO 8601; procena — vidi Korak 2b
cook_time: PT40M
total_time: PT1H               # prep + cook
servings: 4 porcije
nutrition: oko 280 kalorija po porciji   # slobodan tekst, tačno ovaj oblik
ingredients:                   # lista stringova, DOSLOVNO iz originala,
  - 500 g krompira             # jedan sastojak = jedan string,
  - 2 kašike rena              # količina i sastojak zajedno u istom stringu
  - so
instructions:                  # jedan korak = jedan string; IDENTIČAN tekst
  - Krompir oljuštiti i skuvati u slanoj vodi.     # kao Korak 1 u telu
  - Ren narendati i pomešati sa pavlakom.          # (bez "Korak N." prefiksa)
image: /wp-content/uploads/GODINA/slug.hero.jpg
og_image: /wp-content/uploads/GODINA/slug.og.jpg
card_image: /wp-content/uploads/GODINA/slug.kartica.jpg
categories:                    # iz originala, ne menjaj
  - salate
tags:                          # iz originala, ne menjaj
  - krompir
---
```

**Sintaksa `ingredients` i `instructions`:** uvek YAML lista stringova
(crtica + razmak). Bez mapa, bez multiline `|` blokova, bez numeracije u
stringu. `instructions[i]` = tekst Koraka i+1 iz tela, **reč po reč**, bez
prefiksa „Korak N.".

**Stara pogrešna polja (obriši ako postoje, ne koristi):** `ingreedients`,
`recipeinstructions`, `recipeyield`, `preptime`, `cooktime`.

**TELO ČLANKA (ispod `---`) — tačan format:**

```markdown
**Način pripreme:**

<span id="step-1"></span>**Korak 1.** Tekst prvog koraka iz originala.

<span id="step-2"></span>**Korak 2.** Tekst drugog koraka iz originala.

Završni pasus / napomena (novi tekst, SEO — 1–2 rečenice).

**Objašnjenja kulinarskih termina:** (novi tekst, samo po potrebi)
```

**Precizna pravila za korake u telu:**

- Format je tačno: `<span id="step-N"></span>**Korak N.** ` — mala slova u
  `step-N`, numeracija od 1 bez preskakanja, tačka posle broja, jedan razmak
  posle zatvorenog bolda, sve u istom redu sa tekstom koraka.
- Tekst koraka = originalni tekst načina pripreme, samo isečen na logične
  celine — **bez preformulisanja**. Jedan korak = jedna zaokružena radnja ili
  originalni pasus; ne cepaj rečenicu na pola.
- **Uvodni pasus originala** (ako postoji pre postupka) ostaje kao pasus pre
  `**Način pripreme:**` — nije korak.
- **Originalna napomena o serviranju** (npr. „Salata se služi topla.") nije
  korak — ide u završni pasus, doslovno, a novi SEO tekst se dodaje posle nje.
- Ako se postupak ne da prirodno iseći (jedan kratak pasus), dozvoljen je i
  samo **Korak 1** — ne izmišljaj podelu na silu.

**Obriši iz tela:** zaglavlje „Potrebno je" (sastojci idu u YAML), staro
zaglavlje „Priprema", sve stare `<img>` tagove.

**Ne menjaj:** `title`, `permalink`, `date`, `categories`, `tags`, `guid`,
`id`, `author` — čak i ako `title` ima grešku ili je sav velikim slovima.

### Korak 2a — `description` (uvodni tekst, obavezno)

**Šta je:** 1–2 rečenice uvoda u YAML polju `description`. Pojavljuje se na
početku stranice, u Google pretrazi i pri deljenju.

**Mora da sadrži:**

1. **Šta je jelo** — vrsta jela i glavni sastojci (**samo iz originala**).
2. **Karakter** — npr. kremasto, toplo, lagano, zasitno (ako odgovara).
3. **Kada dobro dođe** — hladni dani, ručak, večera, porodični obrok, sezona.

**Ne sme:** prepisivati korake; izmišljati sastojke; prazan šablon tipa
„domaći recept iz kategorije supe i čorbe".

**Dužina:** 120–200 karaktera (1–2 rečenice).

**Formula:**

```
[Naziv jela] je [kakvo je jelo] od [glavni sastojci iz originala].
[Zašto / kada poslužiti — jedna kratka rečenica].
```

**Primer (Čorba od bundeve i šargarepe):**
> Čorba od bundeve i šargarepe je kremasto, toplo jelo od bundeve, šargarepe i
> praziluka sa pirinčem. Odlična je za hladnije dane, lagan ručak ili večeru,
> a uz kiselu pavlaku postaje još puniji obrok.

### Korak 2b — Procena vremena, porcija i kalorija (novo, obavezno)

Stari recepti najčešće **nemaju** vremena ni kalorije. Ova polja su **jedina**
gde je asistentu dozvoljena procena — po sledećim pravilima:

- `prep_time` / `cook_time`: proceni realno iz sastojaka i postupka; zaokruži
  na **5 minuta**; `total_time` = zbir. Format ISO 8601 (`PT20M`, `PT1H10M`).
- `servings`: ako original navodi broj porcija — prepiši; ako ne, proceni iz
  količina (npr. 500 g mesa ≈ 4 porcije). Format: `4 porcije`.
- `nutrition`: gruba procena iz sastojaka, zaokružena na **10 kcal**, uvek u
  obliku `oko NNN kalorija po porciji`. Ne navodi makronutrijente.
- Ako je procena nemoguća (nejasne količine), pitaj vlasnika — ne izmišljaj
  precizne brojeve.
- Procena važi **samo** za ova polja. Za sastojke i korake procena je i dalje
  strogo zabranjena.

### Korak 2c — Provera originala (obavezno pre slika)

Uporedi sa izvornim receptom:

- `ingredients` i svaki **Korak N** — ista reč po reč kao u izvoru
- `instructions[i]` = Korak i+1 (isti tekst, isti redosled)
- `description`, završni pasus i **Objašnjenja** — jedini novi tekst; tu piši
  gramatički ispravno
- nisi zamenio reči, ispravio pravopis ili dodao sastojke/korake

Ako si promenio originalni tekst recepta — vrati ga. Greške iz originala
**ostaju**.

### Korak 3 — Odluka o slikama (algoritam za hero set)

Prvo proveri šta postoji u `wp-content/uploads/GODINA/MESEC/` za taj recept.

```
Postoji fotografija ≥ 400 px (duža strana)?
  → DA: najbolja fotografija gotovog jela = izvor za hero set
        (resize/crop po tabeli u Koraku 4)
  → NE, postoji samo slika < 400 px:
        AI generiše hero set (sekcija 4 — promptovi);
        original sačuvaj kao slug.master.jpg (arhiva);
        NE upscale-uj sitni JPG
  → NE, nema nijedne slike:
        pitaj vlasnika; sa odobrenjem → AI generiše hero set

Više originalnih fotografija? → najbolja gotovog jela = hero.
Nisi siguran? → ne commituj slike; pitaj.
```

- **Ne upscale-uj** sitne JPG-ove (< 400 px duža strana).
- **Ne uzimaj** slike drugog recepta.
- Stare `<img>` iz tela su obrisane u Koraku 2; slike se vraćaju kao hero set.

### Korak 4 — Hero set

**Imena fajlova:** `{slug}.{tip}.jpg` — reči odvojene **tačkom**, mala slova,
**bez kvačica** (č→c, ć→c, š→s, ž→z, đ→dj).

| Fajl | Dimenzija | Gde se koristi |
| ---- | --------- | -------------- |
| `slug.hero.jpg` | 1200×675 | YAML `image:`, vrh stranice |
| `slug.hero.800.jpg` | 800×450 | mobilni (resize iz heroa) |
| `slug.og.jpg` | 1200×630 | YAML `og_image:`, Facebook |
| `slug.kartica.jpg` | 800×600 | YAML `card_image:`, grid |
| `slug.master.jpg` | original | arhiva kopije originala (opciono) |

**Redosled pravljenja:** 1. hero → 2. og → 3. kartica → 4. hero.800 →
(opciono) master.

**YAML posle slika:**

```yaml
image: /wp-content/uploads/GODINA/slug.hero.jpg
og_image: /wp-content/uploads/GODINA/slug.og.jpg
card_image: /wp-content/uploads/GODINA/slug.kartica.jpg
```

**Skripta za resize:** `scripts/process_recipe_images.py` — samo za hero set
iz postojećeg originala ≥ 400 px.

### Korak 5 — Commit (obavezno)

```bash
cd <root-repoa>
git add _posts/ime.md wp-content/uploads/GODINA/slug.*.jpg
git commit -m "Recept: NAZIV — potpuno renoviran"
```

**Ne radi `git push`** — vlasnik pregleda i sam pushuje.

**Commit samo kad je recept potpun** (A + B). Nepotpun → pitaj, ne commituj.

---

## 4. Kadriranje i AI promptovi

**Opšti stil** (u svaki AI prompt):
> Fotorealistična fotografija hrane. Prirodno dnevno svetlo sa leve strane,
> tople boje. Drvena podloga ili svetli stolnjak. Bez teksta, logoa, vodenog
> žiga. Za slatko: umerena slatkoća, domaća kuhinja.

**Zabrane na svim slikama:**

- **Bez escajga** — viljuške, noževi, kašike, štapići, posude za escajg
- **Bez plastičnih poslužavnica** — plastični tanjiri, tacne, posude, kutije
- **Bez metalnih poslužavnica** — metalne tacne, plitici, poslužni plehovi
  (osim pleha za pečenje kada prikazuje pečenje)
- **Dozvoljeno:** drvena daska, keramička zdela, staklena posuda, emajlirani
  pleh za pečenje, platneni stolnjak
- Ako AI ubaci escajg ili plastiku — **regeneriši** sa eksplicitnom zabranom
  u promptu

**Hero set (posebno — AI generisanje hero / og / kartica):**

- **Bez ostataka hrane na stolu** — nema mrvica, prosutih zrna, komadića jela,
  oraha, voća ili sosa oko posude; nema „rasute“ dekoracije hrane po daski
  ili stolnjaku
- Sto / daska / podloga moraju izgledati **čisto**; jelo je **samo u posudi**
  (tanjir, zdela, pleh) u centru kadra
- Ako AI ipak raspe hranu oko tanjira — **regeneriši** hero sa eksplicitnom
  zabranom u promptu: `clean table, no crumbs, no spilled food, no food
  scraps around the dish`
- OG i kartica nastaju iz heroa (crop/resize) pa nasleđuju isto pravilo

**Varijacija:** dozvoljena prirodna varijacija ugla, posude, kadra i
osvetljenja; sme se generisati više varijanti (drugi seed) i uzeti najbolja
koja poštuje zabrane.

| Tip | Kadar | Prompt skica |
| --- | ----- | ------------ |
| **Hero** | 45° odozgo, jelo u centru, 16:9, prostor oko tanjira, **čist sto** | `[GOTOVO JELO] on [POSUDA], 45 degree food photography, wide 16:9 aspect, warm daylight, clean table, no crumbs, no spilled food, no food scraps around the dish, no text, no cutlery, no plastic trays` |
| **OG** | isto jelo, šire, jelo niže u kadru (FB seče gore/dole) | `same dish, wider 1.91:1 aspect, subject lower in frame, safe zone, clean table` — ili crop heroa |
| **Kartica** | crop iz heroa, jelo popunjava kadar | crop hero na 800×600 |

**Napomena o dimenzijama:** generatori slika ignorišu piksele u promptu —
u prompt ide **aspect ratio** (16:9, 1.91:1), a tačne dimenzije (1200×675,
1200×630, 800×600, 800×450) se dobijaju naknadnim **resize/crop** korakom.

**JPEG:** kvalitet 80–85 %. Hero ~80–150 KB.

---

## 5. Pravila teksta — zabrane

| Pravilo | Detalj |
| ------- | ------ |
| **Legir** | Samo ako recept STVARNO ima legir (žumance + kisela pavlaka u vrelo jelo na kraju). Referenca: jagnjeća čorba. |
| **Legir NE** | u prženiji, piti, sarmi, kolačima, projari… |
| **Posebni termini** | zaprška, legir → poseban pasus ispod tog koraka, ne u svim receptima |
| **Obične reči** | dinstati, propržiti, narendati — ne objašnjavati |
| **Provera** | `instructions[i]` = Korak i+1; sastojci = original |
| **Original** | Ne menjaj tekst sastojaka ni načina pripreme — čak i ako ima grešaka |
| **description** | Uvod: šta je jelo + kada dobro dođe (Korak 2a); ne uputstvo |
| **SEO dodaci** | Napomene i objašnjenja — novi, gramatički ispravan tekst |

---

## 6. Checklist pre commita

**Sadržaj:**

- [ ] YAML: description, prep/cook/total_time, servings, nutrition,
      ingredients, instructions — po šablonu iz Koraka 2
- [ ] **Original sačuvan:** sastojci i koraci = isti tekst kao u izvoru
- [ ] `instructions[i]` = Korak i+1, reč po reč, bez prefiksa „Korak N."
- [ ] **description:** uvod (šta + kada), 120–200 karaktera — nije uputstvo
- [ ] SEO dodaci (napomene, objašnjenja) gramatički ispravni
- [ ] Telo: `**Način pripreme:**` + Korak 1…N sa `<span id="step-N"></span>`
- [ ] Nema „Potrebno je", starog „Priprema" ni starih `<img>` u telu
- [ ] Nema korak slika ni komentara o njima (⛔ Appendix A je neaktivan)
- [ ] title, permalink, date, categories, tags, guid, id netaknuti
- [ ] Nema starih pogrešnih polja (`ingreedients`, `preptime`…)

**Slike:**

- [ ] `slug.hero.jpg` (1200×675) + og (1200×630) + kartica (800×600) +
      hero.800 (800×450)
- [ ] YAML: image, og_image, card_image pokazuju na te fajlove
- [ ] Nema escajga, plastičnih ni metalnih poslužavnica
- [ ] Hero (AI): **nema ostataka hrane / mrvica / prosute hrane** na stolu oko posude
- [ ] Imena fajlova: tačke, mala slova, bez kvačica

**Mašinska provera (asistent izvršava pre commita):**

```bash
# YAML validan i dimenzije tačne:
ruby -ryaml -e 'YAML.load_file(ARGV[0].sub(/\.md$/,"")+".md")' _posts/ime.md \
  || python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]).read().split('---')[1])" _posts/ime.md
python3 - <<'EOF'
from PIL import Image
import sys
ocekivano = {"hero": (1200, 675), "og": (1200, 630),
             "kartica": (800, 600), "hero.800": (800, 450)}
# prilagodi putanju i slug:
for tip, dim in ocekivano.items():
    p = f"wp-content/uploads/GODINA/slug.{tip}.jpg"
    assert Image.open(p).size == dim, f"{p}: {Image.open(p).size} != {dim}"
print("Slike OK")
EOF
```

- [ ] Git: fajl commitovan pre izmene; commit posle izmene urađen
      (push — vlasnik)

---

## 7. Prioritet — GA4

Radi recepte po saobraćaju (`top.csv` na Desktopu), ne po datumu fajla.

| Talas | Fokus |
| ----- | ----- |
| Top 1–80 | dopuni gde fali, očisti duplikate |
| Top 81–150 | potpuna renovacija |
| Ostatak | po kategorijama |

Jedan recept = jedan commit, redom sa liste, bez čekanja „ok" između recepata
(pravilo iz sekcije 1). Push na live radi vlasnik kad pregleda promene.

---

## 8. Razrešene kolizije (stara uputstva)

| Stari dokument | Staro pravilo | **Sada važi (ovaj dokument)** |
| -------------- | ------------- | ----------------------------- |
| renoviranje.txt | „samo tekst", ne diraj slike | Potpuna renovacija uključuje hero set |
| renoviranje.txt | ne menjaj `image:` | Možeš dodati/izmeniti `image`, `og_image`, `card_image` uz hero set |
| renoviranje.txt | čekaj „ok" pre sledećeg | Commit odmah; recepti sa liste redom bez pauze; push radi vlasnik |
| renoviranje.txt | commit „samo tekst" | commit „potpuno renoviran" |
| slike.txt | master samo na Drive | master može u repo kao arhiva; nije obavezan na sajtu |
| slike.txt | crop za korake | korak slike su ⛔ neaktivne; pravilo protiv cropa u Appendix A |
| slike.txt | (sve ostalo) | tabela dimenzija je sada u Koraku 4 — slike.txt se ne koristi |

Ako nađeš novo protivrečje — pitaj vlasnika pre nego što nastaviš.

---

## 9. Primer — minimum za jedan recept

**Recept:** Paprikaš sa svinjetinom

1. Tekst: 4 koraka + završni pasus
2. Hero set: `paprikas.sa.svinjetinom.hero.jpg` + og + kartica + hero.800
   (AI generisan, jer je original 240 px — vidi Korak 3, grana < 400 px)
3. Commit (A+B) → vlasnik pushuje

**Anti-primer:** JEDNOSTAVNI KOLAČ OD BUNDEVE sa crop-om iste fotografije za
više slika — **ne ponavljati** (detalji u Appendix A).

---

## 10. Kompletan primer pre → posle

*Primer je **ilustrativan** (skraćen, izmišljeni recept radi prikaza formata).
Za stvarni renoviran recept iz repoa vidi
`_posts/2011-03-22-jagnjeca-corba.md`.*

**PRE (stari format):**

```markdown
---
id: 123
title: KROMPIR SALATA SA RENOM
date: 2011-04-05
author: ime
layout: post
permalink: /krompir-salata-sa-renom/
published: true
categories:
  - salate
tags:
  - krompir
guid: http://superkuvar.com/?p=123
image: /wp-content/uploads/2011/04/krompir-240.jpg
---
**Potrebno je:** 500 g krompira, 2 kašike rena, 100 ml kisele pavlake, so

**Priprema:** Krompir oljuštiti i skuvati u slanoj vodi. Ren narendati i
pomešati sa pavlakom pa preliti preko toplog krompira.

Salata se služi topla.

<img src="/wp-content/uploads/2011/04/krompir-240.jpg" />
```

**POSLE (novi format):**

```markdown
---
id: 123
title: KROMPIR SALATA SA RENOM
date: 2011-04-05
author: ime
layout: post
permalink: /krompir-salata-sa-renom/
published: true
description: >-
  Krompir salata sa renom je jednostavno, blago ljuto jelo od kuvanog
  krompira, rena i kisele pavlake. Odlična je kao topao prilog uz pečenje
  ili lagana večera.
prep_time: PT10M
cook_time: PT25M
total_time: PT35M
servings: 4 porcije
nutrition: oko 180 kalorija po porciji
ingredients:
  - 500 g krompira
  - 2 kašike rena
  - 100 ml kisele pavlake
  - so
instructions:
  - Krompir oljuštiti i skuvati u slanoj vodi.
  - Ren narendati i pomešati sa pavlakom pa preliti preko toplog krompira.
image: /wp-content/uploads/2011/krompir.salata.sa.renom.hero.jpg
og_image: /wp-content/uploads/2011/krompir.salata.sa.renom.og.jpg
card_image: /wp-content/uploads/2011/krompir.salata.sa.renom.kartica.jpg
categories:
  - salate
tags:
  - krompir
guid: http://superkuvar.com/?p=123
---
**Način pripreme:**

<span id="step-1"></span>**Korak 1.** Krompir oljuštiti i skuvati u slanoj
vodi.

<span id="step-2"></span>**Korak 2.** Ren narendati i pomešati sa pavlakom
pa preliti preko toplog krompira.

Salata se služi topla. Najbolje ide uz pečeno meso, a ren joj daje blagu
ljutinu zbog koje osvaja na prvi zalogaj.
```

Obrati pažnju: koraci su **doslovno** stari tekst pripreme; originalna
napomena „Salata se služi topla." je zadržana doslovno, a SEO rečenica je
**dodata posle nje**; `title`, `permalink`, `date`, `guid` su netaknuti;
staro `image` polje je zamenjeno hero setom, a stari `<img>` obrisan.

---

## Appendix A — Korak slike (⛔ NEAKTIVNO — ne primenjuj)

*Ova pravila se čuvaju za budućnost. Primenjuju se tek kada vlasnik u tabeli
STATUS PRAVILA promeni C u AKTIVNO. Do tada asistent NE generiše korak slike,
NE umeće ih u telo i NE ostavlja komentare o njima u receptima.*

**Kada se aktivira, važi:**

- Redosled postaje A → B → C → D; imena `slug.korak1.jpg` …, dimenzija
  900×675, umetanje `![Korak N — naziv](putanja)` odmah posle
  `**Korak N.**` u telu; JPEG ~60–100 KB; u YAML `instructions` ništa se
  ne menja.
- **Pravilo 1 — postoje stare korak fotografije (≥ 400 px, različite faze):**
  koristi ih, samo resize na 900×675; mapiraj na najvizuelnije korake.
- **Pravilo 2 — postoji samo jedna fotografija gotovog jela:** hero set iz
  nje; korak slike **generisati posebno** po sadržaju koraka. **Zabranjeno:**
  crop iste fotografije na različite uglove (gravity, PIL crop, „različit"
  MD5); tri kadra istog gotovog jela kao korak1–3.
  *Anti-primer:* JEDNOSTAVNI KOLAČ OD BUNDEVE — tri koraka = isti pečeni
  kolač iz drugog ugla. *Ispravno za taj recept:* korak1 = narendana bundeva
  i testo u posudi; korak2 = testo u plehu pred pečenje; korak3 = pečen
  kolač isečen na kocke.
- **Pravilo 3 — koliko korak slika:** 2–4; ne za svaki tekstualni korak, samo
  gde je vizuelno smisleno (mešanje, sipanje u pleh, pečenje, ključni trik,
  serviranje).
- **Prompt skica za korak:** `Step N: [RADNJA iz teksta koraka], close-up 4:3
  food photography, natural light, no cutlery, no plastic trays, no text`
  (+ resize na 900×675).
- **Provera pre commita:** svaka korak slika = drugačija faza; nijedna nije
  crop heroa/mastera; vizuelna provera jedna pored druge (ne samo MD5) —
  odnosno programska provera dimenzija + ručni pregled na localhost-u.

---

*superkuvar.com · Jedan dokument = sva pravila za transformaciju recepta*
