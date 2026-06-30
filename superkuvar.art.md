SUPERKUVAR.COM — UPUTSTVO ZA ČLANKE (ARTICLE)
==============================================

Cilj: informativni tekstovi (zdravlje, istorija, vodiči, načini pripreme bez
jednog recepta) sa pravom SEO šemom, sidebarom „Sadržaj“ i **vizuelnim
karticama podsekcija** (obrazac: Srpska kafa, Turska kafa… na /kafa/).

Repo:       /home/dj/repos/superkuvar.github.io
Layout:     _layouts/article.html
Referenca:  /otrovne-pecurke/  i  /kafa/
Paralelno:  superkuvar.md (recepti), slike.txt (dimenzije slika)


0. GIT REPO I COMMIT (OBAVEZNO)
-------------------------------

**Jedini repo za rad:**

    /home/dj/repos/superkuvar.github.io

**Zabranjeno:** rad u drugim klonovima, worktree folderima ili kopijama repoa
(npr. `.grok/worktrees/...`). Lokalni pregled uvek iz ovog foldera:

    cd /home/dj/repos/superkuvar.github.io
    bundle exec jekyll serve --livereload

→ http://localhost:4000

**Commit pre izmene:** Pre nego što se krene sa izmenom bilo kog fajla
(`_posts/...`, layout, CSS, slike…), taj fajl mora biti commitovan u git-u.

**Commit posle izmene:** Kada se izmena završi, odmah commituj sve izmenjene
fajlove. Asistent ne ostavlja necommitovane izmene.

**Push na live:** Asistent **ne pushuje** na GitHub. Vlasnik pregleda promene
(`git status`, `git diff`, localhost) i sam radi `git push origin master` kad
je zadovoljan.

**Ova uputstva** (`superkuvar.md`, `superkuvar.art.md`): commituj ih pre i posle
izmene pravila — isti princip kao za članke i recepte.


1. KADA PIŠEŠ ČLANAK, A KADA RECEPT
-----------------------------------

  ČLANAK (layout: article)              RECEPT (layout: post)
  ────────────────────────────          ─────────────────────
  Više tema / sekcija u jednom tekstu    Jedno jelo, jedan tok
  Nema „Potrebno je“ / Korak 1–N        ingredients + Korak 1–N
  Sidebar: sections → „Sadržaj“         Sidebar: ingredients
  JSON-LD: Article (+ ItemList)         JSON-LD: Recipe
  ### → kartice (Srpska kafa stil)      Koraci sa step-N

  Piši članak kada:
  - enciklopedija, zdravlje, istorija (otrovne pečurke, silicijum)
  - vodič sa više varijanti (kafa: srpska, turska, bosanska, ledena)
  - nema smisla jedan linearni recept ni lažan Recipe schema

  Piši recept (superkuvar.md) kada:
  - jelo ili piće sa jasnim sastojcima i koracima (čorba, tiramisu, pizza)


2. KAKO IZGLEDA STRANICA
------------------------

  Desktop (grid kao kod recepta — .recipe-layout):

    ┌──────────────────┬─────────────────────────────────────┐
    │  Sadržaj         │  Uvodni pasus                       │
    │  (sticky panel)  │  ## Glavna sekcija                  │
    │                  │  ┌─ ### Srpska kafa (kartica) ──┐ │
    │  • Sekcija       │  │ 1. korak… slika desno →      │ │
    │    – Srpska kafa │  └───────────────────────────────┘ │
    │    – Turska kafa │  ┌─ ### Turska kafa (kartica) ──┐ │
    │  • Sledeća       │  │ 1. korak…                    │ │
    │                  │  └───────────────────────────────┘ │
    │                  │  ## Sledeća sekcija …               │
    └──────────────────┴─────────────────────────────────────┘

  Mobilni: sidebar „Sadržaj“ iznad teksta, zatim hero i članak u jednoj koloni.

  Iznad grida: breadcrumb, naslov (h1), description, meta (autor, datum, min
  čitanja), hero slika 16:9.


