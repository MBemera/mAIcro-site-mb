"""Tests for the /blog to /stories/ redirect pages in build_site.py."""

from build_site import Redirect, collect_redirects, render_redirect

STORIES = [{"slug": "learning-by-making"}, {"slug": "a-smaller-kind-of-software"}]


def test_collect_redirects_covers_index_and_every_story() -> None:
    redirects = collect_redirects(STORIES)
    assert redirects == [
        Redirect("blog/index.html", "stories/index.html"),
        Redirect("blog/learning-by-making/index.html", "stories/learning-by-making.html"),
        Redirect("blog/a-smaller-kind-of-software/index.html", "stories/a-smaller-kind-of-software.html"),
    ]


def test_render_redirect_uses_path_relative_to_output_folder() -> None:
    story_page = render_redirect(Redirect("blog/learning-by-making/index.html", "stories/learning-by-making.html"))
    index_page = render_redirect(Redirect("blog/index.html", "stories/index.html"))
    assert 'content="0; url=../../stories/learning-by-making.html"' in story_page
    assert 'href="../stories/index.html"' in index_page


def test_render_redirect_is_not_indexed() -> None:
    page = render_redirect(Redirect("blog/index.html", "stories/index.html"))
    assert '<meta name="robots" content="noindex">' in page
