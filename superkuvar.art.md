SUPERKUVAR.COM — UPUTSTVO ZA ČLANKE (ARTICLE)
==============================================

Cilj: informativni tekstovi (zdravlje, istorija, vodiči) sa pravom SEO šemom,
lepim responsive izgledom — bez lažnog Recipe markupa.

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

  Primeri članaka: otrovne pečurke, silicijum, pizza-istoria
  Primeri vodiča (i dalje post): kafa, pizza (više varijanti)


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

  Opciono (SEO schema):
  about:           kratka tema članka (npr. "Otrovne pečurke")
  item_list:       lista stavki za ItemList JSON-LD (vidi primer ispod)


YAML — ZABRANJENO
-----------------

  ingredients, instructions, prep_time, cook_time, total_time,
  servings, nutrition — to su polja recepta; ne koristiti u člancima.


ŠTA SE NE MENJA
---------------

  title, permalink, date, categories (osim dopune tagova), id, guid, author


Telo članka
-----------

  Struktura:

    <nav class="article-toc"> … ručni sadržaj … </nav>   (opciono)

    Uvodni pasus (1–3 rečenice) — NE ponavljati description reč po reč

    ## Glavna sekcija {#anchor-id}
    Tekst…

    ### Podsekcija
    Tekst…

    ## Sledeća sekcija {#anchor-2}
    …

    **Upozorenje:** ili **Napomena:** — važni saveti (stilizuje se automatski)

  Pravila:
  - Naslov stranice (h1) dolazi iz layouta — u telu koristiti ## i ###, ne #
  - Anchori: {#id} na kraj ## naslova ili pustiti Kramdown da generiše iz naslova
  - Slike u tekstu: ![opis](/wp-content/uploads/.../fajl.jpg)
  - Bez Korak 1, bez „Potrebno je“, bez AdSense skripti u telu
  - Liste, tabele i citati — slobodno


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

  • Jedna kolona, max-width ~760px za tekst (čitljivost)
  • Hero 16:9 pun širina kontejnera, srcset na .hero.jpg
  • article-toc: kartica sa sadržajem, sticky na desktopu (opciono)
  • article-meta-bar: autor, datum, procena čitanja
  • H2 sekcije: razmak, Fraunces, tanka linija iznad (osim prve)
  • H3 podsekcije: manji naslov, više razmaka iznad
  • Slike: zaobljeni uglovi, senka; figure.species-card za vrstu + slika
  • Upozorenje/Napomena: narandžasti blok (kao Legir kod recepta)
  • tag-chip red na dnu
  • „Slični članci“ — 3 kartice iz iste kategorije
  • Reklame: leaderboard (header), in-content (posle uvoda), bottom — kao recept


UNIVERZALNI UPIT (kopiraj u Grok)
---------------------------------

  Superkuvar — članak po superkuvar.art.md

  Repo: /home/dj/repos/superkuvar.github.io
  Fajl: _posts/....md
  URL: https://superkuvar.com/...

  ZADATAK:
  - layout: article
  - YAML: description, image set, about, item_list (ako ima listu)
  - Telo: ## sekcije, bez Recipe polja
  - NE menjaj: title, permalink, date, id
  - Hero set iz postojeće slike (slike.txt)
  - Commit + push

  ZABRANJENO:
  - ingredients / instructions / prep_time
  - layout: post sa praznim Recipe schema
  - AdSense u telu
  - description koji je samo „Sadržaj: …“


PROVERA PRE COMMITA
-------------------

  1. layout: article u front matter
  2. description je pravi uvod (ne TOC)
  3. Nema Recipe u page source (View Source → application/ld+json)
  4. Article + eventualno ItemList prisutni
  5. Hero + og + kartica u YAML
  6. Mobilni: TOC i tekst čitljivi, slike ne prelivaju


GIT
---

  git add _layouts/article.html _posts/....md assets/css/superkuvar.css
  git add wp-content/uploads/.../slug.hero.jpg ...
  git commit -m "Članak: [naslov] — article layout i SEO"
  git push origin master