3. YAML — KOMPLETAN ŠABLON
--------------------------

```yaml
---
id: 123
title: NASLOV ČLANKA
date: 2020-01-03
author: ime
layout: article
permalink: /url-clanka/
published: true
description: 1–2 rečenice uvoda za Google i početak stranice. Šta je tema + zašto čitati.
about: Kratka tema za schema (opciono)
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
item_list:
  - name: Stavka za listu
    description: Jedna rečenica (opciono, za ItemList SEO)
---
```

### Obavezna polja

| Polje | Pravilo |
|-------|---------|
| `layout` | uvek `article` |
| `description` | pravi uvod, 120–220 znakova; **ne** „Sadržaj: …“ |
| `image` | `slug.hero.jpg` |
| `og_image` | `slug.og.jpg` |
| `card_image` | `slug.kartica.jpg` |
| `sections` | sidebar „Sadržaj“ — obavezno za duže članke |
| `categories`, `tags` | konkretni tagovi, ne samo kategorija |

### Zabranjena polja (recept)

`ingredients`, `instructions`, `prep_time`, `cook_time`, `total_time`,
`servings`, `nutrition`

### Ne menjati

`title`, `permalink`, `date`, `id`, `guid`, `author`


4. sections — SIDEBAR „SADRŽAJ“
-------------------------------

Sidebar se puni iz YAML polja `sections:`. **Ne piši** TOC u markdown telu.

### Pravila za id

- `id` u YAML **mora** odgovarati anchoru u telu: `## Naslov {#id}`
- id piši latinicom, malim slovima, reči spojene crticom: `srpska-kafa`, `amanita-phalloides`
- `name` u sidebaru = kratki naslov za čitaoca (može srpski, sa kvacicama)
- Svaka stavka u `items:` = jedan `###` u telu

### Dva nivoa

```
sections:
  - name: Načini kuvanja          ← ## u telu
    id: nacini-kuvanja
    items:
      - name: Srpska kafa          ← ### u telu (kartica)
        id: srpska-kafa
      - name: Turska kafa
        id: turska-kafa
```

Klik u sidebaru skroluje na `#srpska-kafa`.


5. VIZUELNE KARTICE PODSEKCIJA — OBAVEZAN OBRAZAC
-------------------------------------------------

**Referentni izgled:** /kafa/ — blokovi „Srpska kafa“, „Turska kafa“, „Bosanska
kafa“, „Ledena kafa“. Svaki novi članak sa više pod-tema **mora** koristiti isti
obrazac, ne običan tekst ili liste.

### Šta aktivira karticu

Layout (`_layouts/article.html`) i CSS (`assets/css/superkuvar.css`) automatski
pretvaraju svaki **`###` naslov koji je direktno dete** glavnog teksta u
karticu (`.article-subsection`):

- `###` mora biti **na vrhu kolone teksta** (sibling `h2`, ne unutar liste ili
  drugog bloka)
- Sve do sledećeg `###` ili `##` ulazi u istu karticu (pasusi, liste, slike)
- Naslov kartice = tekst `###` (npr. „Srpska kafa“, „Napoletana“, „Amatoksini“)
- `id` u `{#srpska-kafa}` = anchor za sidebar i skrol

**Ne piši pod-teme kao bold, podnaslov u pasusu ili bullet listu** — uvek `###`.

### Kako kartica izgleda (ne menjaj u markdownu — dolazi iz CSS-a)

| Element | Stil |
|---------|------|
| Telo kartice | Bela pozadina, senka, zaobljeni uglovi, tanka ivica |
| Naslov (`###`) | Gradient traka (narandžasto → belo), **narandžasta leva ivica** 4px |
| Parna kartica (2., 4. …) | Braon leva ivica, blago krem gradient |
| Numerisana lista u kartici | **Narandžasti brojevi** (koraci postupka) |
| Slika u kartici (desktop ≥640px) | **Desno**, max ~220px — prostor levo za reklamu |
| Slika u kartici (mobilni) | Puna širina kartice |

