"""Build the static mAIcro site from content/ into site/.

Each page body lives in content/pages/*.html (or is generated from
content/courses.json and content/stories.json). This script wraps every body
in the shared <head>, header and footer, resolves {{root}} to the right
relative prefix for the page's folder depth, and writes plain HTML files.
It also writes redirect pages from the live site's /blog URLs to /stories/.
The output in site/ needs no build step to view: open site/index.html.

Usage:
    py -3.12 maicro-marketing/tools/build_site.py
"""

from __future__ import annotations

import html
import json
import logging
from dataclasses import dataclass, field
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = PROJECT_DIR / "content"
SITE_DIR = PROJECT_DIR / "site"

BRAND_HTML = 'm<span class="ai">AI</span>cro'
DEFAULT_DESCRIPTION = (
    "PostgreSQL 18, generated GraphQL, vector search, graph queries, workflows and an MCP server "
    "in one Docker container on your own computer, plus guided courses in mAIcroverse. "
    "Free to run locally. Early alpha."
)
NAV_ITEMS = [
    ("index.html", "Home", "home"),
    ("meet.html", f"Meet {BRAND_HTML}", "meet"),
    ("maicroverse.html", f"{BRAND_HTML}verse", "maicroverse"),
    ("courses/index.html", "Courses", "courses"),
    ("stories/index.html", "Stories", "stories"),
    ("index.html#ask-agent", "Ask your agent", "ask-agent"),
]

logger = logging.getLogger("build-site")


@dataclass
class Page:
    output: str
    title: str
    body: str
    nav: str = ""
    description: str = DEFAULT_DESCRIPTION
    scripts: list[str] = field(default_factory=list)
    root_override: str | None = None

    @property
    def root(self) -> str:
        if self.root_override is not None:
            return self.root_override
        return "../" * self.output.count("/")


def read_fragment(name: str) -> str:
    return (CONTENT_DIR / "pages" / f"{name}.html").read_text(encoding="utf-8")


def render_nav_links(current: str) -> str:
    links = []
    for href, label, key in NAV_ITEMS:
        current_attribute = ' aria-current="page"' if key == current else ""
        links.append(f'<li><a href="{{{{root}}}}{href}"{current_attribute}>{label}</a></li>')
    return "\n          ".join(links)


def render_header(current: str) -> str:
    nav_links = render_nav_links(current)
    return f"""  <header class="site-header">
    <div class="wrap header-inner">
      <a class="brand" href="{{{{root}}}}index.html"><img src="{{{{root}}}}images/logo/logo-lockup.png" width="1283" height="244" alt="mAIcro home"></a>
      <nav class="site-nav" aria-label="Main">
        <ul class="nav-list">
          {nav_links}
        </ul>
        <a class="nav-cta" href="{{{{root}}}}get-started.html">Get started <span class="arrow" aria-hidden="true">↗</span></a>
      </nav>
      <details class="mobile-menu">
        <summary>Menu</summary>
        <ul>
          {nav_links}
          <li><a href="{{{{root}}}}get-started.html">Get started</a></li>
        </ul>
      </details>
    </div>
  </header>"""


