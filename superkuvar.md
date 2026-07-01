# SUPERKUVAR.COM
## Kompletno uputstvo — transformacija jednog recepta

**Datum:** jun 2026 · **Repo:** `/home/dj/repos/superkuvar.github.io` · **Sajt:** https://superkuvar.com

**Ovaj dokument zamenjuje** `renoviranje.txt` i `slike.txt`. Jedan dokument = sva pravila.

---

## 0. Git repo i commit (obavezno)

**Jedini repo za rad:**

```
/home/dj/repos/superkuvar.github.io
```

**Zabranjeno:** rad u drugim klonovima, worktree folderima ili kopijama repoa
(npr. `.grok/worktrees/...`). Lokalni pregled uvek iz **ovog** foldera:

```bash
cd /home/dj/repos/superkuvar.github.io
bundle exec jekyll serve --livereload
```

→ http://localhost:4000

**Commit pre izmene:** Pre nego što se krene sa izmenom bilo kog fajla
(`_posts/...`, layout, CSS, slike…), taj fajl mora biti **commitovan** u git-u.

**Commit posle izmene:** Kada se izmena završi, odmah **commituj** sve izmenjene
fajlove. Asistent ne ostavlja necommitovane izmene.

**Push na live:** Asistent **ne pushuje** na GitHub. Vlasnik pregleda promene
(`git status`, `git diff`, localhost) i sam radi `git push origin master` kad
je zadovoljan.

**Ova uputstva** (`superkuvar.md`, `superkuvar.art.md`): commituj ih pre i posle
izmene pravila — isti princip kao za recepte i članke.

---

## 1. Šta napišeš asistentu

```
Potpuno renoviraj recept:
URL: https://superkuvar.com/...
```

To je dovoljno. Asistent radi sve ispod i **commituje**; vlasnik pushuje na live.

**Važno:** jedan recept = jedan posao. **Bez batch moda** — recept po recept, individualno.

---

## 2. Šta znači „potpuno renoviran“

Jedan recept = **dva dela + commit** (privremeno). Tekst bez hero seta **nije gotov**.

| Deo | Rezultat |
|-----|----------|
| **A. Tekst** | YAML + Korak 1, 2, 3… u telu |
| **B. Hero set** | glavna slika + og + kartica |
| **C. Korak slike** | 2–4 slike u tekstu posle koraka — **⏸ privremeno se ne rade** (vidi ispod) |
| **D. Commit** | `git commit` (push radi vlasnik) |

**⏸ Privremeno: korak slike se ne rade.** Radi pojednostavljenja unapređenja sajta,
renovacija recepta za sada obuhvata samo **A (tekst) + B (hero set)**. Sva pravila o
korak slikama u ovom dokumentu **ostaju** — vraćaju se u budućnosti kad se krene sa
korak slikama. U telu članka **ne umetaj** `slug.korak1.jpg` … dok traje ova izmena.

**Referenca:** jagnjeća čorba (`_posts/2011-03-22-jagnjeca-corba.md`)

**Redosled (sada):** A → B → D. **Redosled (budućnost):** A → B → C → D.
Nikad obrnuto (hero pre teksta pravi duplikate i pogrešne slike).

---

## 3. Transformacija — pet koraka (glavni tok)

### Korak 1 — Pročitaj original

- Otvori `_posts/....md` i razumi šta se zaista kuva.
- Ne izmišljaj sastojke. Ne kopiraj fraze iz drugog recepta.
- Proveri postojeće slike: YAML `image:`, `<img>` u članku, fajlovi u `wp-content/uploads/`.

### Korak 2 — Pilot tekst (YAML + telo)

**Originalni tekst — ne menjati:** Sastojci i način pripreme moraju **ostati kao u originalu** — iste reči, isti redosled, iste formulacije (uključujući stare pravopisne ili gramatične greške). **Ne prepisuj, ne lektorši i ne „poboljšavaj“** tekst recepta.

**Šta smeš da dodaš (za SEO i čitljivost):**

| Dodatak | Gde | Primer |
|---------|-----|--------|
| **Uvod** | YAML `description` | vidi **Korak 2a** ispod |
| **Napomene** | završni pasus ili poseban blok | serviranje, varijante, saveti iz originalne napomene |
| **Objašnjenja termina** | na kraju članka | dinstanje, zaprška, legir — samo ako se pojavljuju u originalu |

