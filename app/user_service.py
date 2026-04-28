"""
User Service — handles basic user operations for the demo app.
This is the CLEAN version. No bugs here.
"""


def get_user(users: list, user_id: int):
    """Safely fetch a user by their ID from a list."""
    for user in users:
        if user.get("id") == user_id:
            return user
    return None


def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate the final price after applying a discount."""
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount must be between 0 and 100")
    if price < 0:
        raise ValueError("Price cannot be negative")
    discount = price * (discount_percent / 100)
    return round(price - discount, 2)


def get_average_score(total_score: float, num_students: int) -> float:
    """Calculate the average score per student."""
    if num_students == 0:
        raise ValueError("Cannot divide by zero students")
    return round(total_score / num_students, 2)


def get_usernames(users: list) -> list:
    """Return a list of all usernames in uppercase."""
    result = []
    for user in users:
        result.append(user["username"].upper())
    return result


def get_config_value(config: dict, key: str, default=None):
    """Safely retrieve a value from config, returning default if missing."""
    return config.get(key, default)