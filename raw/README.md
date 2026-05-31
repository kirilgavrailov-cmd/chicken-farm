# raw/ — Сурови източници (immutable)

Каталог на първоизточниците, от които е извлечено `wiki/`. Това е слой 1 от модела (виж [/CLAUDE.md](../CLAUDE.md)).

> ⚠️ Самите файлове (особено защитени с авторско право) **не се качват в git** — пазят се локално; тук е само описанието. Виж `.gitignore`.

## Източници

### `src-01` — Damme & Hildebrand 2015 (книга)
- **Заглавие:** Legehennenhaltung und Eierproduktion
- **Автори:** Klaus Damme, Ralf-Achim Hildebrand
- **Издател / година:** Verlag Eugen Ulmer, Stuttgart, 2015
- **Обем / формат:** 242 стр., PDF (ebook за лична употреба)
- **Език:** немски
- **Локално:** `~/Downloads/174902-1_21052896.pdf` (извън репото — авторско право)
- **Извлечено в:** `wiki/00`–`wiki/07` (ingest на 2026-05-31)

### `src-02` — ЕС/BG нормативна база (онлайн, свободна)
- **Тип:** първично законодателство и официални страници (не copyright — може и raw да се качи)
- **Източници:** Council Dir. 1999/74/EC, 98/58/EC; Регл. (ЕО) 589/2008; Регл. (ЕС) 1308/2013; Дир. 2002/4/ЕО; Реш. (ЕС) 2017/302 (IED 2010/75/ЕС); Наредба № 25/2005, № 44/2006, № 1/2008; ЗВД чл. 137; ЕК — Laying hens / End the Cage Age
- **Достъп:** EUR-Lex, lex.bg, mzh.government.bg, food.ec.europa.eu
- **Извлечено в:** `wiki/regulation/*` (ingest 2026-05-31)

### `src-03` — Management guides на хибридите (онлайн, свободни)
- **Тип:** официални performance datasheets / management guides
- **Източници:** Lohmann Breeders (Brown-Classic 08.21, LSL-Classic 09.2015); Hy-Line International (Brown 12.2025, W-36 01.2020); Hendrix Genetics ISA (Brown 2016); H&N International (Brown Nick / Nick Chick 2020)
- **Достъп:** сайтове на производителите (PDF, безплатни)
- **Извлечено в:** `wiki/breeds/*` (ingest 2026-05-31)

### `src-04` — Болести: ветеринарни референции (онлайн, свободни)
- **Тип:** референтни ръководства и право
- **Източници:** WOAH Terrestrial Manual (3.3.13 Марек, 3.3.14 Нюкасъл); MSD/Merck Veterinary Manual; EFSA; EU право (2160/2003, 517/2011, 1237/2007, 1177/2006, 2016/429, 2020/687, 2023/361, 1831/2003); рецензирана литература за Dermanyssus (PMC5537931 и др.)
- **Достъп:** woah.org, merckvetmanual.com, EUR-Lex, EFSA, PubMed/PMC
- **Извлечено в:** `wiki/health/*` (ingest 2026-05-31)

### `src-05` — (ОЧАКВА СЕ) Англоезични/BG учебници — категория D
- **Статус:** не е приет; чака локални файлове (copyright → само локално, по `.gitignore`)
- **Кандидати:** Bell & Weaver, *Commercial Chicken Meat and Egg Production* (Springer, 2002); Appleby/Mench/Hughes, *Poultry Behaviour and Welfare* (CABI, 2004); Roodbont *Laying Hen / Egg Signals*; Генчев & Луканов, *Птицевъдство* (Тракийски у-т)
- **За да приема:** пусни PDF/epub в `raw/` (както `src-01`) и кажи кой да извлека
