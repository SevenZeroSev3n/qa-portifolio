import pytest
from playwright.sync_api import Page
from pages.wiki_home import WikiHome
from pages.wiki_article import WikiArticle

@pytest.mark.parametrize(
    "term, expected_title",
    [
        ("Playwright (software)", "Playwright (software)"),
        ("Python (programming language)", "Python (programming language)"),
    ],
)
def test_wikipedia_search(page: Page, term: str, expected_title: str):
    home = WikiHome(page)
    home.goto()
    home.search(term)

    article = WikiArticle(page)
    article.expect_article(expected_title)
