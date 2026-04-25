# Spec: Registration

## Overview

Implement user registration functionality for the Spendly expense tracker. This feature allows new users to create an account by providing their name, email, and password. The registration form already exists in `templates/register.html`; this step adds the backend logic to handle form submission, validate input, hash passwords, and store new users in the database.

## Depends on

- Step 01: Database Setup (users table with username, email, password_hash columns)

## Routes

- **POST /register** — Handles registration form submission — public
  - Validates input (name, email, password)
  - Checks if email already exists
  - Hashes password and inserts new user
  - Redirects to /login on success
  - Re-renders registration form with error message on failure

## Database changes

- No new tables or columns required
- Uses existing `users` table from Step 01

## Templates

- **Modify:** `templates/register.html`
  - Add flash message display for success/error feedback
  - Ensure form fields match backend expectations (name, email, password)

## Files to change

| File | Description |
|------|-------------|
| `app.py` | Add POST handler for /register route with validation, password hashing, and user creation |
| `database/db.py` | Add `create_user(username, email, password)` function |

## Files to create

- None

## New dependencies

- No new dependencies — use existing `werkzeug.security` for password hashing

## Rules for implementation

- No SQLAlchemy or ORMs — use parameterized SQLite queries only
- Passwords must be hashed with `werkzeug.security.generate_password_hash()`
- Validate password length (minimum 8 characters)
- Validate email format (basic check for @ symbol)
- Validate name is not empty
- Check for duplicate email before inserting
- Use Flask's `flash()` for user feedback
- Redirect to `/login` after successful registration
- All templates extend `base.html`
- Use CSS variables — never hardcode hex values

## Definition of done

- [ ] User can submit registration form with name, email, and password
- [ ] Passwords less than 8 characters are rejected with error message
- [ ] Duplicate email addresses are rejected with error message
- [ ] Empty name is rejected with error message
- [ ] Successful registration creates user in database with hashed password
- [ ] User is redirected to /login page after successful registration
- [ ] Error messages are displayed on the registration form
- [ ] Registration page renders correctly with navbar and footer
