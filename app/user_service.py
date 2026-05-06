"""
User Service — handles basic user operations for the demo app.
WARNING: This version has intentional bugs for demo purposes.
This is the file you commit on the second push to trigger Claude.
"""

import sqlite3


def get_user(db_path: str, user_id: str):
    """Fetch a user by ID from the database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # BUG 1 (CRITICAL) — SQL Injection
    # user_id is pasted directly into the query string using an f-string.
    # An attacker can pass: user_id = "1 OR 1=1" and get ALL users back.
    # Fix: use parameterised queries → cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

    user = cursor.fetchone()
    conn.close()
    return user


def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate the final price after applying a discount."""

    # BUG 2 (HIGH) — No input validation
    # Nothing stops discount_percent from being 150 (paying us to take it)
    # or -10 (charging the customer more). Also no check for negative prices.
    # Fix: add guards → if not (0 <= discount_percent <= 100): raise ValueError(...)
    discount = price * (discount_percent / 100)
    return price - discount


def get_average_score(total_score: float, num_students: int) -> float:
    """Calculate the average score per student."""

    # BUG 3 (HIGH) — Division by zero
    # If num_students is 0 this crashes with ZeroDivisionError.
    # Fix: if num_students == 0: raise ValueError("No students")
    return total_score / num_students


def get_usernames(users: list) -> list:
    """Return a list of all usernames in uppercase."""
    result = []

    # BUG 4 (HIGH) — Off-by-one error
    # range(len(users) + 1) goes one index PAST the end of the list.
    # On the last iteration users[i] raises an IndexError.
    # Fix: range(len(users))  OR  just: for user in users
    for i in range(len(users) + 1):
        result.append(users[i]["username"].upper())
    return result


def get_config_value(config: dict, key: str):
    """Retrieve a value from config."""

    # BUG 5 (MEDIUM) — KeyError risk
    # If `key` doesn't exist in config this raises a KeyError and crashes.
    # Fix: return config.get(key, None)
    return config[key]