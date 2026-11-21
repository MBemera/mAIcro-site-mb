# mAIcro site (static redesign draft)

Plain HTML, CSS and a little JavaScript. No framework. Open `index.html` in a browser, or serve the folder:

```sh
cd site
python -m http.server 8000
# then visit http://localhost:8000/
```

Serving over `http://localhost` is the most reliable way to test copying and the IDE connection.

## Pages

| Page | Copy source |
|---|---|
| `index.html` | Carbon v2 copy (`../research/maicro-site-copy-carbon-v2.pdf`), plus live-site sections: "What brings you here?" picker and "Out in the world" |
| `what-is-maicro.html` | Carbon v2 "What mAIcro is" and "How the pieces fit together", moved off the home page |
| `meet.html` | live maicro.app `/meet` (IDE tour, 5 screenshots) |
| `get-started.html` | Carbon v2 steps + live `/get-started` platform commands and after-install links |
| `maicroverse.html` | live `/maicroverse` |
| `courses/index.html`, `courses/<id>.html` (14) | live `/courses` and `/courses/<id>` |
| `stories/index.html`, `stories/<slug>.html` (4) | live `/blog` and `/blog/<slug>` |
| `404.html` | live not-found page |
| `llms.txt` | live `/llms.txt`; only the Stories link changed, from `/blog` to `/stories/` |
| `blog/` | generated redirect pages: `/blog` and `/blog/<slug>/` go to the matching `/stories/` page |

Logos in `images/logo/` are cut from the logo sheet (`../../brand/logo-sheet.png`). The same files are in `../../brand/logos/`.

The home-page demo (`#demo`) plays `media/maicro-explainer.mp4`, a copy of `../../video/mAIcro-explainer.mp4`. Its poster `images/video/maicro-explainer-poster.jpg` is the video's intro card. After re-editing the video, copy the new MP4 over `media/maicro-explainer.mp4` and update the length in the figcaption.

## Scripts

| File | What it does |
|---|---|
| `agent-prompt.js` | "Ask your agent" copy button and `?prompt=1` / `#ask-agent` deep link (unchanged). |
| `interest.js` | Home "What brings you here?" picker. `stories/index.html` shows the same choices and filters the story list by them. Stored in `localStorage` (`maicro-interest`) on this device only. |
| `install.js` | Get started platform picker (auto-selects your OS) and "Copy command" buttons. |
| `ide-connect.js` | "Connect your IDE" + "Open course in mAIcro". Checks `<address>/health` and the IDE page title, stores the address in `localStorage` (`maicro-website-ide-address`), opens `<address>#course=<id>` in a tab named `maicro-ide`. Same behaviour as the live site. The course button stays disabled, with a "Connect your IDE below" hint, until an address checks out. |

Without JavaScript every interest panel, platform command and story stays visible.

## Editing

The pages are generated from `../content/` so the header and footer stay identical everywhere:

```sh
py -3.12 ../tools/build_site.py          # rebuild site/*.html from content/
py -3.12 ../tools/check_site.py --shots-dir shots/buildout   # links, console errors, overflow, screenshots
```

- Page bodies: `../content/pages/*.html` (`{{root}}` becomes the relative path to the site root).
- Courses and stories: `../content/courses.json`, `../content/stories.json`, `../content/stories/*.html`, extracted once from the live maicro.app pages.
- Styles: `styles.css` (edit directly). Scripts: edit directly.

The "Ask your agent" prompt appears in `prompt.txt` and in `<pre id="agent-prompt">` in `../content/pages/home.html`; change both.

## Before publishing

- Re-check the **[check]** items in `../research/SITE_COPY.md` (version, image size, local-model support, licence).
- Carbon copy says 15 courses; the live catalogue lists 14. Decide which is right.
- Carbon step 1 says to install and start Docker first; the live install page says the script handles Docker. Both are shown on `get-started.html`; confirm with the founder.
- Remove "Draft redesign" from the footer (`../tools/build_site.py`, `render_footer`).
- The demo video uses the founder's own YouTube footage; get their OK before publishing it. `python -m http.server` has no byte-range support, so seeking in the video only works on a real web host.
