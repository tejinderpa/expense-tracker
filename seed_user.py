"""
Seed a realistic random Indian user into the database.
"""
import random
from datetime import datetime
from werkzeug.security import generate_password_hash
from database.db import get_db


# Indian names - regional diversity
INDIAN_FIRST_NAMES = [
    # North Indian
    "Rahul", "Amit", "Priya", "Neha", "Rajesh", "Pooja", "Suresh", "Anita",
    "Vikram", "Deepika", "Arjun", "Kavita", "Manish", "Ritu", "Karan", "Sneha",
    # South Indian
    "Arvind", "Lakshmi", "Krishnan", "Meera", "Venkat", "Divya", "Ramesh", "Janaki",
    "Murthy", "Padma", "Sridhar", "Revathi", "Bala", "Kamala", "Ganesh", "Theresa",
    # East Indian
    "Sourav", "Rani", "Debashish", "Mamata", "Anirban", "Srija", "Prosenjit", "Koel",
    "Rituparna", "Saswata", "Parambrata", "Nusrat", "Dev", "Srabanti", "Jeet", "Mimi",
    # West Indian
    "Sameer", "Prajakta", "Siddharth", "Mrunmayee", "Sachin", "Priyanka", "Ajinkya",
    "Sonali", "Ram", "Laxman", "Seema", "Dinesh", "Usha", "Pradeep", "Meenakshi", "Ashok"
]

INDIAN_LAST_NAMES = [
    # Common North Indian
    "Sharma", "Verma", "Gupta", "Agarwal", "Singh", "Kumar", "Yadav", "Chauhan",
    "Malik", "Kapoor", "Khanna", "Bhatia", "Sethi", "Oberoi", "Nayar", "Chopra",
    # Common South Indian
    "Iyer", "Iyengar", "Menon", "Nair", "Reddy", "Rao", "Pillai", "Chettiar",
    "Gounder", "Mudaliar", "Hegde", "Bhat", "Kamath", "Shenoy", "Prabhu", "Rai",
    # Common East Indian
    "Banerjee", "Chatterjee", "Ganguly", "Mukherjee", "Das", "Dutta", "Roy",
    "Sengupta", "Bose", "Sarkar", "Ghosh", "Pal", "Jana", "Mondal",
    # Common West Indian
    "Patil", "Deshmukh", "Jadhav", "Pawar", "Shinde", "Bhosale", "More", "Thakur",
    "Kulkarni", "Deshpande", "Joshi", "Bhatt", "Modi", "Patel", "Shah", "Mehta"
]

EMAIL_DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "rediffmail.com"]


def generate_indian_name():
    """Generate a random Indian name."""
    first_name = random.choice(INDIAN_FIRST_NAMES)
    last_name = random.choice(INDIAN_LAST_NAMES)
    return f"{first_name} {last_name}"


def generate_email(first_name, last_name):
    """Generate an email from name with random suffix."""
    # Use lowercase with dot separator
    name_part = f"{first_name.lower()}.{last_name.lower()}"
    suffix = random.randint(10, 999)
    domain = random.choice(EMAIL_DOMAINS)
    return f"{name_part}{suffix}@{domain}"


def email_exists(email):
    """Check if email already exists in the database."""
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result is not None


def generate_unique_user():
    """Generate a user with a unique email."""
    max_attempts = 100
    for _ in range(max_attempts):
        name = generate_indian_name()
        first_name, last_name = name.split(" ", 1)
        email = generate_email(first_name, last_name)

        if not email_exists(email):
            return name, email

    # Fallback: add timestamp to ensure uniqueness
    name = generate_indian_name()
    first_name, last_name = name.split(" ", 1)
    suffix = datetime.now().strftime("%Y%m%d%H%M%S")
    domain = random.choice(EMAIL_DOMAINS)
    email = f"{first_name.lower()}.{last_name.lower()}{suffix}@{domain}"
    return name, email


def seed_user():
    """Create and insert a unique Indian user."""
    name, email = generate_unique_user()
    password = "password123"
    password_hash = generate_password_hash(password)

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
        (name, email, password_hash)
    )

    user_id = cursor.lastrowid
    conn.commit()
    conn.close()

    print(f"User created successfully!")
    print(f"  User ID: {user_id}")
    print(f"  Name: {name}")
    print(f"  Email: {email}")


if __name__ == "__main__":
    seed_user()
