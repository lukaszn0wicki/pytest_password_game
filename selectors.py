class Selectors:
    captcha_img = "#__layout > div > div > div.password-wrapper > div:nth-child(5) > div > div:nth-child(1) > div > " \
                  "div > div > div.captcha-wrapper > img.captcha-img"
    cookie_accept = "body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > " \
                    "div.fc-footer-buttons-container > div.fc-footer-buttons > " \
                    "button.fc-button.fc-cta-consent.fc-primary-button > p"
    new_captcha_btn = "img.captcha-refresh"
    password_field = "#__layout > div > div > div.password-wrapper > div.password-box > div.password-box-inner > " \
                     "div:nth-child(2) > div"
    level_01 = "div.min-length"
    level_02 = "div.number"
    level_03 = "div.uppercase"
    level_04 = "div.special"
    level_05 = "div.digits"
    level_06 = "div.month"
    level_07 = "div.roman"
    level_08 = "div.sponsors"
    level_09 = "div.roman-multiply"
    level_10 = "div.captcha"
    level_11 = "div.wordle"