def render_footer() -> str:
    return f"""  <footer class="site-footer">
    <div class="wrap footer-inner">
      <div class="footer-brand-block">
        <img class="footer-icon" src="{{{{root}}}}images/logo/logo-app-icon.png" width="421" height="417" alt="">
        <div>
          <a class="footer-brand" href="{{{{root}}}}index.html">{BRAND_HTML}<span class="ai">.</span></a>
          <p>Make something that matters to you.</p>
        </div>
      </div>
      <div class="footer-groups">
        <div>
          <p class="footer-heading">Explore</p>
          <ul class="footer-links">
            <li><a href="{{{{root}}}}get-started.html">Get started</a></li>
            <li><a href="{{{{root}}}}what-is-maicro.html">What {BRAND_HTML} is</a></li>
            <li><a href="{{{{root}}}}meet.html">Meet {BRAND_HTML}</a></li>
            <li><a href="{{{{root}}}}maicroverse.html">{BRAND_HTML}verse</a></li>
            <li><a href="{{{{root}}}}courses/index.html">Courses</a></li>
            <li><a href="{{{{root}}}}stories/index.html">Stories</a></li>
            <li><a href="{{{{root}}}}index.html#ask-agent">Ask your agent</a></li>
            <li><a href="{{{{root}}}}llms.txt">llms.txt</a></li>
          </ul>
        </div>
        <div>
          <p class="footer-heading">{BRAND_HTML}</p>
          <ul class="footer-links">
            <li><a href="https://www.youtube.com/@TeamBloxez">YouTube ↗</a></li>
            <li><a href="https://github.com/bloxez">GitHub ↗</a></li>
            <li><a href="https://discord.gg/q5YUzxSvJ2">Discord ↗</a></li>
            <li><a href="https://hub.docker.com/r/bloxez/maicro-g2a">Docker image ↗</a></li>
          </ul>
        </div>
        <div>
          <p class="footer-heading">Founder</p>
          <ul class="footer-links">
            <li><a href="https://www.linkedin.com/in/chrisnurse/" aria-label="Founder on LinkedIn">LinkedIn ↗</a></li>
            <li><a href="https://github.com/chrisnurse" aria-label="Founder on GitHub">GitHub ↗</a></li>
            <li><a href="https://www.youtube.com/@TeamBloxez" aria-label="Founder on YouTube">YouTube ↗</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="wrap footer-bottom">
      <p>Made for curious minds and useful little ideas.</p>
      <p>Draft redesign. Facts checked against public sources on 21 November 2026.</p>
    </div>
  </footer>"""


def render_document(page: Page) -> str:
    plain_title = html.escape(page.title)
    scripts = "".join(f'\n  <script src="{{{{root}}}}{script}" defer></script>' for script in page.scripts)
    document = f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#102b40">
  <title>{plain_title}</title>
  <meta name="description" content="{html.escape(page.description)}">
  <meta property="og:title" content="{plain_title}">
  <meta property="og:description" content="{html.escape(page.description)}">
  <meta property="og:type" content="website">
  <link rel="icon" href="{{{{root}}}}images/logo/favicon-32.png" type="image/png" sizes="32x32">
  <link rel="apple-touch-icon" href="{{{{root}}}}images/logo/apple-touch-icon.png">
  <link rel="stylesheet" href="{{{{root}}}}styles.css">{scripts}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>

{render_header(page.nav)}

  <main id="main">
{page.body.rstrip()}
  </main>

