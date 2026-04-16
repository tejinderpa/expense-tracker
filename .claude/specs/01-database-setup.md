# Database Setup Specification

## 1. Overview

Replace the stub in `database/db.py` with a working SQLite implementation. This step establishes the data layer foundation for the Spendly application. All future features (authentication, profile, expense tracking) depend on this being correctly implemented.

## 2. Dependencies

- **Nothing** — this is the first step.

## 3. Routes

- No new routes required
- Existing placeholder routes in `app.py` remain unchanged

## 4. Database Schema

### A. `users` Table

| Column        | Type    | Constraints                           |
|---------------|---------|---------------------------------------|
| id            | INTEGER | Primary key, autoincrement            |
| username      | TEXT    | Unique, not null                      |
| email         | TEXT    | Unique, not null                      |
| password_hash | TEXT    | Not null                              |
| created_at    | TEXT    | Default `datetime('now')`             |

### B. `expenses` Table

| Column      | Type    | Constraints                           |
|-------------|---------|---------------------------------------|
| id          | INTEGER | Primary key, autoincrement            |
| user_id     | INTEGER | Foreign key → `users.id`, not null    |
| amount      | REAL    | Not null                              |
| category    | TEXT    | Not null                              |
| date        | TEXT    | Not null (YYYY-MM-DD format)          |
| description | TEXT    | Nullable                              |
| created_at  | TEXT    | Default `datetime('now')`             |

## 5. Functions to Implement (`database/db.py`)

### A. `get_db()`

- Opens connection to `spendly.db` (or `expense_tracker.db`) in project root
- Sets:
  - `row_factory = sqlite3.Row`
  - `PRAGMA foreign_keys = ON`
- Returns the connection

### B. `init_db()`

- Creates both tables using `CREATE TABLE IF NOT EXISTS`
- Safe to call multiple times
- Ensures schema is ready before app usage

### C. `seed_db()`

- Checks if `users` table already contains data
- If yes → return early (no duplication)
- Inserts one demo user:
  - **name:** Demo User
  - **email:** demo@spendly.com
  - **password:** demo123 (hashed using werkzeug)
- Inserts 8 sample expenses:
  - All linked to demo user
  - Cover multiple categories
  - Dates spread across current month
  - At least one expense per category

## 6. Changes to `app.py`

**Import:**
- `get_db`
- `init_db`
- `seed_db`

**Startup:**
- Call `init_db()` and `seed_db()` inside `app.app_context()` on startup
- Ensure DB is ready before routes are used

## 7. Files to Change

| File               | Description                          |
|--------------------|--------------------------------------|
| `database/db.py`   | Implement all functions              |
| `app.py`           | Add imports and startup calls        |

## 8. Files to Create

- None

## 9. Dependencies

- No new pip packages required
- Use:
  - `sqlite3` (standard library)
  - `werkzeug.security` (already installed)

## 10. Categories (Fixed List)

Use exactly these values:

1. Food
2. Transport
3. Bills
4. Health
5. Entertainment
6. Shopping
7. Other

## 11. Implementation Rules

- No ORMs (no SQLAlchemy)
- Use parameterized queries only
- Never use string formatting in SQL
- Enable `PRAGMA foreign_keys = ON` on every connection
- Store `amount` as REAL (float), not INTEGER
- Hash passwords using `werkzeug.security.generate_password_hash()`
- `seed_db()` must prevent duplicate inserts
- Dates must follow `YYYY-MM-DD` format consistently

## 12. Expected Behavior

| Function    | Expected Outcome                                      |
|-------------|-------------------------------------------------------|
| `get_db()`  | Working connection with dict-like row access, FK on  |
| `init_db()` | Creates tables safely, no failure on repeated runs   |
| `seed_db()` | Inserts demo data once, no duplication               |

**Database enforces:**
- Unique email constraint
- Valid foreign key relationships

## 13. Error Handling Expectations

| Scenario                              | Expected Result                        |
|---------------------------------------|----------------------------------------|
| Inserting duplicate email             | Fail (UNIQUE constraint)               |
| Inserting expense with invalid user_id| Fail (foreign key constraint)          |
| Invalid queries                       | Raise clear errors for debugging       |

## 14. Definition of Done

- [ ] Database file is created on app startup
- [ ] Both tables exist with correct schema and constraints
- [ ] Demo user exists with hashed password
- [ ] 8 sample expenses exist across categories
- [ ] No duplicate seed data on repeated runs
- [ ] App starts without errors
- [ ] Foreign key enforcement works
- [ ] All queries use parameterized SQL