SEO i kvalitet pisanja postižu se **dodacima**, ne izmenom starog teksta recepta.

**Dodaj u YAML:**

| Polje | Primer |
|-------|--------|
| `description` | **obavezno** — uvodni tekst po Koraku 2a |
| `prep_time` | `PT20M` |
| `cook_time` | `PT40M` |
| `total_time` | `PT1H` |
| `servings` | `4 porcije` |
| `nutrition` | `oko 280 kalorija po porciji` |
| `ingredients` | lista sastojaka — **doslovno iz originala** |
| `instructions` | koraci — **isti tekst kao u telu**, samo podeljen po koracima |

**Telo članka (ispod `---`):**

```
**Način pripreme:**

<span id="step-1"></span>**Korak 1.** ...

<!-- privremeno: korak slike se ne umetaju
![Korak 1 — naziv](/wp-content/uploads/.../slug.korak1.jpg)
-->

<span id="step-2"></span>**Korak 2.** ...
...
Završni pasus / napomena (novi tekst, SEO — 1–2 rečenice).
...
**Objašnjenja kulinarskih termina:** (novi tekst, po potrebi)
```

**Koraci u telu:** originalni tekst načina pripreme, podeljen na Korak 1…N — **bez preformulisanja**.

**Obriši iz tela:** zaglavlje „Potrebno je“ (sastojci idu u YAML), „Priprema“ u starom formatu, sve stare `<img>`.

**Ne menjaj:** `title`, `permalink`, `date`, `categories`, `tags`, `guid`, `id`.

**Možeš dodati u YAML:** `image`, `og_image`, `card_image` (u fazi slika).

**Stara pogrešna polja (ne koristi):** `ingreedients`, `recipeinstructions`, `recipeyield`, `preptime`, `cooktime`.

### Korak 2a — `description` (uvodni tekst, obavezno)

**Šta je:** 1–2 rečenice **uvoda** u YAML polju `description`. Pojavljuje se na početku stranice, u Google pretrazi i pri deljenju.

**Svrha:** SEO + da čitalac odmah razume **šta je jelo** i **kada dobro dođe**.

**Nije:** uputstvo za kuvanje, kopija „Način pripreme“, lista koraka.

**Mora da sadrži:**

1. **Šta je jelo** — vrsta jela i glavni sastojci (**samo iz originala**).
2. **Karakter** — npr. kremasto, toplo, lagano, zasitno (ako odgovara receptu).
3. **Kada dobro dođe** — npr. hladni dani, ručak, večera, porodični obrok, sezona.

**Ne sme:**

- prepisivati korake („oprati, oljuštiti, kuvati…“);
- izmišljati sastojke koji nisu u originalu;
- koristiti prazan šablon tipa „domaći recept iz kategorije supe i čorbe“.

**Dužina:** oko 120–200 karaktera (1–2 rečenice).

**Formula:**

```
[Naziv jela] je [kakvo je jelo] od [glavni sastojci iz originala].
[Zašto / kada poslužiti — jedna kratka rečenica].
```

**Primer (ČORBA OD BUNDEVE I ŠARGAREPE):**

> Čorba od bundeve i šargarepe je kremasto, toplo jelo od bundeve, šargarepe i praziluka sa pirinčem. Odlična je za hladnije dane, lagan ručak ili večeru, a uz kiselu pavlaku postaje još puniji obrok.

### Korak 2b — Provera originala (obavezno pre slika)

Pre slika **uporedi sa originalom** i proveri:

- `ingredients` i svaki **Korak N** — ista reč po reč kao u izvornom receptu
- `instructions[i]` = Korak i+1 (isti tekst, isti redosled)
- `description`, završni pasus i **Objašnjenja** — jedini novi tekst; tu piši gramatički ispravno
- nisi slučajno zamenio reči, ispravio pravopis ili dodao sastojke/korake

Ako si promenio originalni tekst recepta — vrati ga. Greške iz originala **ostaju**.

### Korak 3 — Odluka o slikama (algoritam)

**⏸ Privremeno preskočeno za korak slike.** Ovaj korak se sada odnosi samo na **hero set**
(B). Pravila za korak slike ispod ostaju za budućnost — ne briši ih.

Prvo proveri šta postoji u `wp-content/uploads/GODINA/MESec/` za taj recept.