### Obrazac za pisanje (kopiraj strukturu)

Svaka **varijanta / vrsta / pod-tema** = jedan red u `sections.items` **i**
jedan `###` blok u telu. Naslov u sidebaru i naslov kartice treba da se
poklapaju (npr. sidebar „Srpska kafa“ → `### Srpska kafa {#srpska-kafa}`).

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

### Bosanska kafa {#bosanska-kafa}

1. U džezvi prokuvati samo vodu…
2. …

### Ledena kafa {#ledena-kafa}

1. Skuvati jaču kafu…
2. …
```

Isti princip za enciklopediju (pečurke, pizze):

```markdown
## Poznate pizze {#poznate-pizze}

Uvod sekcije jednom rečenicom.

### Napoletana {#napoletana}

![Pizza napoletana](/wp-content/uploads/.../pizza.napoletana.jpg)

Klasičan napuljski stil — beli luk u nadevu.

### Siciliana {#siciliana}

![Pizza siciliana](/wp-content/uploads/.../pizza.siciliana.jpg)

Ribani ovčji sir, slana riba, masline…
```

### Šta NE raditi (kartica se neće pojaviti ili će izgled pogrešno)

| Loše | Dobro |
|------|-------|
| `**Srpska kafa**` + pasus | `### Srpska kafa {#srpska-kafa}` |
| Bullet lista varijanti pod `##` | Svaka varijanta = poseban `###` |
| `####` ili `#` za pod-temu | Samo `###` za karticu |
| `###` unutar numerisane liste | `###` na početku, lista ispod |
| Jedan dugačak pasus za sve vrste | Jedna kartica po vrsti |
| `## Srpska kafa` za varijantu | `##` samo za poglavlje; varijanta = `###` |

### Kada koristiti kartice

- **Uvek** kad u sidebaru imaš `items:` (varijante kafe, vrste pečuraka, tipovi
  pizze, toksini, sorte…)
- **Uvek** kad članak poredi više načina / vrsta / pod-tema
- Jedna pod-tema = jedna kartica = jedan `###` = jedan `id` u YAML-u

`##` poglavlja (npr. „Načini kuvanja“, „Poznate pizze“) **nisu** kartice — to
su naslovi iznad grupe kartica. Opšti tekst sekcije (mere, uvod) ide **između**
`##` i prvog `###`, van kartica.


6. TELO ČLANKA — KAKO SE PIŠE
-----------------------------

Sve ispod `---` ide u **desnu kolonu**. Levi panel dolazi automatski iz YAML.
Vizuelni stil pod-tema — vidi **sekciju 5** (kartice kao Srpska / Turska kafa).

### Hijerarhija naslova

| Nivo | Markdown | Uloga |
|------|----------|-------|
| h1 | — | **ne piši** — layout stavlja `title` |
| h2 | `## Sekcija {#id}` | poglavlje (Toksini, Načini kuvanja) |
| h3 | `### Podnaslov {#id}` | **kartica** — varijanta, vrsta, pod-tema |

**Nikad `#` u telu** — samo `##` i `###`.

### Redosled na stranici

```
Uvodni pasus (1–3 rečenice, drugačije formulisan od description)

## Prva sekcija {#prva-sekcija}
Uvod sekcije (opciono). Slika sekcije (opciono).

### Podsekcija A {#podsekcija-a}    ← kartica
Tekst, numerisana lista ili pasusi.

### Podsekcija B {#podsekcija-b}    ← kartica
…

**Upozorenje:** ili **Napomena:** — automatski narandžasti callout blok.

## Zaključak {#zaključak}
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
- Slika u kartici: stavi odmah posle `###` ili posle kratkog uvoda