{render_footer()}
</body>
</html>
"""
    return document.replace("{{root}}", page.root)


def render_connect_panel() -> str:
    return """        <div class="connect" data-ide-connect>
          <p class="card-label">Connect your IDE</p>
          <p>Running m<span class="ai">AI</span>cro? Save your IDE address to open courses right in your IDE. The address is saved only on this device, and you sign in within the IDE — the website never sees your credentials.</p>
          <form class="connect-form" data-connect-form hidden>
            <label for="ide-address">IDE or server address</label>
            <div class="connect-row">
              <input id="ide-address" name="address" type="url" inputmode="url" autocomplete="url" placeholder="http://localhost:4321/instance/maicroverse/ide" required>
              <button type="submit" class="button button-small">Connect</button>
              <button type="button" class="button button-small" data-disconnect hidden>Forget address</button>
            </div>
          </form>
          <p class="status" data-connect-status role="status" aria-live="polite"></p>
          <noscript><p class="small">Connecting needs JavaScript. You can still open each course README from the IDE project tree.</p></noscript>
        </div>"""


def render_course_list(courses: list[dict]) -> str:
    rows = []
    for course in courses:
        rows.append(f"""          <li>
            <a href="{{{{root}}}}courses/{course['id']}.html">
              <span class="course-name">{course['title']}</span>
              <span class="course-lead">{course['lead']}</span>
              <span class="course-more" aria-hidden="true">Explore course →</span>
            </a>
          </li>""")
    return '        <ul class="course-list">\n' + "\n".join(rows) + "\n        </ul>"


def render_course_section(section: dict) -> str:
    css_class = ' class="course-warning"' if "warning" in section["class"] else ""
    return f"""        <section{css_class}>
          <h2>{section['heading']}</h2>
          {section['html']}
        </section>"""


def render_course_neighbours(courses: list[dict], index: int) -> str:
    links = []
    if index > 0:
        previous = courses[index - 1]
        links.append(f'<a href="{{{{root}}}}courses/{previous["id"]}.html">← {previous["title"]}</a>')
    if index < len(courses) - 1:
        following = courses[index + 1]
        links.append(f'<a class="next" href="{{{{root}}}}courses/{following["id"]}.html">{following["title"]} →</a>')
    return '        <nav class="pager" aria-label="More courses">' + "".join(links) + "</nav>"


def render_course_body(courses: list[dict], index: int) -> str:
    course = courses[index]
    sections = "\n".join(render_course_section(section) for section in course["sections"])
    readme_path = f"scripts/courses/{course['id']}/00.readme.md"
    return f"""    <section class="page-hero" aria-labelledby="page-title">
      <div class="wrap">
        <p class="back-row"><a href="{{{{root}}}}courses/index.html">← Back to courses</a></p>
        <h1 id="page-title">{course['title']}</h1>
        <p class="lead">{course['lead']}</p>
      </div>
    </section>

    <section aria-label="About this course">
      <div class="wrap course-body">
{sections}
      </div>
    </section>

    <section class="band" aria-labelledby="explore-title">
      <div class="wrap course-action">
        <h2 id="explore-title">Open the course in your IDE.</h2>
        <p>Open the course README in your m<span class="ai">AI</span>cro IDE. You’ll need an instance with the courses installed; see <a href="{{{{root}}}}courses/index.html#prepare">Prepare your learning instance</a> in the course catalogue. Opening the README won’t run any scripts.</p>
        <p>On an older IDE without website course-link support, open <code>{readme_path}</code> from the project tree instead.</p>
        <p class="actions"><button type="button" class="button button-primary" data-open-course="{course['id']}" disabled><span>Open course in m<span class="ai">AI</span>cro</span> <span class="arrow" aria-hidden="true">↗</span></button></p>
        <p class="small" data-open-course-hint hidden>Connect your IDE below to enable this button.</p>
{render_connect_panel()}
{render_course_neighbours(courses, index)}
      </div>
    </section>
"""


def render_story_list(stories: list[dict]) -> str:
    rows = []
    for story in stories:
        interests = " ".join(story["interests"])
        rows.append(f"""          <li data-interests="{interests}">
            <a href="{{{{root}}}}stories/{story['slug']}.html">
              <span class="story-title">{story['title']}</span>
              <span class="story-summary">{story['summary']}</span>
              <span class="story-more" aria-hidden="true">Read the story →</span>
            </a>
          </li>""")
    return '        <ul class="story-list">\n' + "\n".join(rows) + "\n        </ul>"


def render_story_body(story: dict, body_html: str) -> str:
    return f"""    <article aria-labelledby="page-title">
      <section class="page-hero">
        <div class="wrap">
          <p class="back-row"><a href="{{{{root}}}}stories/index.html">← Back to stories</a></p>
          <h1 id="page-title">{story['title']}</h1>
          <p class="lead">{story['summary']}</p>
        </div>
      </section>
      <section>
        <div class="wrap prose">
{body_html.rstrip()}
          <p class="pager"><a href="{{{{root}}}}stories/index.html">← More stories</a><a class="next" href="{{{{root}}}}get-started.html">Install m<span class="ai">AI</span>cro →</a></p>
        </div>
      </section>
    </article>