#### Pravilo 1 — Postoje stare korak fotografije (≥ 400 px, različite) *(budućnost)*

**⏸ Privremeno se ne primenjuje** — korak slike se trenutno ne rade.

Ako u upload folderu ima **2–4 različite** originalne fotografije koje prikazuju **različite faze** pripreme (ne isto gotovo jelo):

- **Koristi ih** za `slug.korak1.jpg` … — samo resize na **900×675**
- Mapiraj na najvizuelnije korake u tekstu
- Hero set može iz najbolje fotografije gotovog jela ili posebno generisanog heroa

#### Pravilo 2 — Postoji samo jedna fotografija gotovog jela *(budućnost — korak slike)*

Tipičan slučaj: jedan stari WP JPG pečenog kolača ili jela na tanjiru.

- **Hero, og, kartica, hero.800, master** → iz te fotografije (resize/crop po `slike.txt`)
- **Korak slike** → **generisati posebno** (AI ili ručno), po **sadržaju koraka** u receptu

**Zabranjeno** u ovom slučaju:

- crop iste fotografije na različite uglove (gravity, PIL crop, „različit“ MD5)
- tri kadra istog gotovog jela kao korak1, korak2, korak3

**Primer greške:** JEDNOSTAVNI KOLAČ OD BUNDEVE — tri koraka = isti pečeni kolač iz drugog ugla. **Pogrešno.**

**Ispravno za taj recept:**

| Slika | Šta prikazuje |
|-------|----------------|
| korak1 | narendana bundeva, mutena jaja, testo u posudi |
| korak2 | testo sipano u pleh, pred pečenjem |
| korak3 | pečen kolač isečen na kocke, posut šećerom |

#### Pravilo 3 — Koliko korak slika *(budućnost)*

- Generiši **2–4** korak slike
- **Ne** za svaki tekstualni korak — samo tamo gde je **vizuelno smisleno**
- Biraj: mešanje/mutenje, sipanje u pleh, pečenje u toku, ključni trik, serviranje
- Umetni sliku odmah **posle** odgovarajućeg `**Korak N.**` u markdownu

#### Ostala pravila

```
Ima slika >= 400 px?  → DA: resize u hero set
                      → koraci: Pravilo 1 ili 2 (gore), ne automatski crop
Nema slike uopšte?     → pitaj vlasnika; sa odobrenjem → AI za hero i korake
Više originalnih?      → najbolja gotovog jela = hero; faze pripreme = koraci
Nisi siguran?          → ne pushuj; pitaj
```

- **Ne upscale-uj** sitne JPG-ove (< 400 px duža strana).
- **Ne uzimaj** slike drugog recepta.
- **Stare `<img>`** u tekstu obriši u Koraku 2; slike se vraćaju kao hero set (koraci — u budućnosti).

#### Provera korak slika pre commita *(budućnost — privremeno preskočiti)*

- [ ] Svaka korak slika = **drugačija faza** postupka, ne isti tanjir/pleh
- [ ] Nijedna korak slika nije crop heroa/mastera (osim ako je to bila originalna WP fotografija te faze)
- [ ] Otvori sve korak JPG-ove jedan pored drugog — ako izgledaju kao ista slika, generiši ponovo

### Korak 4 — Hero set *(+ korak slike u budućnosti)*

**Imena fajlova:** `{slug}.{tip}.jpg` — reči odvojene **tačkom**, mala slova, bez kvčica (č→c, š→s, ž→z, đ→dj).

| Fajl | Dimenzija | Gde se koristi |
|------|-----------|----------------|
| `slug.hero.jpg` | 1200×675 | YAML `image:`, vrh stranice |
| `slug.hero.800.jpg` | 800×450 | mobilni (resize iz heroa) |
| `slug.og.jpg` | 1200×630 | YAML `og_image:`, Facebook deljenje |
| `slug.kartica.jpg` | 800×600 | YAML `card_image:`, grid |
| `slug.korak1.jpg` … | 900×675 | u tekstu posle Korak N — **⏸ privremeno se ne rade** |
| `slug.master.jpg` | arhiva | kopija originala (opciono u repo) |

**Redosled pravljenja (sada):** 1.hero → 2.og → 3.kartica → 4.hero.800 → (opciono) master

**Redosled pravljenja (budućnost):** … → 5.korak1…N → 6.master

**YAML posle slika:**

