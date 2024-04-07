import pytest
import time
from selectors import Selectors
from conftest import is_roman


def level_result(game, level):
    time.sleep(1)
    return "checkmark.svg" in game.query_selector(level).inner_html()


PASSWORD = []


def test_001_min_length(game, password_level_01):
    PASSWORD.append(password_level_01)
    game.query_selector(Selectors.password_field).fill(''.join(PASSWORD))
    assert level_result(game, Selectors.level_01)


def test_002_number(game, password_level_02):
    PASSWORD.append(password_level_02)
    game.query_selector(Selectors.password_field).fill(''.join(PASSWORD))
    assert level_result(game, Selectors.level_02)


def test_003_uppercase(game, password_level_03):
    PASSWORD.append(password_level_03)
    game.query_selector(Selectors.password_field).fill(''.join(PASSWORD))
    assert level_result(game, Selectors.level_03)


def test_004_special_char(game, password_level_04):
    PASSWORD.append(password_level_04)
    game.query_selector(Selectors.password_field).fill(''.join(PASSWORD))
    assert level_result(game, Selectors.level_04)


@pytest.mark.parametrize("password_level_05", [PASSWORD], indirect=True)
def test_005_digits_sum(game, password_level_05):
    PASSWORD.append(password_level_05)
    game.query_selector(Selectors.password_field).fill(''.join(PASSWORD))
    assert level_result(game, Selectors.level_05)


def test_006_month(game, password_level_06):
    PASSWORD.append(password_level_06)
    game.query_selector(Selectors.password_field).fill(''.join(PASSWORD))
    assert level_result(game, Selectors.level_06)


def test_007_roman(game, password_level_07):
    PASSWORD.append(password_level_07)
    game.query_selector(Selectors.password_field).fill(''.join(PASSWORD))
    assert level_result(game, Selectors.level_07)


def test_008_sponsors(game, password_level_08):
    PASSWORD.append(password_level_08)
    game.query_selector(Selectors.password_field).fill(''.join(PASSWORD))
    assert level_result(game, Selectors.level_08)


@pytest.mark.parametrize("password_level_09", [PASSWORD], indirect=True)
def test_009_roman35(game, password_level_09):
    PASSWORD = password_level_09
    game.query_selector(Selectors.password_field).fill(''.join(PASSWORD))
    assert level_result(game, Selectors.level_09)


def test_010_captcha(game, password_level_10):
    PASSWORD.append(password_level_10)
    game.query_selector(Selectors.password_field).fill(''.join(PASSWORD))
    assert level_result(game, Selectors.level_10)
    digits_sum = roman_multiply = True
    for symbol in password_level_10:
        if symbol.isdigit() and 1 <= int(symbol) <= 9:
            digits_sum = False
        if is_roman(symbol):
            roman_multiply = False
    assert level_result(game, Selectors.level_05) == digits_sum
    assert level_result(game, Selectors.level_09) == roman_multiply


@pytest.mark.parametrize("captcha_clean", [PASSWORD], indirect=True)
def test_010_captcha_clean(game, captcha_clean):
    PASSWORD = captcha_clean
    game.query_selector(Selectors.password_field).fill(''.join(PASSWORD))


def test_011_wordle(game, password_level_11):
    PASSWORD.append(password_level_11)
    game.query_selector(Selectors.password_field).fill(''.join(PASSWORD))
    assert level_result(game, Selectors.level_11)
