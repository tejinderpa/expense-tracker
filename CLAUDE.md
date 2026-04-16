

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Spendly is a personal expense tracking Flask application. It's designed as an educational project with incremental feature development (Steps 1-9+).

## Technology Stack

- **Backend**: Flask 3.1.3, Werkzeug 3.1.6
- **Database**: SQLite (via `database/` package)
- **Frontend**: Vanilla JavaScript, Jinja2 templates, CSS custom properties
- **Testing**: pytest 8.3.5, pytest-flask 1.3.0

## Development Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Flask development server
python app.py
# Server runs on http://localhost:5001 (configured in app.py)

# Run tests
pytest

# Run a single test file
pytest tests/test_file.py

# Run a specific test
pytest tests/test_file.py::test_function_name
```

## Project Architecture

### Application Structure

```
app.py              # Main Flask application with routes
database/           # Database module (students implement in Step 1)
  __init__.py
  db.py             # get_db(), init_db(), seed_db() (placeholder comments)
static/
  css/style.css     # Single stylesheet with CSS custom properties
  js/main.js        # Placeholder for future JavaScript features
templates/
  base.html         # Base template with navbar, footer, blocks
  landing.html      # Homepage with hero, features, video modal
  login.html        # Authentication form
  register.html     # Registration form
  terms.html        # Legal page
  privacy.html      # Legal page
```

### Routing Structure

Current routes in `app.py`:
- `/` — Landing page
- `/login`, `/register` — Authentication (forms ready, logic pending)
- `/logout` — Placeholder ("coming in Step 3")
- `/profile` — Placeholder ("coming in Step 4")
- `/expenses/add`, `/expenses/<id>/edit`, `/expenses/<id>/delete` — Placeholders (Steps 7-9)
- `/terms`, `/privacy` — Static legal pages (implemented)

### Database Module (`database/db.py`)

Currently contains placeholder comments. Expected functions:
- `get_db()` — Returns SQLite connection with `row_factory=sqlite3.Row` and foreign keys
- `init_db()` — Creates tables using `CREATE TABLE IF NOT EXISTS`
- `seed_db()` — Inserts sample data for development

### CSS Architecture

Uses CSS custom properties for theming in `:root`:
- Colors: `--ink`, `--paper`, `--accent`, `--accent-2`, `--danger`
- Fonts: `--font-display` (DM Serif Display), `--font-body` (DM Sans)
- Layout: `--max-width: 1200px`, `--auth-width: 440px`

Key component classes:
- `.navbar`, `.nav-inner` — Sticky header with brand + links
- `.hero` — Two-column grid (content + mock card visual)
- `.auth-section`, `.auth-card` — Centered forms
- `.modal` — Video modal with 16:9 aspect ratio container

### Template Conventions

All templates extend `base.html`:
```jinja
{% block title %}{% endblock %}
{% block head %}{% endblock %}
{% block content %}{% endblock %}
{% block scripts %}{% endblock %}
```

Footer links: `/terms`, `/privacy`

### Modal Implementation Pattern

The video modal in `landing.html` uses vanilla JS:
- Open: Add `.modal-open` class, set `body.style.overflow = 'hidden'`
- Close: Remove class, reset overflow, stop video by resetting iframe `src`
- Triggers: Button click, X button, outside click, Escape key
