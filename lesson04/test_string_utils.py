import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("cat", "Cat"),
    ("good bye", "Good bye"),
    ("рыжик", "Рыжик"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123", "123"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" Cat", "Cat"),
    ("  Good bye", "Good bye"),
    (" Рыжик ", "Рыжик "),
    (" 123", "123")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("abc ", "abc "),
    ("", ""),
    ("   ", "   "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Cat", "C", True),
    ("Good bye", "S", False),
    ("Рыжик ", "ло", False),
    ("123", "2", True)
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Sun", "Sun", True),
    ("", "", False),
    ("   ", "   ", True),
    (123, 12, True)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Cat", "C", "at"),
    ("Good bye", "bye", "Good "),
    ("Рыжик", "ыжик", "Р"),
    ("123", "2", "13")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Sun", "Sun", ""),
    ("", "", ""),
    ("   ", "   ", ""),
    ("Cat", "m", "Cat"),
    (123, 1, 23),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
