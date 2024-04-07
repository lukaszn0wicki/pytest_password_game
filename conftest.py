import pytest
import requests
import random
import string
import time
from datetime import datetime
from playwright.sync_api import (sync_playwright)
from selectors import Selectors


def is_clean(captcha: str):
    for symbol in captcha:
        if symbol.isdigit() and 1 <= int(symbol) <= 9:
            return False
        if is_roman(symbol):
            return False
    return True


def is_roman(letter: str):
    return letter in ['I', 'V', 'X', 'L', 'C', 'D', 'M']


@pytest.fixture(scope="session")
def game():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://neal.fun/password-game/')
        cookie_accept = page.query_selector(Selectors.cookie_accept)
        cookie_accept.click()
        password_field = page.query_selector(Selectors.password_field)
        password_field.click()
        yield page
        browser.close()


@pytest.fixture(scope="module")
def password_level_01():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(5))


@pytest.fixture(scope="module")
def password_level_02():
    return str(random.randint(0, 9))


@pytest.fixture(scope="module")
def password_level_03():
    return random.choice(string.ascii_uppercase)


@pytest.fixture(scope="module")
def password_level_04():
    specials = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|',
                '\\', ';', ':', '\'', '"', ',', '.', '/', '<', '>', '?']
    return random.choice(specials)


@pytest.fixture(scope="module")
def password_level_05(request):
    digits = [int(request.param[1])]
    while missing := 25 - sum(digits):
        if missing >= 9:
            digits.append(random.randint(0, 9))
        else:
            digits.append(random.randint(0, missing))
    return ''.join(str(i) for i in digits[1:])


@pytest.fixture(scope="module")
def password_level_06():
    months = ['january', 'february', 'march', 'april', 'may', 'june',
              'july', 'august', 'september', 'october', 'november', 'december']
    return random.choice(months)


@pytest.fixture(scope="module")
def password_level_07():
    romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    return random.choice(romans)


@pytest.fixture(scope="module")
def password_level_08():
    sponsors = ['pepsi', 'starbucks', 'shell']
    return random.choice(sponsors)


@pytest.fixture(scope="module")
def password_level_09(request):
    password = request.param
    solutions = [['VII', 'V'],
                 ['V', 'VII'],
                 ['XXXV', ''],
                 ['', 'XXXV']]
    solution = random.choice(solutions)
    if is_roman(password[2]):
        password[2] = solution[0]
        password[6] = solution[1]
    else:
        password[6] = solution[0]
        password.append(solution[1])
    return password


@pytest.fixture(scope="module")
def password_level_10(game):
    captcha = game.query_selector(Selectors.captcha_img)
    captcha_img = captcha.get_attribute("src")
    return captcha_img.split("/")[-1].replace(".png", "")


@pytest.fixture(scope="module")
def captcha_clean(request, game):
    password = request.param
    new_captcha = password[-1]
    while not is_clean(new_captcha):
        refresh_captcha = game.query_selector(Selectors.new_captcha_btn)
        refresh_captcha.click()
        time.sleep(0.5)
        captcha = game.query_selector(Selectors.captcha_img)
        captcha_img = captcha.get_attribute("src")
        new_captcha = captcha_img.split("/")[-1].replace(".png", "")
    password[-1] = new_captcha
    return password


@pytest.fixture(scope="module")
def password_level_11():
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    resp = requests.get(f"https://www.nytimes.com/svc/wordle/v2/{year}-{month:02}-{day:02}.json")
    result = resp.json()["solution"]
    return result
