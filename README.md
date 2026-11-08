# CISC 217 Week 12 — Web APIs with FastAPI

This lab builds a small character API with FastAPI.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '[test]'
python -m pytest -q
```

Several tests should fail initially. Complete the TODOs in `src/cisc217_week12/main.py`.

Run the app with:

```bash
uvicorn cisc217_week12.main:app --reload
```

Then open `/docs` or `/redoc`.