```yaml
image: /wp-content/uploads/GODINA/slug.hero.jpg
og_image: /wp-content/uploads/GODINA/slug.og.jpg
card_image: /wp-content/uploads/GODINA/slug.kartica.jpg
```

**Umetanje koraka u tekst** *(budućnost — privremeno ne umetati):**

```markdown
![Korak 2 — naziv jela](/wp-content/uploads/GODINA/slug.korak2.jpg)
```

odmah **posle** tog koraka. Biraj **2–4 najvizuelnija koraka** (ne svaki). Svaka korak-slika mora prikazivati **različitu fazu** — nikad istu fotografiju gotovog jela na više mesta.

### Korak 5 — Commit (obavezno)

```bash
cd /home/dj/repos/superkuvar.github.io
git add _posts/ime.md wp-content/uploads/.../slug.*.jpg
git commit -m "Recept: NAZIV — potpuno renoviran"
```

**Ne radi `git push`** — vlasnik pregleda i sam pushuje na live.

**Commit samo kad je recept potpun** (A+B; C korak slike privremeno nije obavezan).
Nepotpun → pitaj, ne commituj.

---

## 4. Kadriranje i AI promptovi

**Opšti stil** (u svaki AI prompt):

> Fotorealistična fotografija hrane. Prirodno dnevno svetlo sa leve strane, tople boje. Drvena podloga ili svetli stolnjak. Bez teksta, logoa, vodenog žiga. Za slatko: umerena slatkoća, domaća kuhinja.

**Zabrane na slikama** (hero, og, kartica i koraci):

- **Bez escajga** — viljuške, noževi, kašike, štapići, posude za escajg
- **Bez plastičnih poslužavnica** — plastični tanjiri, tacne, posude, kutije
- **Bez metalnih poslužavnica** — metalne tacne, plitici, poslužni plehovi (osim pleha za pečenje u koraku pečenja)
- **Dozvoljeno:** drvena daska, keramička zdjela, staklena posuda, emajlirani pleh za pečenje, platneni stolnjak
- Ako AI ubaci escajg ili plastiku — **regeneriši** sliku sa eksplicitnom zabranom u promptu

**Varijacija na slikama** (dozvoljeno):

- AI slike **ne moraju biti vizuelno identične** — dozvoljena je prirodna varijacija u uglu, posudi, kadru i osvetljenju između heroa i koraka, i među koracima
- Možeš generisati **više varijanti** iste slike (drugi seed, blago izmenjen prompt) i uzeti najbolju koja poštuje zabrane i prikazuje pravu fazu
- Korak slike **ne moraju** imati potpuno istu podlogu ili posudu kao hero — važno je da svaka slika prikazuje **drugačiju fazu** postupka i da deluje apetitno i domaće
- Varijacija **nije** izgovor za crop iste fotografije gotovog jela niti za tri gotovo ista kadra — to i dalje zabranjeno (vidi Korak 3, Pravilo 2)

| Tip | Kadar | Prompt skica |
|-----|-------|----------------|
| **Hero** | 45° odozgo, jelo u centru, 16:9, prostor oko tanjira | `[GOTOVO JELO] on [POSUDA], 45 degree food photography, wide 16:9, warm daylight, no text, 1200x675` |
| **OG** | isto jelo, šire, jelo niže u kadru (FB seče gore/dole) | `same dish, wider 1.91:1, subject lower in frame, safe zone, 1200x630` ili crop heroa |
| **Korak** | bliže, 4:3, **jedna radnja / jedna faza**, sličan domaći stil (varijacija posude/kadra OK) | `Step N: [RADNJA iz teksta koraka], close-up 4:3 food photography, natural light, no cutlery, no plastic trays, no text, 900x675` |
| **Kartica** | crop iz heroa, jelo popunjava kadar | crop hero na 800×600 |

**JPEG:** kvalitet 80–85 %. Hero ~80–150 KB, korak ~60–100 KB.

**Skripta za resize:** `scripts/process_recipe_images.py` — samo za **hero set** iz postojećeg originala ≥ 400 px. **Ne koristi** za generisanje korak slika iz iste fotografije.

---

## 5. Pravila teksta — zabrane

