import re
from playwright.sync_api import Page, expect

def test_example_domain_title_and_h1(page: Page):
    page.goto("https://example.com/")
    expect(page).to_have_title(re.compile(r"Example Domain", re.I))
    expect(page.locator("h1")).to_have_text(re.compile(r"Example Domain", re.I))
