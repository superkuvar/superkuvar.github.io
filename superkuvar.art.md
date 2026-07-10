# SUPERKUVAR.COM — UPUTSTVO ZA ČLANKE (ARTICLE)

**Verzija:** 2.0 · **Datum:** jul 2026

**Cilj:** informativni tekstovi (zdravlje, istorija, vodiči, načini pripreme
bez jednog recepta) sa pravom SEO šemom, sidebarom „Sadržaj" i **vizuelnim
karticama podsekcija** (obrazac: Srpska kafa, Turska kafa… na `/kafa/`).

**Repo (logički):** `superkuvar/superkuvar.github.io`, grana `master`
**Repo (lokalno):** `/home/dj/repos/superkuvar.github.io`
**Layout:** `_layouts/article.html`
**Referenca:** `/otrovne-pecurke/` i `/kafa/`
**Paralelni dokument:** `superkuvar.md` (recepti; tamo je i tabela dimenzija
slika — `slike.txt` **više ne postoji i ne citira se**)

**Changelog:**
- v2.0 (jul 2026): popravljen markdown (tabela članak/recept, naslovi
  sekcija); uklonjene reference na slike.txt; `article_column` i interno
  linkovanje ubačeni u YAML šablon i checklist; dodata sekcija o tačnosti i
  izvorima (YMYL); dodate smernice za obim; dodat mini primer skeleta.
- v1.x: prvobitna verzija.

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

**Commit pre izmene:** pre izmene bilo kog fajla taj fajl mora biti
commitovan. **Ako nije**, asistent ga prvo commituje
(`git commit -m "backup: <fajl> pre izmene"`), pa tek onda menja.

**Commit posle izmene:** odmah commituj sve izmenjene fajlove. Asistent ne
ostavlja necommitovane izmene.

**Push na live:** asistent **ne pushuje**. Vlasnik pregleda (`git status`,
`git diff`, localhost) i sam radi `git push origin master`.

**Ova uputstva** (`superkuvar.md`, `superkuvar.art.md`): commituj ih pre i
posle izmene pravila; pri izmeni ažuriraj Changelog.

---

## 1. Kada pišeš članak, a kada recept

| | ČLANAK (`layout: article`) | RECEPT (`layout: post`) |
| --- | --- | --- |
| Sadržaj | više tema / sekcija u jednom tekstu | jedno jelo, jedan tok |
| Struktura tela | `##` sekcije + `###` kartice | „Korak 1–N" sa `step-N` |
| Sastojci | nema „Potrebno je" | `ingredients` u YAML |
| Sidebar | `sections:` → panel „Sadržaj" | sastojci |
| JSON-LD | Article (+ ItemList) | Recipe |
| Pod-teme | kartice (Srpska kafa stil) | — |

**Piši članak kada:**

- enciklopedija, zdravlje, istorija (otrovne pečurke, silicijum)
- vodič sa više varijanti (kafa: srpska, turska, bosanska, ledena)
- nema smisla jedan linearni recept ni lažna Recipe schema

**Piši recept (po `superkuvar.md`) kada:**

- jelo ili piće sa jasnim sastojcima i koracima (čorba, tiramisu, pizza)

---

## 2. Kako izgleda stranica

Desktop (grid kao kod recepta — `.recipe-layout`):

```
┌──────────────────┬─────────────────────────────────────┐
│  Sadržaj         │  Uvodni pasus                       │
│  (sticky panel)  │  ## Glavna sekcija                  │
│                  │  ┌─ ### Srpska kafa (kartica) ───┐  │
│  • Sekcija       │  │ 1. korak… slika desno →       │  │
│    – Srpska kafa │  └───────────────────────────────┘  │
│    – Turska kafa │  ┌─ ### Turska kafa (kartica) ───┐  │
│  • Sledeća       │  │ 1. korak…                     │  │
│                  │  └───────────────────────────────┘  │
│                  │  ## Sledeća sekcija …               │
└──────────────────┴─────────────────────────────────────┘
```

Mobilni: sidebar „Sadržaj" iznad teksta, zatim hero i članak u jednoj koloni.