| Pravilo | Detalj |
|---------|--------|
| **Legir** | Samo ako recept STVARNO ima legir (žumance + kisela pavlaka u vrelu jelo na kraju). Referenca: jagnjeća čorba, Korak 3 + pasus **Legir:** ispod. |
| **Legir NE** | u prženiji, piti, sarmi, kolačima, projari… |
| **Posebni termini** | zapreška, legir → poseban pasus ispod tog koraka, ne u svim receptima |
| **Obične reči** | dinstati, propržiti, narendati — ne objašnjavati |
| **Provera** | `instructions[i]` = Korak i+1; sastojci = original |
| **Original** | **Ne menjaj** tekst sastojaka ni načina pripreme — čak i ako ima grešaka |
| **description** | Uvod: šta je jelo + kada dobro dođe (Korak 2a); ne uputstvo |
| **SEO dodaci** | Napomene i objašnjenja — novi, gramatički ispravni tekst |
| **Korak slike** | 2–4 **različite faze** postupka; **ne** crop heroa/mastera kad postoji samo jedna fotka gotovog jela — **⏸ privremeno se ne rade** |

---

## 6. Checklist pre pusha

- [ ] YAML: description, vremena, servings, nutrition, ingredients, instructions
- [ ] **Original sačuvan:** sastojci i koraci = isti tekst kao u izvoru
- [ ] **description:** uvod (šta + kada), po Koraku 2a — nije uputstvo
- [ ] **SEO dodaci:** napomene, objašnjenja — gramatički ispravni
- [ ] Telo: Način pripreme + Korak 1…N sa `<span id="step-N">`
- [ ] Nema „Potrebno je“ ni starih `<img>` u telu
- [ ] `slug.hero.jpg` + og + kartica + hero.800
- [ ] YAML: image, og_image, card_image
- [ ] ~~2–4 korak slike umetnute posle odgovarajućih koraka~~ *(privremeno — preskočiti)*
- [ ] ~~**Korak slike = različite faze** (vizuelna provera, ne samo MD5)~~ *(budućnost)*
- [ ] **Nema escajga, plastičnih ni metalnih poslužavnica** na slikama
- [ ] Imena fajlova: tačka, bez kvčica
- [ ] title, permalink, date, categories netaknuti
- [ ] commit urađen (push — vlasnik)

---

## 7. Prioritet — GA4

Radi recepte po saobraćaju (`top.csv` na Desktopu), ne po datumu fajla.

| Talas | Fokus |
|-------|-------|
| Top 1–80 | dopuni gde fali, očisti duplikate |
| Top 81–150 | potpuna renovacija |
| Ostatak | po kategorijama |

Jedan recept = jedan commit. U batch režimu: odmah na sledeći, bez čekanja „ok“.
Push na live radi vlasnik kad pregleda promene.

---

## 8. Razrešene kolizije (stara uputstva)

| Stari dokument | Staro pravilo | **Sada važi (ovaj dokument)** |
|----------------|---------------|-------------------------------|
| renoviranje.txt | „samo tekst“, ne diraj slike | **Potpuna renovacija** uključuje hero set; korak slike privremeno ne |
| renoviranje.txt | ne menjaj `image:` | Možeš dodati/izmeniti `image`, `og_image`, `card_image` uz hero set |
| renoviranje.txt | čekaj „ok“ pre sledećeg | **Commit** odmah; push radi vlasnik |
| renoviranje.txt | commit „samo tekst“ | commit **„potpuno renoviran“** |
| slike.txt | master samo na Drive | master može u repo kao arhiva; nije obavezan na sajtu |
| slike.txt | crop za korake | **Zabranjen** crop heroa kad je jedina fotka gotovog jela |

Ako nađeš novo protivrečje — pitaj vlasnika pre nego što nastaviš.

---

## 9. Primer — minimum za jedan recept

**Recept:** Paprikaš sa svinjetinom

1. Pilot: 4 koraka + završni pasus
2. Hero: `paprikas.sa.svinjetinom.hero.jpg` (AI jer original 240 px)
3. *(budućnost)* Koraci: `korak1.jpg` (luk), `korak2.jpg` (meso), `korak3.jpg` (kuvanje) — **različite faze**
4. Commit (A+B) → vlasnik pushuje → https://superkuvar.com/paprikaš-sa-svinjetinom/

**Anti-primer:** JEDNOSTAVNI KOLAČ OD BUNDEVE sa crop-om iste fotografije — **ne ponavljati**.

---

*superkuvar.com · Jedan dokument = sva pravila za transformaciju recepta*