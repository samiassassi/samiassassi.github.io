# Sami Assassi: academic website

Static trilingual site (English at the root, French in `fr/`, Arabic RTL in `ar/`) for GitHub Pages.
No framework: one Python script generates every page from one content file.

```
content.py        ← ALL text (EN / FR / AR): bio, publications, projects, teaching, advisory, talks, CV
build.py          ← page layouts + interface strings (menus, buttons, headings)
assets/style.css  ← design (Calibri Light, "Terroir" palette, light/dark, RTL, print)
assets/site.js    ← value-chain explorer, publication filters, map tooltips, theme toggle
assets/map.json   ← simplified wilaya map (generated once by tools/make_map.py)
docs/             ← GENERATED site: this is what GitHub Pages serves (don't edit by hand)
source/           ← original CVs and photo (not published)
```

## Edit and rebuild

1. Edit `content.py` (e.g. add a publication to `PUBS`, a talk to `TALKS`, news to `NEWS`).
2. Run `python build.py`.
3. Preview: `python -m http.server 8765 --directory docs`, then open http://localhost:8765

Profile links (Google Scholar, LinkedIn, ResearchGate) are empty in `PERSON` and therefore hidden;
paste a URL to make them appear everywhere.

**Adding a publication:** copy an entry in `PUBS`, give it a unique `k`, set `status` (`pub`, `forth`, `review`),
`th` (themes: `land`, `farm`, `contract`, `market`, `city`) and the `doi` without `https://doi.org/`.
To feature it in the value-chain explorer, add its `k` to the matching theme's `pubs` list in `THEMES`.

## Publish on GitHub Pages

Target address: **https://samiassassi.github.io** (GitHub organization `samiassassi`).
`source/` (original CVs and photo) is git-ignored and never published.

1. On GitHub, create the free organization **samiassassi** (github.com/organizations/plan).
2. In that organization, create an empty **public** repository named **samiassassi.github.io** (no README, no licence).
3. From a terminal in this folder: `git push -u origin main`
4. In the repository: *Settings → Pages → Build and deployment*: Source **Deploy from a branch**, branch **main**, folder **/docs** → Save.
5. After a minute the site is live at https://samiassassi.github.io

If the name `samiassassi` is taken, choose another organization name, then change `SITE_URL` in `build.py`,
run `python build.py`, and point git at the new repository:
`git remote set-url origin https://github.com/<org>/<org>.github.io.git`

**Updating later:** edit `content.py` → `python build.py` → `git add -A` → `git commit -m "Update"` → `git push`.

## To confirm with Sami

- Laboratory Director 2023–2025 and ENSA Scientific Council 2021–2026 come from the **French CV only**; they're not in the English CV.
- Email `assassisami@hotmail.com` and ORCID are shown publicly.
- Tamazight listed as a native language (French CV: "Berbère", full marks).
- Arabic text: have a native reader proofread, especially institution names.
- Google Scholar / LinkedIn / ResearchGate URLs, if he wants them shown.
- Photo: crop of the White House picture (EXIF removed). A higher-resolution portrait would look sharper on retina screens.
