---
description: Create a single dummy user in the database

allowed-tools: Read, Bash(python3:*)
---

1. Read `database/db.py` to understand the `users` table schema and the `get_db()` helper function.

2. Write and run a Python script that:

   **Generates a realistic random Indian user:**
   - **Name:** A realistic Indian first name + last name (draw from common names across North/South/East/West regions)
   - **Email:** Derived from the name with a random 2-3 digit suffix (e.g., `rahul.sharma91@gmail.com`)
   - **Password:** `"password123"` hashed using Werkzeug's `generate_password_hash`
   - **created_at:** Current datetime

   **Ensures uniqueness:**
   - Check if the generated email already exists in the `users` table
   - If it exists, regenerate the user details until a unique email is produced

   **Inserts the user:**
   - Use the same `get_db()` pattern found in `db.py`
   - Insert into the `users` table

3. Print confirmation with:
   - User ID
   - Name
   - Email