Iznad grida: breadcrumb, naslov (h1), description, meta (autor, datum, min
čitanja), hero slika 16:9.

---

## 3. YAML — kompletan šablon

```yaml
---
id: 123
title: NASLOV ČLANKA
date: 2020-01-03
author: ime
layout: article
permalink: /url-clanka/
published: true
description: >-
  1–2 rečenice uvoda za Google i početak stranice, 120–220 znakova.
  Šta je tema + zašto čitati. Ne „Sadržaj: …".
about: kafa                    # opciono; kratka fraza (2–4 reči, mala slova)
                               # za schema `about` — tema članka, ne rečenica
article_column: kuvarica       # obavezno: kuvarica ili zdravlje (sekcija 12)
image: /wp-content/uploads/GODINA/slug.hero.jpg
og_image: /wp-content/uploads/GODINA/slug.og.jpg
card_image: /wp-content/uploads/GODINA/slug.kartica.jpg
categories:
  - zdravlje
tags:
  - konkretan-tag
sections:
  - name: Glavna sekcija
    id: glavna-sekcija
    items:
      - name: Podsekcija A
        id: podsekcija-a
      - name: Podsekcija B
        id: podsekcija-b
  - name: Druga sekcija
    id: druga-sekcija
item_list:                     # opciono — sekcija 7
  - name: Stavka za listu
    description: Jedna rečenica.
---
```

### Obavezna polja

| Polje | Pravilo |
| ----- | ------- |
| `layout` | uvek `article` |
| `description` | pravi uvod, 120–220 znakova; **ne** „Sadržaj: …" |
| `article_column` | `kuvarica` ili `zdravlje` — obavezno za svaki članak (sekcija 12) |
| `image` | `slug.hero.jpg` |
| `og_image` | `slug.og.jpg` |
| `card_image` | `slug.kartica.jpg` |
| `sections` | sidebar „Sadržaj" — obavezno za duže članke |
| `categories`, `tags` | konkretni tagovi, ne samo kategorija |

### Zabranjena polja (pripadaju receptu)

`ingredients`, `instructions`, `prep_time`, `cook_time`, `total_time`,
`servings`, `nutrition`

### Ne menjati (kod renovacije postojećeg teksta)

`title`, `permalink`, `date`, `id`, `guid`, `author`

---

## 4. `sections` — sidebar „Sadržaj"

Sidebar se puni iz YAML polja `sections:`. **Ne piši** TOC u markdown telu.

### Pravila za id

- `id` u YAML **mora** odgovarati anchoru u telu: `## Naslov {#id}`
- id: latinica, mala slova, reči spojene crticom, **bez kvačica** (č→c, ć→c,
  š→s, ž→z, đ→dj) i bez tačaka — npr. `srpska-kafa`, `amanita-phalloides`,
  `zdravlje-i-kofein`
- `name` u sidebaru = kratki naslov za čitaoca (može srpski, sa kvačicama)
- Svaka stavka u `items:` = jedan `###` u telu

**Napomena o sintaksi:** `{#id}` posle naslova je **kramdown** atribut
(Jekyllov podrazumevani markdown). Radi samo u ovom repou/Jekyllu — na
GitHub previewu se prikazuje kao tekst, to je normalno.

### Dva nivoa

```yaml
sections:
  - name: Načini kuvanja        # ← ## u telu
    id: nacini-kuvanja
    items:
      - name: Srpska kafa       # ← ### u telu (kartica)
        id: srpska-kafa
      - name: Turska kafa
        id: turska-kafa
```

Klik u sidebaru skroluje na `#srpska-kafa`.

---

## 5. Vizuelne kartice podsekcija — obavezan obrazac

**Referentni izgled:** `/kafa/` — blokovi „Srpska kafa", „Turska kafa",
„Bosanska kafa", „Ledena kafa". Svaki novi članak sa više pod-tema **mora**
koristiti isti obrazac, ne običan tekst ili liste.

### Šta aktivira karticu