### Upozorenje i Napomena

Počni pasus sa:

```
**Upozorenje:** tekst…
**Napomena:** tekst…
```

Layout automatski dodaje narandžasti blok (kao Legir kod recepta). Callout
**ne** ide unutar `###` kartice ako važi za celu sekciju — stavi ga pre `##`
ili između `##` i prvog `###`.

### Šta ne pišeš u telu

- `<nav>` / ručni sadržaj
- `**Korak 1.**` i `<span id="step-N">`
- lista „Potrebno je“
- AdSense `<script>` blokovi
- `#` naslovi prvog nivoa
- bold umesto `###` za pod-teme (gubi se vizuelni stil kartica)


7. item_list — SEO LISTA (OPCIONO)
----------------------------------

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


8. JSON-LD I SEO
----------------

Automatski iz `_layouts/article.html`:

| Schema | Kada |
|--------|------|
| **Article** | uvek |
| **ItemList** | ako postoji `item_list:` |
| **BlogPosting** | jekyll-seo-tag ({% seo %}) — duplo je OK |

**Ne koristiti:** Recipe (lažan recept), MedicalWebPage (YMYL).

`description` u YAML = meta description i og:description (ne TOC).

Za članke je article layout **bolji za SEO** od starog `layout: post` sa
praznim Recipe schema.


9. SLIKE
--------

Dimenzije i imena — vidi `slike.txt` (isto kao recepti).

| Fajl | Dimenzija | YAML / upotreba |
|------|-----------|-----------------|
| slug.hero.jpg | 1200×675 | `image:` |
| slug.hero.800.jpg | 800×450 | srcset (automatski) |
| slug.og.jpg | 1200×630 | `og_image:` |
| slug.kartica.jpg | 800×600 | `card_image:` |

Slug: latinica, tačke, bez kvčica — npr. `otrovne.pecurke`, `kafa`.

### Slike u tekstu (unutar kartica — sekcija 5)

- Sliku stavi **unutar** `###` kartice (posle naslova ili kratkog uvoda)
- Desktop: automatski desno, max ~220px — vidi tabelu u sekciji 5
- Alt tekst obavezan: `![Amanita phalloides — zelena pupavka](...)`

Hero slika = jedna na vrhu stranice (iz YAML `image:`), ne duplirati u telu
osim ako ilustruje sekciju.


10. REKLAME
----------

- Leaderboard: header (layout)
- In-content: automatski posle uvoda / pred prvim `##` (layout)
- Bottom: ispod članka
- **Ne** ugrađivati AdSense u markdown

Article layout je **čistiji za reklame** od starog teksta sa ručnim slotovima.


11. REFERENTNI PRIMERI (KOPIRAJ STRUKTURU)
------------------------------------------

### A) Otrovne pečurke — enciklopedija + lista vrsta

- URL: /otrovne-pecurke/
- `sections`: Toksini (6 toksina) + Najotrovnije (4 vrste) + Zaključak
- `item_list`: 4 vrste pečuraka
- Telo: `##` poglavlja, svaki toksin i svaka vrsta = `###` kartica
- Slike vrsta unutar `###` kartica

### B) Kafa — vodič sa varijantama (ZLATNI STANDARD KARTICA)

- URL: /kafa/
- `sections`: O kafi, Prženje, Ječam, Načini kuvanja (4 varijante), Dekaf
- `item_list`: 4 načina kuvanja
- Telo: **Srpska / Turska / Bosanska / Ledena kafa** = `###` kartice + numerisani
  koraci — **kopiraj ovaj vizuelni obrazac** za sve slične članke
- Kategorija: `napici` (ne mora biti `zdravlje`)

### C) Istorija pizze — enciklopedija vrsta

- URL: /pizza-istoria/
- `sections`: Počeci, Napulj, Poznate pizze (4 vrste u `items`)
- Telo: Napoletana, Siciliana, Romana, Margherita = `###` kartice sa slikama


