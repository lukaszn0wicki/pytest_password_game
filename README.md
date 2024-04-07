# pytest_password_game
Solve first levels of https://neal.fun/password-game/

Simple test scenario for PasswordGame, using pytest and playwright.


## Initial installation:

```python3 -m pip install -r requirements.txt```

```playwright install```

## Usage:
Console: ```pytest -sv test_password_game.py```
Executing in Jenkins pipeline can be done using ```password_game.sh```


## How does it work?


The algorithm in each test examines levels of the game, randomly selecting and appending the next part of the password in such a way that it meets the criteria of the new level. Some levels may introduce a solution that disrupts previous achievements (for example, a random Roman numeral in level 7 may prevent a solution in level 9), so when necessary, tests modify previously generated parts of the password.

For level 10 (captcha), the test initially checks the code generated for the first time, but later refreshes it until it obtains a code without numbers or Roman numerals, in order to avoid having to modify previous values.


