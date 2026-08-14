# Models4PT Development Guide

This guide describes the repository as it exists today. The documents in
`doc/project-foundation/` describe the broader scientific program and intended
architecture.

## Supported tools

- Python 3.11 is the development and container baseline.
- Python 3.12 is also exercised in continuous integration.
- Node.js 20.19 is the frontend and continuous-integration baseline. Newer
  supported Node.js releases may also be used.
- Docker is optional.

The repository's `.python-version` selects Python 3.11 in version managers that
support that file.

## Backend setup

Create a virtual environment from the repository root:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.lock
python -m pip install --no-deps --no-build-isolation -e .
```

The lockfile contains the complete resolved development dependency set. The
editable installation exposes the local `models4pt` package without asking pip
to resolve a second dependency graph.

Run the API:

```bash
python -m uvicorn models4pt.app:app --reload
```

The current endpoints are:

- `GET /` — basic application response
- `GET /health` — health response
- `GET /docs` — automatically generated FastAPI documentation

Run backend tests:

```bash
python -m pytest -q
```

## Frontend setup

Install the exact dependency tree recorded in `frontend/package-lock.json`:

```bash
npm --prefix frontend ci
```

Run the development server:

```bash
npm --prefix frontend run dev
```

Vite serves the frontend on port 5173 and proxies `/health` and `/api` to the
backend on port 8000.

Validate the frontend:

```bash
npm --prefix frontend run typecheck
npm --prefix frontend run build
```

The production bundle is written to `frontend/dist/` and is not committed.

## Running both services locally

Use two terminals from the repository root.

Terminal 1:

```bash
source .venv/bin/activate
python -m uvicorn models4pt.app:app --reload
```

Terminal 2:

```bash
npm --prefix frontend run dev
```

Open `http://localhost:5173`. The page should report a successful backend
health response.

## Docker

The Docker image currently packages the backend only:

```bash
docker build -t models4pt-backend .
docker run --rm -p 8000:8000 models4pt-backend
```

For backend development with source mounting and reload:

```bash
docker compose up --build
```

The frontend remains a separate build and is not copied into the backend
image.

## Dependency updates

Dependency manifests and lockfiles serve different purposes:

- `pyproject.toml` declares the supported Python dependency ranges.
- `requirements.lock` records the resolved production dependency set used by
  the backend container.
- `requirements-dev.lock` records a reproducible resolved Python development
  environment.
- `frontend/package.json` declares frontend dependency ranges.
- `frontend/package-lock.json` records the exact frontend dependency tree.

When Python dependencies change, regenerate the development lock with Python
3.11 and `pip-tools`:

```bash
python -m pip install pip-tools
python -m piptools compile --strip-extras --output-file requirements.lock pyproject.toml
python -m piptools compile --allow-unsafe --strip-extras --extra dev --output-file requirements-dev.lock pyproject.toml
```

When frontend dependencies change, update and validate the npm lockfile:

```bash
npm --prefix frontend install
npm --prefix frontend run typecheck
npm --prefix frontend run build
```

Commit a manifest and its corresponding lockfile together.

## Continuous integration

The GitHub Actions workflow runs for pushes and pull requests targeting
`master`. It performs:

- backend tests on Python 3.11 and 3.12 using `requirements-dev.lock`
- frontend installation with `npm ci`
- frontend TypeScript checking
- frontend production build

## Current architecture

The backend is intentionally separated into small experiments:

- `domain.py` defines the initial scientific objects.
- `extraction.py` is a deterministic mock candidate extractor. It is not a
  production NLP or LLM implementation.
- `translation.py` tests the boundary between extracted language, ontology
  resolution, evidence, and a proposed causal claim.
- `app.py` currently exposes health endpoints only.

The current dataclasses are exploratory domain objects, not persistence or API
schemas. Future database and API models should preserve the scientific
distinctions without requiring these exact implementation types to become
permanent.

## Before opening a pull request

Run all available local checks:

```bash
python -m pytest -q
npm --prefix frontend run typecheck
npm --prefix frontend run build
```

Changes to scientific representations should also be checked against:

- `doc/project-foundation/FOUNDATIONAL_PRINCIPLES.md`
- `doc/project-foundation/SYSTEM BOUNDARIES.md`