12. CHECKLIST PRE COMMITA
-------------------------

- [ ] `layout: article`
- [ ] `description` = pravi uvod (ne sadržaj)
- [ ] `sections:` — svaki `id` ima odgovarajući `##` ili `### {#id}` u telu
- [ ] Svaka stavka u `sections.items` = `###` kartica (obrazac kao Srpska kafa)
- [ ] Nema bold/liste umesto `###` za varijante i pod-teme (sekcija 5)
- [ ] Nema TOC u markdown telu
- [ ] Nema Recipe polja ni `layout: post`
- [ ] Hero + og + kartica u YAML
- [ ] Nema AdSense u telu
- [ ] View Source: Article JSON-LD, nema Recipe
- [ ] Klikovi u sidebaru skroluju na sekcije
- [ ] `title`, `permalink`, `date` netaknuti

Provera lokalno: `bundle exec jekyll serve` → http://localhost:4000/url/


13. GIT
-------

```bash
cd /home/dj/repos/superkuvar.github.io
git add _posts/ime-clanka.md wp-content/uploads/.../slug.*
git commit -m "Članak: NASLOV — article layout i sekcije"
```

**Ne radi `git push`** — vlasnik pregleda i sam pushuje na live.

Uključi u commit i izmene u `superkuvar.art.md` / `superkuvar.md` ako su
ažurirana pravila rada.


14. UNIVERZALNI UPIT ZA ASISTENTA
---------------------------------

```
Superkuvar — novi ili renoviran članak po superkuvar.art.md

Fajl: _posts/....md
URL: https://superkuvar.com/...

- layout: article
- YAML: description, sections (sa items), hero set, about, item_list po potrebi
- Telo: uvod + ## sekcije + ### kartice {#id} (vizuelni stil kao Srpska/Turska kafa)
- Svaka stavka u sections.items = ### kartica — ne bold, ne bullet lista
- Poštuj sekciju 5 superkuvar.art.md (article-subsection kartice)
- Bez TOC u telu, bez Recipe polja, bez AdSense
- NE menjaj: title, permalink, date, id
- Commit (bez push — vlasnik pushuje)
- Repo: /home/dj/repos/superkuvar.github.io (ne drugi klon)
```


15. BRZA POREĐENJA (ZAKLJUČCI IZ RADA)
--------------------------------------

| Pitanje | Odgovor |
|---------|---------|
| Kafa — recept ili članak? | **Članak** (više varijanti + enciklopedija) |
| Gde ide sadržaj (TOC)? | YAML `sections:`, panel „Sadržaj“ |
| Kako istaknuti pod-teme? | **`###` + `{#id}`** → kartice (Srpska kafa obrazac) |
| Vizuelni stil varijanti? | Uvek `###` kartice — **ne** bold, **ne** bullet pod `##` |
| Referenca za kartice? | /kafa/ (Srpska, Turska, Bosanska, Ledena kafa) |
| Vrste u sidebaru? | `items:` pod roditeljskom sekcijom = isti naslovi kao `###` |
| SEO schema? | Article + opciono ItemList |
| Slike u podsekciji? | Unutar `###` kartice; desno na desktopu (sekcija 5) |
| Pizza? | Recept (`post`) — jedan tok koraka |
| superkuvar.art.md u git-u? | **Da** — commituj pre/posle izmene pravila |
| Push na live? | **Ne** — samo vlasnik, posle pregleda |
| Početna „Najnoviji recepti“? | **Ne** — `layout: article` i kategorija `zdravlje` se preskaču |

### Početna stranica

Članci (`layout: article`) i postovi u kategoriji `zdravlje` **ne ulaze** u
„Najnoviji recepti“ na početnoj. Recepti (npr. pizza, tiramisu) ostaju.
Novi članak: postavi `layout: article` — automatski isključen sa home.

---

*superkuvar.com · Uputstvo za članke (article)*