Layout (`_layouts/article.html`) i CSS (`assets/css/superkuvar.css`)
automatski pretvaraju svaki **`###` naslov koji je direktno dete** glavnog
teksta u karticu (`.article-subsection`):

- `###` mora biti **na vrhu kolone teksta** (sibling `h2`, ne unutar liste
  ili drugog bloka)
- Sve do sledećeg `###` ili `##` ulazi u istu karticu (pasusi, liste, slike)
- Naslov kartice = tekst `###` (npr. „Srpska kafa", „Napoletana",
  „Amatoksini")
- `{#srpska-kafa}` = anchor za sidebar i skrol

**Ne piši pod-teme kao bold, podnaslov u pasusu ili bullet listu** — uvek `###`.

### Kako kartica izgleda (ne menjaj u markdownu — dolazi iz CSS-a)

| Element | Stil |
| ------- | ---- |
| Telo kartice | bela pozadina, senka, zaobljeni uglovi, tanka ivica |
| Naslov (`###`) | gradient traka (narandžasto → belo), narandžasta leva ivica 4px |
| Parna kartica (2., 4. …) | braon leva ivica, blago krem gradient |
| Numerisana lista u kartici | narandžasti brojevi (koraci postupka) |
| Slika u kartici (desktop ≥ 640px) | desno, max ~220px — prostor levo za reklamu |
| Slika u kartici (mobilni) | puna širina kartice |

### Obrazac za pisanje (kopiraj strukturu)

Svaka **varijanta / vrsta / pod-tema** = jedan red u `sections.items` **i**
jedan `###` blok u telu. Naslov u sidebaru i naslov kartice treba da se
poklapaju (sidebar „Srpska kafa" → `### Srpska kafa {#srpska-kafa}`).

```markdown
## Načini kuvanja {#nacini-kuvanja}

**Mera po šoljici:** 1 šoljica vode, 1 kašičica kafe…
(opšti uvod sekcije — **van** kartice, iznad prvog ###)

### Srpska kafa {#srpska-kafa}

1. Džezvu napuniti vodom…
2. …

### Turska kafa {#turska-kafa}

1. U džezvu staviti kafu i šećer…
2. …
```

Isti princip za enciklopediju (pečurke, pizze):

```markdown
## Poznate pizze {#poznate-pizze}

Uvod sekcije jednom rečenicom.

### Napoletana {#napoletana}

![Pizza napoletana](/wp-content/uploads/GODINA/pizza.napoletana.jpg)

Klasičan napuljski stil — beli luk u nadevu.

### Siciliana {#siciliana}

![Pizza siciliana](/wp-content/uploads/GODINA/pizza.siciliana.jpg)

Ribani ovčji sir, slana riba, masline…
```

### Šta NE raditi (kartica se neće pojaviti ili će izgled biti pogrešan)

| Loše | Dobro |
| ---- | ----- |
| `**Srpska kafa**` + pasus | `### Srpska kafa {#srpska-kafa}` |
| bullet lista varijanti pod `##` | svaka varijanta = poseban `###` |
| `####` ili `#` za pod-temu | samo `###` za karticu |
| `###` unutar numerisane liste | `###` na početku, lista ispod |
| jedan dugačak pasus za sve vrste | jedna kartica po vrsti |
| `## Srpska kafa` za varijantu | `##` samo za poglavlje; varijanta = `###` |

### Kada koristiti kartice

- **Uvek** kad u sidebaru imaš `items:` (varijante kafe, vrste pečuraka,
  tipovi pizze, toksini, sorte…)
- **Uvek** kad članak poredi više načina / vrsta / pod-tema
- Jedna pod-tema = jedna kartica = jedan `###` = jedan `id` u YAML-u

`##` poglavlja (npr. „Načini kuvanja", „Poznate pizze") **nisu** kartice — to
su naslovi iznad grupe kartica. Opšti tekst sekcije (mere, uvod) ide
**između** `##` i prvog `###`, van kartica.

---

## 6. Telo članka — kako se piše

Sve ispod `---` ide u **desnu kolonu**. Levi panel dolazi automatski iz YAML.
Vizuelni stil pod-tema — vidi sekciju 5.

### Hijerarhija naslova

| Nivo | Markdown | Uloga |
| ---- | -------- | ----- |
| h1 | — | **ne piši** — layout stavlja `title` |
| h2 | `## Sekcija {#id}` | poglavlje (Toksini, Načini kuvanja) |
| h3 | `### Podnaslov {#id}` | **kartica** — varijanta, vrsta, pod-tema |

**Nikad `#` u telu** — samo `##` i `###`.

### Obim (smernice)

- Članak: **3–7** `##` sekcija; ukupno okvirno **800–2000 reči**. Kraće od
  toga ne opravdava sidebar; duže — razmisli o podeli na dva članka (pitaj
  vlasnika).
- Kartica (`###`): **50–150 reči** ili 3–8 numerisanih koraka. Ne prazne
  kartice od jedne rečenice.
- Uvodni pasus: 1–3 rečenice.

### Redosled na stranici

```markdown
Uvodni pasus (1–3 rečenice, drugačije formulisan od description)

## Prva sekcija {#prva-sekcija}
Uvod sekcije (opciono). Slija sekcije (opciono).

### Podsekcija A {#podsekcija-a}    ← kartica
Tekst, numerisana lista ili pasusi.

### Podsekcija B {#podsekcija-b}    ← kartica
…

**Upozorenje:** ili **Napomena:** — automatski narandžasti callout blok.

## Zaključak {#zakljucak}
…
```

### Uvodni pasus

- Kratak kontekst pre prvog `##`
- **Ne** kopiraj `description` reč po reč
- **Ne** stavljaj listu sadržaja

### Liste i koraci unutar kartice

- Numerisana lista ispod `###` = koraci postupka (kafa, pripreme)
- Običan pasus ispod `###` = objašnjenje (toksini, zdravlje, istorija)
- Može pasus pa lista — oba ostaju u istoj kartici
- Slika u kartici: odmah posle `###` ili posle kratkog uvoda

### Upozorenje i Napomena

Počni pasus sa:

```markdown
**Upozorenje:** tekst…
**Napomena:** tekst…
```

Layout automatski dodaje narandžasti blok (kao Legir kod recepta). Callout
**ne** ide unutar `###` kartice ako važi za celu sekciju — stavi ga pre `##`
ili između `##` i prvog `###`.

### Šta ne pišeš u telu

- `<nav>` / ručni sadržaj
- `**Korak 1.**` i `<span id="step-N">`
- lista „Potrebno je"
- AdSense `<script>` blokovi
- `#` naslovi prvog nivoa
- bold umesto `###` za pod-teme (gubi se vizuelni stil kartica)

---

## 7. `item_list` — SEO lista (opciono)

Kad članak ima **nabrajanje stavki** (vrste kafe, otrovne pečurke, sorte…),
dodaj `item_list:` u YAML. Layout emituje **ItemList** JSON-LD.

```yaml
item_list:
  - name: Srpska kafa
    description: Voda i šećer prvo do ključanja…
  - name: Turska kafa
    description: Kafa i šećer u hladnu vodu…
```

Stavke u `item_list` treba da odgovaraju `###` podsekcijama ili glavnim
temama članka. `description` = jedna kratka rečenica.

---

## 8. JSON-LD i SEO

Automatski iz `_layouts/article.html`:

| Schema | Kada |
| ------ | ---- |
| **Article** | uvek |
| **ItemList** | ako postoji `item_list:` |
| **BlogPosting** | jekyll-seo-tag (`{% seo %}`) — duplo je OK |

**Ne koristiti:** Recipe (lažan recept), MedicalWebPage (YMYL).

`description` u YAML = meta description i og:description (ne TOC).

Za članke je article layout **bolji za SEO** od starog `layout: post` sa
praznim Recipe schema.

---

## 9. Tačnost, izvori i zdravstvene teme (YMYL) — obavezno

Članci o zdravlju, ishrani i bezbednosti (otrovne pečurke!) su YMYL sadržaj —
greška može naneti stvarnu štetu čitaocu. Zato:

- **Nema izmišljanja činjenica.** Doze, toksini, simptomi, nutritivne
  vrednosti, istorijski podaci — samo ono što asistent može da potvrdi u
  pouzdanim izvorima (naučne/medicinske publikacije, zvanične institucije,
  ozbiljne enciklopedije). Nesiguran podatak → izostavi ili pitaj vlasnika.
- **Bez medicinskih saveta i obećanja.** Ne piši „leči", „sprečava bolest",
  „zamenjuje terapiju". Dozvoljeno: opšte, oprezno informisanje
  („istraživanja povezuju…", „tradicionalno se koristi…").
- **Bez uputstava opasnih po život.** Kod tema poput otrovnih pečuraka:
  tekst sme da opisuje vrste i simptome radi prepoznavanja i prevencije, ali
  ne sme da ohrabruje samostalno branje na osnovu članka. Obavezan
  **Upozorenje:** callout (npr. „U slučaju sumnje na trovanje odmah
  potražiti hitnu pomoć; nijedan članak ne zamenjuje stručnu identifikaciju.").
- **Zdravstveni članci** (`article_column: zdravlje`) završavaju se kratkom
  napomenom da tekst ima informativni karakter i ne zamenjuje savet lekara.
- **Brojevi i tvrdnje** koje asistent ne može da potvrdi radije uopšti
  („nekoliko sati", „male količine") nego da navede precizan izmišljen broj.

Ova sekcija ima **prednost** nad SEO ciljevima: bolje kraći i tačan članak
nego dugačak i izmišljen.

---

## 10. Slike

Dimenzije, imena i AI promptovi su **isti kao za recepte** — vidi
`superkuvar.md`, Korak 4 (tabela) i sekciju 4 (promptovi i zabrane:
bez escajga, plastičnih i metalnih poslužavnica, bez teksta).

| Fajl | Dimenzija | YAML / upotreba |
| ---- | --------- | --------------- |
| `slug.hero.jpg` | 1200×675 | `image:` |
| `slug.hero.800.jpg` | 800×450 | srcset (automatski) |
| `slug.og.jpg` | 1200×630 | `og_image:` |
| `slug.kartica.jpg` | 800×600 | `card_image:` |

Slug: latinica, tačke, mala slova, **bez kvačica** — npr. `otrovne.pecurke`,
`kafa`.

### Slike u tekstu (unutar kartica — sekcija 5)

- Sliku stavi **unutar** `###` kartice (posle naslova ili kratkog uvoda)
- Desktop: automatski desno, max ~220px — vidi tabelu u sekciji 5
- Alt tekst obavezan: `![Amanita phalloides — zelena pupavka](...)`

Hero slika = jedna na vrhu stranice (iz YAML `image:`); ne duplirati u telu
osim ako ilustruje sekciju.

---

## 11. Reklame

- Leaderboard: header (layout)
- In-content: automatski posle uvoda / pred prvim `##` (layout)
- Bottom: ispod članka
- **Ne** ugrađivati AdSense u markdown

Article layout je čistiji za reklame od starog teksta sa ručnim slotovima.

---

## 12. Kolona na /clanci/ i interno linkovanje (obavezno)

### `article_column`

Na listi članaka (`clanci.md`, layout `articles`) filter deli sadržaj u dve
kolone. **Svaki članak mora imati** u YAML:

```yaml
article_column: kuvarica   # ili zdravlje
```

| `article_column` | Sadržaj |
| ---------------- | ------- |
| `kuvarica` | tehnike kuvanja, sastojci, zimnica, post, tradicija, bezbednost |
| `zdravlje` | vitamini, prevencija, biljke, suplementi |

Kartica na `/clanci/` prikazuje tag **Kuvarica** ili **Zdravlje**. Opis
stranice `/clanci/` obuhvata zdravlje, ishranu, tehnike kuvanja, sastojke,
tradiciju i bezbednost — ne samo zdravlje.

### Interno linkovanje (obavezno)

Svaki novi članak linkuje **5–10 postojećih recepata** sa superkuvar.com,
**relativnim permalincima** (npr. `[sarma](/sarma/)`), prirodno u tekstu —
ne kao spisak linkova na kraju. Linkuj samo recepte koji stvarno postoje u
`_posts/` (proveri permalink pre linkovanja; ne izmišljaj URL-ove).

### Početna stranica

Članci (`layout: article`) i postovi u kategoriji `zdravlje` **ne ulaze** u
„Najnoviji recepti" na početnoj. Novi članak: `layout: article` → automatski
isključen sa home.

---

## 13. Referentni primeri (kopiraj strukturu)

### A) Otrovne pečurke — enciklopedija + lista vrsta

- URL: `/otrovne-pecurke/`
- `sections`: Toksini (6 toksina) + Najotrovnije (4 vrste) + Zaključak
- `item_list`: 4 vrste pečuraka
- Telo: `##` poglavlja; svaki toksin i svaka vrsta = `###` kartica
- Slike vrsta unutar `###` kartica; obavezno **Upozorenje:** (sekcija 9)

### B) Kafa — vodič sa varijantama (ZLATNI STANDARD KARTICA)

- URL: `/kafa/`
- `sections`: O kafi, Prženje, Ječam, Načini kuvanja (4 varijante), Dekaf
- `item_list`: 4 načina kuvanja
- Telo: Srpska / Turska / Bosanska / Ledena kafa = `###` kartice +
  numerisani koraci — **kopiraj ovaj vizuelni obrazac**
- Kategorija: `napici` (ne mora biti `zdravlje`); `article_column: kuvarica`

### C) Istorija pizze — enciklopedija vrsta

- URL: `/pizza-istoria/`
- `sections`: Počeci, Napulj, Poznate pizze (4 vrste u `items`)
- Telo: Napoletana, Siciliana, Romana, Margherita = `###` kartice sa slikama

### D) Mini skelet novog članka (ilustrativan)

```markdown
---
id: 456
title: DOMAĆA KAFA — VODIČ
date: 2026-07-01
author: ime
layout: article
permalink: /kafa-vodic/
published: true
description: >-
  Vodič kroz načine pripreme domaće kafe — srpska, turska i ledena varijanta,
  sa koracima i merama po šoljici.
about: priprema kafe
article_column: kuvarica
image: /wp-content/uploads/2026/kafa.vodic.hero.jpg
og_image: /wp-content/uploads/2026/kafa.vodic.og.jpg
card_image: /wp-content/uploads/2026/kafa.vodic.kartica.jpg
categories:
  - napici
tags:
  - kafa
sections:
  - name: Načini kuvanja
    id: nacini-kuvanja
    items:
      - name: Srpska kafa
        id: srpska-kafa
      - name: Turska kafa
        id: turska-kafa
item_list:
  - name: Srpska kafa
    description: Voda i šećer prvo do ključanja, pa kafa.
  - name: Turska kafa
    description: Kafa i šećer u hladnu vodu, kuva se zajedno.
---
Malo koje piće prati domaću trpezu kao kafa — evo kako se sprema na dva
tradicionalna načina.

## Načini kuvanja {#nacini-kuvanja}

**Mera po šoljici:** 1 šoljica vode, 1 puna kašičica kafe.

### Srpska kafa {#srpska-kafa}

1. Džezvu napuniti vodom i dodati šećer po ukusu…
2. …

Uz srpsku kafu odlično ide [vanilice](/vanilice/) ili [baklava](/baklava/).

### Turska kafa {#turska-kafa}

1. U džezvu staviti kafu i šećer, naliti hladnom vodom…
2. …
```

---

## 14. Checklist pre commita

**YAML:**

- [ ] `layout: article`
- [ ] `description` = pravi uvod, 120–220 znakova (ne sadržaj)
- [ ] `article_column: kuvarica` ili `zdravlje`
- [ ] `sections:` — svaki `id` ima odgovarajući `## {#id}` ili `### {#id}`
      u telu; id-jevi bez kvačica
- [ ] Hero + og + kartica u YAML (`image`, `og_image`, `card_image`)
- [ ] `item_list` (ako članak nabraja stavke) odgovara `###` karticama
- [ ] Nema Recipe polja ni `layout: post`
- [ ] `title`, `permalink`, `date`, `id`, `guid`, `author` netaknuti
      (kod renovacije)

**Telo:**

- [ ] Uvodni pasus pre prvog `##` (nije kopija description)
- [ ] Svaka stavka u `sections.items` = `###` kartica (obrazac Srpska kafa)
- [ ] Nema bold/liste umesto `###` za varijante i pod-teme (sekcija 5)
- [ ] Nema TOC u telu, nema `#` naslova, nema AdSense
- [ ] Slike unutar kartica sa alt tekstom
- [ ] **5–10 linkova ka postojećim receptima**, relativni permalinci,
      provereni (sekcija 12)
- [ ] **YMYL provera** (sekcija 9): nema izmišljenih podataka, nema
      medicinskih saveta; zdravstvene teme imaju **Upozorenje:** /
      informativnu napomenu
- [ ] Obim u okviru smernica (sekcija 6)

**Provera lokalno:**

- [ ] `bundle exec jekyll serve` → <http://localhost:4000/url/>
- [ ] View Source: Article JSON-LD, nema Recipe
- [ ] Klikovi u sidebaru skroluju na sekcije
- [ ] Kartice se vizuelno renderuju (kao na `/kafa/`)

---

## 15. Git

```bash
cd <root-repoa>
git add _posts/ime-clanka.md wp-content/uploads/GODINA/slug.*
git commit -m "Članak: NASLOV — article layout i sekcije"
```

**Ne radi `git push`** — vlasnik pregleda i sam pushuje na live.

Uključi u commit i izmene u `superkuvar.art.md` / `superkuvar.md` ako su
ažurirana pravila rada.

---

## 16. Univerzalni upit za asistenta

```
Superkuvar — novi ili renoviran članak po superkuvar.art.md

Fajl: _posts/....md
URL: https://superkuvar.com/...

- layout: article
- YAML: description, article_column, sections (sa items), hero set,
  about i item_list po potrebi
- Telo: uvod + ## sekcije + ### kartice {#id} (stil kao Srpska/Turska kafa)
- Svaka stavka u sections.items = ### kartica — ne bold, ne bullet lista
- Poštuj sekciju 5 (kartice), sekciju 9 (YMYL/tačnost) i sekciju 12
  (article_column + 5–10 linkova ka receptima)
- Bez TOC u telu, bez Recipe polja, bez AdSense
- NE menjaj: title, permalink, date, id
- Commit (bez push — vlasnik pushuje)
- Repo: root repoa superkuvar/superkuvar.github.io (ne drugi klon)
```

---

## 17. Brza poređenja (zaključci iz rada)

| Pitanje | Odgovor |
| ------- | ------- |
| Kafa — recept ili članak? | **Članak** (više varijanti + enciklopedija) |
| Gde ide sadržaj (TOC)? | YAML `sections:`, panel „Sadržaj" |
| Kako istaknuti pod-teme? | `###` + `{#id}` → kartice (Srpska kafa obrazac) |
| Vizuelni stil varijanti? | uvek `###` kartice — ne bold, ne bullet pod `##` |
| Referenca za kartice? | `/kafa/` (Srpska, Turska, Bosanska, Ledena) |
| Vrste u sidebaru? | `items:` pod roditeljskom sekcijom = isti naslovi kao `###` |
| SEO schema? | Article + opciono ItemList |
| Slike u podsekciji? | unutar `###` kartice; desno na desktopu (sekcija 5) |
| Dimenzije slika? | `superkuvar.md`, Korak 4 (slike.txt ne postoji) |
| Pizza? | recept (`post`) — jedan tok koraka |
| Zdravstvene tvrdnje? | samo proverene; bez saveta — sekcija 9 |
| superkuvar.art.md u git-u? | **da** — commituj pre/posle izmene pravila |
| Push na live? | **ne** — samo vlasnik, posle pregleda |
| Početna „Najnoviji recepti"? | `layout: article` i kategorija `zdravlje` se preskaču |

---

*superkuvar.com · Uputstvo za članke (article)*
