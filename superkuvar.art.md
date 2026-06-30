SUPERKUVAR.COM — UPUTSTVO ZA ČLANKE (ARTICLE)
==============================================

Cilj: informativni tekstovi (zdravlje, istorija, vodiči) sa pravom SEO šemom,
responsive rasporedom kao kod recepta (sidebar + tekst) — bez lažnog Recipe markupa.

Repo:     /home/dj/repos/superkuvar.github.io
Layout:   _layouts/article.html
Referenca: /otrovne-pecurke/ (pilot)
Paralelno: renoviranje.txt (recepti), slike.txt (slike)


KADA KORISTITI ČLANAK UMESTO RECEPTA
------------------------------------

  ČLANAK (layout: article)          RECEPT (layout: post)
  ─────────────────────────         ─────────────────────
  Nema kuvanja / koraka             Ima sastojke i korake
  Enciklopedija, zdravlje           Jelo ili piće za pripremu
  Više sekcija (##)                 Korak 1–N
  JSON-LD: Article                  JSON-LD: Recipe
  Sidebar: sections (Sadržaj)       Sidebar: ingredients (Potrebno je)

  Primeri članaka: otrovne pečurke, silicijum, pizza-istoria
  Primeri vodiča (i dalje post): kafa, pizza (više varijanti)


RASPORED STRANICE (KAO RECEPT)
------------------------------

  Desktop: grid 300px + 1fr (ista .recipe-layout klasa)

    ┌─────────────────┬──────────────────────────────┐
    │  Sadržaj        │  Tekst članka                │
    │  (sticky)       │  ## sekcije, slike, napomene │
    └─────────────────┴──────────────────────────────┘

  Mobilni: jedna kolona — sidebar iznad teksta (kao „Potrebno je“)

  Analogija:
    recept  →  ingredients:  + panel „Potrebno je“
    članak  →  sections:      + panel „Sadržaj“


YAML — OBAVEZNO
---------------

  layout: article
  description:     1–2 rečenice (pravi uvod za SEO i meta; NE lista sadržaja)
  image:           /wp-content/uploads/.../slug.hero.jpg
  og_image:        /wp-content/uploads/.../slug.og.jpg
  card_image:      /wp-content/uploads/.../slug.kartica.jpg
  published: true
  categories:      [zdravlje]  (ili druga kategorija)
  tags:            konkretne reči (pecurke, toksini…)

  sections:        navigacija u levom panelu (obavezno za duže članke)
    - name: Glavna sekcija
      id: anchor-id          ← mora odgovarati ## naslovu u telu
      items:                 ← opciono, podsekcije (###)
        - name: Podsekcija
          id: podsekcija-id

  Opciono (SEO schema):
  about:           kratka tema članka (npr. "Otrovne pečurke")
  item_list:       lista stavki za ItemList JSON-LD (vidi primer ispod)


PRIMER sections (otrovne pečurke)
---------------------------------

  sections:
    - name: Toksini
      id: toksini
      items:
        - name: Amatoksini
          id: amatoksini
        - name: Muskarin
          id: muskarin
    - name: Najotrovnije pečurke u Srbiji
      id: najotrovnije-pecurke-u-srbiji
    - name: Zaključak
      id: zaključak

  id mora biti isti kao Kramdown anchor iz ## naslova u telu.
  Provera: klik na link u sidebaru skroluje na odgovarajući naslov.


YAML — ZABRANJENO
-----------------

  ingredients, instructions, prep_time, cook_time, total_time,
  servings, nutrition — to su polja recepta; ne koristiti u člancima.


ŠTA SE NE MENJA
---------------

  title, permalink, date, categories (osim dopune tagova), id, guid, author


Telo članka
-----------

  Struktura (samo desna kolona — levi panel dolazi iz sections: u YAML):

    Uvodni pasus (1–3 rečenice) — NE ponavljati description reč po reč

    ## Glavna sekcija {#anchor-id}
    Tekst…

    ### Podsekcija {#pod-anchor}
    Tekst…

    ## Sledeća sekcija {#anchor-2}
    …

    **Upozorenje:** ili **Napomena:** — važni saveti (stilizuje se automatski)

  Pravila:
  - Naslov stranice (h1) dolazi iz layouta — u telu koristiti ## i ###, ne #
  - Anchori: {#id} na kraj ## naslova; id uskladiti sa sections: u YAML
  - Sadržaj (TOC) ide u YAML sections:, NE u telo članka
  - Slike u tekstu: ![opis](/wp-content/uploads/.../fajl.jpg)
  - Bez Korak 1, bez liste sastojaka u telu, bez AdSense skripti
  - Liste, tabele i citati — slobodno u tekstu


JSON-LD (automatski iz layouta)
-------------------------------

  1. Article — uvek:
     headline, description, image, author, datePublished, publisher,
     articleSection (kategorija), about (ako je about: u YAML)

  2. ItemList — ako postoji item_list: u YAML:
     item_list:
       - name: Amanita phalloides
         description: Zelena pupavka — smrtonosna.
       - name: Amanita virosa
         description: Bela pupavka.

  NE koristiti: Recipe, MedicalWebPage (YMYL zahteva medicinski autoritet).


SLIKE (isto kao recepti — vidi slike.txt)
-----------------------------------------

  slug.hero.jpg       1200×675   16:9
  slug.hero.800.jpg   800×450    srcset mobilni
  slug.og.jpg         1200×630   Facebook
  slug.kartica.jpg    800×600    grid kartice
  slug.master.jpg     arhiva

  Slug članka: skraćen naslov latinicom, tačke.
    ZAŠTO SU PEČURKE OTROVNE → otrovne.pecurke

  Slike u tekstu: postojeće fotografije, min. 400 px duža strana;
  po potrebi resize na 900×675 (4:3) za uniformnost.


RESPONSIVE IZGLED (article.html + CSS)
--------------------------------------

  • Isti grid kao recept: .recipe-layout (300px sidebar + tekst)
  • Sidebar: .ingredients-panel.article-sidebar, sticky na desktopu
  • Naslov panela: „Sadržaj“ (umesto „Potrebno je“)
  • Bez sections: .recipe-layout--single, tekst max ~760px
  • Hero 16:9 pun širina kontejnera, srcset na .hero.jpg
  • article-meta-bar: autor, datum, procena čitanja
  • H2/H3 u .article-content: Fraunces, razmaci, scroll-margin za anchor
  • species-list: kartice vrsta + slika (responsive grid)
  • Upozorenje/Napomena: narandžasti callout blok
  • tag-chip red na dnu
  • „Slični članci“ — 3 kartice iz iste kategorije
  • Reklame: leaderboard, in-content (posle uvoda), bottom


UNIVERZALNI UPIT (kopiraj u Grok)
---------------------------------

  Superkuvar — članak po superkuvar.art.md

  Repo: /home/dj/repos/superkuvar.github.io
  Fajl: _posts/....md
  URL: https://superkuvar.com/...

  ZADATAK:
  - layout: article
  - YAML: description, sections, image set, about, item_list (ako ima listu)
  - Telo: ## sekcije (anchor id = sections.id), bez TOC u telu
  - NE menjaj: title, permalink, date, id
  - Commit + push

  ZABRANJENO:
  - ingredients / instructions / prep_time
  - TOC u markdown telu (ide u sections:)
  - layout: post sa praznim Recipe schema
  - AdSense u telu


PROVERA PRE COMMITA
-------------------

  1. layout: article u front matter
  2. sections: u YAML, linkovi rade (#id)
  3. description je pravi uvod (ne TOC)
  4. Nema Recipe u page source
  5. Desktop: sticky sidebar; mobilni: sidebar iznad teksta
  6. Hero + og + kartica u YAML


GIT
---

  git add _layouts/article.html _posts/....md assets/css/superkuvar.css superkuvar.art.md
  git commit -m "Članak: sidebar sections kao Potrebno je"
  git push origin master