"""


def fill_placeholders(fragment: str, values: dict[str, str]) -> str:
    for key, value in values.items():
        fragment = fragment.replace("{{" + key + "}}", value)
    return fragment


def collect_pages() -> list[Page]:
    courses = json.loads((CONTENT_DIR / "courses.json").read_text(encoding="utf-8"))
    stories = json.loads((CONTENT_DIR / "stories.json").read_text(encoding="utf-8"))
    pages = [
        Page("index.html", "mAIcro: a local backend toolbox and learning sandbox for you and your AI agents",
             read_fragment("home"), nav="home", scripts=["agent-prompt.js", "interest.js"]),
        Page("meet.html", "Meet mAIcro: this is what building looks like", read_fragment("meet"), nav="meet",
             description="A tour of the mAIcro IDE: scripts that document themselves, SchemaPad, CypherPad graphs, dashboards and a wiki beside your work."),
        Page("what-is-maicro.html", "What mAIcro is, and why it's built this way", read_fragment("what-is-maicro"), nav="",
             description="One container instead of five separate services, a toolbox for you and your agents, and a place for learning."),
        Page("get-started.html", "Get started with mAIcro", read_fragment("get-started"), nav="",
             description="Install mAIcro on Windows, WSL, macOS or Linux with one setup command, then open your local IDE.",
             scripts=["install.js"]),
        Page("maicroverse.html", "mAIcroverse: courses and stories", read_fragment("maicroverse"), nav="maicroverse",
             description="Courses and stories to learn mAIcro by making things."),
        Page("courses/index.html", "Courses from mAIcroverse",
             fill_placeholders(read_fragment("courses-index"), {
                 "course_list": render_course_list(courses),
                 "course_count": str(len(courses)),
                 "connect_panel": render_connect_panel(),
             }),
             nav="courses", scripts=["ide-connect.js"],
             description="Hands-on mAIcro courses: Markdown, GraphQL tables, vectors, graphs, workflows, API wrappers, AI signatures, forms and browser automation."),
        Page("stories/index.html", "Stories from mAIcroverse",
             fill_placeholders(read_fragment("stories-index"), {
                 "story_list": render_story_list(stories),
                 "story_count": str(len(stories)),
             }),
             nav="stories", scripts=["interest.js"],
             description="Notes, stories, and little sparks of inspiration for curious minds."),
        Page("404.html", "Page not found · mAIcro", read_fragment("404"), root_override="/"),
    ]
    for index, course in enumerate(courses):
        pages.append(Page(f"courses/{course['id']}.html", f"{course['title']} · mAIcro course",
                          render_course_body(courses, index), nav="courses", scripts=["ide-connect.js"],
                          description=html.unescape(course["lead"])))
    for story in stories:
        body = (CONTENT_DIR / "stories" / f"{story['slug']}.html").read_text(encoding="utf-8")
        pages.append(Page(f"stories/{story['slug']}.html", f"{story['title']} · mAIcro stories",
                          render_story_body(story, body), nav="stories",
                          description=html.unescape(story["summary"])))
    return pages


@dataclass(frozen=True)
class Redirect:
    output: str
    target: str


def collect_redirects(stories: list[dict]) -> list[Redirect]:
    redirects = [Redirect("blog/index.html", "stories/index.html")]
    for story in stories:
        redirects.append(Redirect(f"blog/{story['slug']}/index.html", f"stories/{story['slug']}.html"))
    return redirects


def render_redirect(redirect: Redirect) -> str:
    href = "../" * redirect.output.count("/") + redirect.target
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <meta http-equiv="refresh" content="0; url={href}">
  <title>This page has moved · mAIcro</title>
</head>
<body>
  <p>This page has moved to <a href="{href}">{href}</a>.</p>
</body>
</html>
"""


def write_redirect(redirect: Redirect) -> None:
    target = SITE_DIR / redirect.output
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render_redirect(redirect), encoding="utf-8")


def write_page(page: Page) -> None:
    target = SITE_DIR / page.output
    target.parent.mkdir(parents=True, exist_ok=True)
    document = render_document(page)
    if "{{" in document:
        raise ValueError(f"unfilled placeholder in {page.output}")
    target.write_text(document, encoding="utf-8")


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    pages = collect_pages()
    for page in pages:
        write_page(page)
    stories = json.loads((CONTENT_DIR / "stories.json").read_text(encoding="utf-8"))
    redirects = collect_redirects(stories)
    for redirect in redirects:
        write_redirect(redirect)
    logger.info("wrote %d pages and %d /blog redirects to %s", len(pages), len(redirects), SITE_DIR)


if __name__ == "__main__":
    main()
