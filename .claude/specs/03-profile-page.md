# Spec: Profile Page Design

## Overview

Implement the user profile page that displays account information and provides a dashboard overview. This feature builds on the registration system (Step 02) and gives users a view of their account details plus summary statistics of their expenses. The profile page serves as the main dashboard users will see after logging in.

## Depends on

- Step 01: Database Setup (users and expenses tables)
- Step 02: Registration (user creation with hashed passwords)

## Routes

- **GET /profile** — Displays user profile page — logged-in users only
  - Shows user's name, email, and account creation date
  - Displays summary statistics (total expenses, this month's spending)
  - Shows recent expenses list
  - Redirects to /login if not authenticated

## Database changes

- No new tables or columns required
- Uses existing `users` and `expenses` tables from Step 01

## Templates

- **Create:** `templates/profile.html`
  - Profile card with user avatar placeholder, name, email, member since
  - Stats section with summary cards (total spent, this month, transaction count)
  - Recent expenses table listing last 5-10 expenses
  - Edit profile button (placeholder for future step)

## Files to change

| File | Description |
|------|-------------|
| `app.py` | Implement GET /profile route with user data lookup and stats calculation |
| `database/db.py` | Add `get_user_by_id(user_id)`, `get_user_expense_stats(user_id)`, `get_recent_expenses(user_id, limit)` functions |
| `static/css/style.css` | Add profile-specific styles (profile card, stats grid, expense table) |

## Files to create

| File | Description |
|------|-------------|
| `templates/profile.html` | Profile page template extending base.html |

## New dependencies

- No new dependencies — use existing Flask and SQLite functionality

## Rules for implementation

- No SQLAlchemy or ORMs — use parameterized SQLite queries only
- All templates extend `base.html`
- Use CSS variables — never hardcode hex values
- Profile page must be protected (redirect to /login if not authenticated)
- Use Flask's `session` for authentication state (prepare for Step 03)
- Display currency in INR (₹) format per user preference
- Stats calculations must handle edge cases (user with no expenses)
- All monetary values formatted to 2 decimal places

## Definition of done

- [ ] Profile page accessible at /profile route
- [ ] User's name, email, and member since date displayed
- [ ] Stats section shows total expenses count and sum
- [ ] Recent expenses table shows last 5-10 expenses with amount, category, date, description
- [ ] Page renders with navbar and footer from base.html
- [ ] Profile-specific CSS styles added to style.css
- [ ] All monetary values formatted as INR (₹) with 2 decimal places
- [ ] Edge case handled: user with zero expenses shows "No expenses yet"
- [ ] Template uses existing CSS variables for theming
