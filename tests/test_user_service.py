import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from app.user_service import (
    calculate_discount,
    get_average_score,
    get_usernames,
    get_config_value,
    get_user,
)

def test_get_user_found():
    users = [{"id": 1, "username": "alice"}, {"id": 2, "username": "bob"}]
    assert get_user(users, 1)["username"] == "alice"

def test_get_user_not_found():
    users = [{"id": 1, "username": "alice"}]
    assert get_user(users, 99) is None

def test_discount_basic():
    assert calculate_discount(100, 10) == 90.0

def test_discount_invalid_raises():
    with pytest.raises(ValueError):
        calculate_discount(100, 150)

def test_average_score_basic():
    assert get_average_score(300, 3) == 100.0

def test_average_score_zero_students_raises():
    with pytest.raises(ValueError):
        get_average_score(300, 0)

def test_get_usernames():
    users = [{"username": "alice"}, {"username": "bob"}]
    assert get_usernames(users) == ["ALICE", "BOB"]

def test_config_value_found():
    config = {"host": "localhost"}
    assert get_config_value(config, "host") == "localhost"

def test_config_value_missing_returns_default():
    config = {"host": "localhost"}
    assert get_config_value(config, "missing_key") is None
