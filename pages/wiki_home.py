# pages/wiki_home.py
import re
import urllib.parse
from playwright.sync_api import Page, expect

class WikiHome:
    def __init__(self, page: Page):
        self.page = page

    def goto(self):
        self.page.goto("https://en.wikipedia.org/", wait_until="domcontentloaded")
        self.page.set_default_timeout(15_000)

    def search(self, term: str):
        q = urllib.parse.quote(term)
        url = (
            "https://en.wikipedia.org/w/index.php"
            f"?title=Special:Search&search={q}&go=Go&ns0=1"
        )
        self.page.goto(url, wait_until="domcontentloaded")
        expect(self.page).to_have_url(
            re.compile(r"/(wiki/|w/index\.php\?title=Special%3ASearch)")
        )
