# QA Web Runner (Python + Playwright)

[![E2E (Playwright Python)](https://github.com//actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com//actions/workflows/ci.yml)

Suite E2E com Playwright + pytest, relatório HTML e CI em 3 navegadores.

## Rodar local
python -m venv .venv && .\.venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install
python -m pytest -q tests/test_wikipedia_search.py --headed
python -m pytest -q tests/test_wikipedia_search.py --html=reports/report.html --self-contained-html
