import sqlite3
from pathlib import Path
from werkzeug.security import generate_password_hash

# Database file path
DB_PATH = Path(__file__).parent.parent / "data" / "expenses.db"


def get_db():
    """
    Returns a SQLite connection with row_factory and foreign keys enabled.
    """
    # Ensure data directory exists
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row  # Enable dict-like row access

    # Enable foreign key constraints
    conn.execute("PRAGMA foreign_keys = ON")

    return conn


def init_db():
    """
    Creates all tables using CREATE TABLE IF NOT EXISTS.
    """
    conn = get_db()
    cursor = conn.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Expenses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()


def seed_db():
    """
    Inserts sample data for development.
    """
    conn = get_db()
    cursor = conn.cursor()

    # Check if data already exists
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] > 0:
        conn.close()
        return  # Already seeded

    # Sample user (password hashed with werkzeug)
    demo_password_hash = generate_password_hash("demo123")
    cursor.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
        ("Demo User", "demo@spendly.com", demo_password_hash)
    )

    # Sample expenses (user_id=1 for Demo User)
    # 8 expenses across all 7 categories: Food, Transport, Bills, Health, Entertainment, Shopping, Other
    sample_expenses = [
        (1, 250.00, "Food", "2026-04-01", "Grocery shopping"),
        (1, 50.00, "Transport", "2026-04-03", "Bus pass"),
        (1, 3500.00, "Bills", "2026-04-05", "Electricity bill"),
        (1, 1200.00, "Health", "2026-04-07", "Doctor visit"),
        (1, 800.00, "Entertainment", "2026-04-09", "Movie tickets"),
        (1, 1800.00, "Shopping", "2026-04-11", "New shirt"),
        (1, 500.00, "Other", "2026-04-13", "Miscellaneous"),
        (1, 180.00, "Food", "2026-04-15", "Restaurant lunch"),
    ]

    cursor.executemany(
        "INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)",
        sample_expenses
    )

    conn.commit()
    conn.close()
