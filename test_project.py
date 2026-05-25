import pytest
from project import user_data


def test_user_data_starts_empty():

    user_data.clear()

    assert user_data == {}


def test_store_user_data():

    user_data["age"] = "18"
    user_data["height"] = "177"
    user_data["weight"] = "87"
    user_data["activity"] = "2"

    assert user_data["age"] == "18"
    assert user_data["height"] == "177"
    assert user_data["weight"] == "87"
    assert user_data["activity"] == "2"


def test_user_data_clear():

    user_data["test"] = "value"

    user_data.clear()

    assert user_data == {}