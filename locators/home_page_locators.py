from selenium.webdriver.common.by import By

# Вопрос 1
QUESTION_PRICE = [By.XPATH, ".//div[@class='accordion__button' and contains(text(), 'Сколько это стоит?')]"]
ANSWER_PRICE = [By.XPATH, ".//p[contains(text(), 'Сутки — 400 рублей.')]"]

# Вопрос 2
QUESTION_MULTIPLE_SCOOTERS = [By.XPATH, ".//div[@class='accordion__button' and contains(text(), 'Хочу сразу несколько самокатов!')]"]
ANSWER_MULTIPLE_SCOOTERS = [By.XPATH, ".//p[contains(text(), 'Пока что у нас так: один заказ — один самокат.')]"
]
# Вопрос 3
QUESTION_RENTAL_TIME = [By.XPATH, ".//div[@class='accordion__button' and contains(text(), 'Как рассчитывается время')]"]
ANSWER_RENTAL_TIME = [By.XPATH, ".//p[contains(text(), 'Допустим, вы оформляете заказ')]"]

# Вопрос 4
QUESTION_ORDER_TODAY = [By.XPATH, ".//div[@class='accordion__button' and contains(text(), 'Можно ли заказать самокат')]"]
ANSWER_ORDER_TODAY =[ By.XPATH, ".//p[contains(text(), 'Только начиная с завтрашнего дня.')]"]

# Вопрос 5
QUESTION_EXTEND_OR_RETURN = [By.XPATH, ".//div[@class='accordion__button' and contains(text(), 'продлить заказ или вернуть самокат раньше')]"]
ANSWER_EXTEND_OR_RETURN = [By.XPATH, ".//p[contains(text(), 'Пока что нет!')]"]

# Вопрос 6
QUESTION_CHARGING = [By.XPATH, ".//div[@class='accordion__button' and contains(text(), 'зарядку вместе с самокатом')]"]
ANSWER_CHARGING = [By.XPATH, ".//p[contains(text(), 'приезжает к вам с полной зарядкой')]"]

# Вопрос 7
QUESTION_CANCEL = [By.XPATH, ".//div[@class='accordion__button' and contains(text(), 'отменить заказ')]"]
ANSWER_CANCEL = [By.XPATH, ".//p[contains(text(), 'Да, пока самокат не привезли.')]"]

# Вопрос 8
QUESTION_OUTSIDE_MKAD = [By.XPATH, ".//div[@class='accordion__button' and contains(text(), 'МКАДом, привезёте?')]"]
ANSWER_OUTSIDE_MKAD = [By.XPATH, ".//p[contains(text(), 'И Москве, и Московской области.')]"
]
QUESTION_LOCATOR_TEMPLATE = [By.ID, "accordion__heading-{}"]
ANSWER_LOCATOR_TEMPLATE = [By.ID, "accordion__panel-{}"]
SCROLL_LOCATOR = [By.XPATH, ".//div[contains(@class, 'Home_FourPart__1uthg')]"]

IMG_SAMOCAT = (By.XPATH, './/img[@src="/assets/scooter.png" and @alt="Scooter blueprint"]')

CLOSE_COOCKIE_WINDOW = [By.ID, 'rcc-confirm-button']