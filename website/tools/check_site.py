"""Check the built site in headless Chromium.

Serves site/ on localhost, opens every page, and reports console errors,
failed requests and internal links that point at missing files. Saves a
desktop (1280 px) and mobile (390 px) full-page screenshot of each page.

Usage:
    py -3.12 maicro-marketing/tools/check_site.py [--shots-dir DIR]
Exit code 1 if any problem is found.
"""

from __future__ import annotations

import argparse
import functools
import http.server
import logging
import sys
import threading
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

from playwright.sync_api import Page, sync_playwright

PROJECT_DIR = Path(__file__).resolve().parent.parent
SITE_DIR = PROJECT_DIR / "site"
VIEWPORTS = {"desktop": {"width": 1280, "height": 900}, "mobile": {"width": 390, "height": 844}}

logger = logging.getLogger("check-site")


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:  # noqa: A002 - signature fixed by the base class
        return


def start_server() -> tuple[http.server.ThreadingHTTPServer, str]:
    handler = functools.partial(QuietHandler, directory=str(SITE_DIR))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_address[1]}/"


def list_pages() -> list[str]:
    pages = sorted(path.relative_to(SITE_DIR).as_posix() for path in SITE_DIR.rglob("*.html"))
    return [page for page in pages if not page.startswith("shots/")]


def find_broken_links(page: Page, base_url: str) -> list[str]:
    hrefs = page.eval_on_selector_all(
        "a[href], link[href], img[src], script[src]",
        "elements => elements.map(element => element.getAttribute('href') || element.getAttribute('src'))",
    )
    broken = []
    for href in hrefs:
        absolute = urljoin(page.url, href)
        if not absolute.startswith(base_url):
            continue
        relative = unquote(urlparse(absolute).path).lstrip("/")
        target = SITE_DIR / relative
        if target.is_dir():
            target = target / "index.html"
        if not target.exists():
            broken.append(href)
    return broken


def check_page(page: Page, base_url: str, page_path: str, shots_dir: Path | None, viewport_name: str) -> list[str]:
    problems: list[str] = []
    page.on("console", lambda message: problems.append(f"console {message.type}: {message.text}")
            if message.type in ("error", "warning") else None)
    page.on("requestfailed", lambda request: problems.append(f"request failed: {request.url}"))
    response = page.goto(base_url + page_path, wait_until="networkidle")
    if response is None or response.status != 200:
        problems.append(f"status {response.status if response else 'none'}")
    if viewport_name == "desktop":
        problems += [f"broken link: {href}" for href in find_broken_links(page, base_url)]
    if shots_dir:
        shot = shots_dir / viewport_name / (page_path.replace("/", "__").removesuffix(".html") + ".png")
        shot.parent.mkdir(parents=True, exist_ok=True)
        page.screenshot(path=str(shot), full_page=True)
    overflow = page.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
    if overflow > 0:
        problems.append(f"horizontal overflow {overflow}px")
    return problems


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shots-dir", type=Path, default=None)
    arguments = parser.parse_args()

    server, base_url = start_server()
    failures = 0
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        for viewport_name, viewport in VIEWPORTS.items():
            context = browser.new_context(viewport=viewport, is_mobile=viewport_name == "mobile")
            for page_path in list_pages():
                page = context.new_page()
                problems = check_page(page, base_url, page_path, arguments.shots_dir, viewport_name)
                page.close()
                if problems:
                    failures += 1
                    logger.error("%s [%s]\n  %s", page_path, viewport_name, "\n  ".join(problems))
            context.close()
        browser.close()
    server.shutdown()
    logger.info("checked %d pages x %d viewports, %d with problems", len(list_pages()), len(VIEWPORTS), failures)
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
