# pages/wiki_article.py
import re
from playwright.sync_api import Page, expect

class WikiArticle:
    def __init__(self, page: Page):
        self.page = page
        self.heading = page.locator("#firstHeading")
        # Primeiro parágrafo real (ignora placeholders .mw-empty-elt)
        self.first_paragraph = page.locator(
            "#mw-content-text .mw-parser-output > p:not(.mw-empty-elt)"
        ).first
        # Container da lista de resultados (Special:Search)
        self.results_container = page.locator("#mw-content-text .mw-search-results")

    def _maybe_navigate_from_search_results(self, expected_title: str):
        """Se a busca abriu Special:Search, clica no resultado correto e navega para o artigo."""
        if "title=Special%3ASearch" in self.page.url or "/w/index.php?title=Special:Search" in self.page.url:
            expect(self.results_container).to_be_visible(timeout=15_000)

            # 1) Tenta pelo accessible name exato
            link = self.page.get_by_role("link", name=expected_title, exact=True)
            if not link.count():
                # 2) Fallback pelo atributo title
                link = self.page.locator(f'a[title="{expected_title}"]')

            expect(link.first).to_be_visible(timeout=15_000)
            link.first.click()
            expect(self.page).to_have_url(re.compile(r"/wiki/"), timeout=15_000)

    def expect_article(self, expected_title: str):
        # Se necessário, sai dos resultados para o artigo
        self._maybe_navigate_from_search_results(expected_title)

        # Valida artigo carregado
        expect(self.page).to_have_url(re.compile(r"/wiki/"), timeout=15_000)
        expect(self.heading).to_have_text(re.compile(re.escape(expected_title), re.I), timeout=15_000)
        expect(self.first_paragraph).to_be_visible(timeout=15_000)
        # Segurança extra: evita parágrafo vazio
        expect(self.first_paragraph).not_to_have_text(re.compile(r"^\s*$"), timeout=15_000)
