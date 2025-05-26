from selenium.webdriver.common.by import By

#кнопка заказать в шапке сайта и внизу страницы
ORDER_BUTTON_HEADER = [By.XPATH, './/div[contains(@class, "Header_Nav")]/button[text()="Заказать"]']
ORDER_DOWN_ON_MAIN_PAGE = [By.XPATH, './/div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]']

#селекторы полей для формы заказа
NAME_INPUT =[By.XPATH, './/input[contains(@placeholder, "Имя")]']
SURNAME_INPUT = [By.XPATH, './/input[contains(@placeholder, "Фамилия")]']
ADDRESS_INPUT = [By.XPATH, './/input[contains(@placeholder, "Адрес")]']
METRO_STATION = [By.XPATH, './/input[contains(@placeholder, "Станция метро")]']
SELECT_METRO_STATION = [By.XPATH, './/div[@class="Order_Text__2broi" and text()="Лубянка"]']
PHONE_NUMBER_UNPUT = [By.XPATH, './/input[contains(@placeholder, "Телефон: на него позвонит курьер")]']

#кнопка далее под формой
NEXT_BUTTON = [By.XPATH, './/div[contains(@class, "Order_NextButton")]/button[text()="Далее"]']

#Локаторы для срока аренды
DELIVERY_DATE_INPUT = [By.XPATH, './/input[contains(@placeholder, "Когда привезти самокат")]']
RENTAL_PERIOD_DROPDOWN = [By.XPATH, './/div[contains(@class, "Dropdown-control") and .//div[text()="* Срок аренды"]]']
RENTAL_TIME_DROPDOWN = [By.XPATH, './/div[@class="Dropdown-menu"]//div[text()="{text}"]']

SELECT_COLOR = [By.ID, '{color}']

COMMNET_INPUT = [By.XPATH, './/input[contains(@placeholder, "Комментарий для курьера")]']

ORDER_BUTTON = [By.XPATH, './/div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]']

CONFIRM_BUTTON = [By.XPATH, './/button[text()="Да"]']

SUCCES_CREATE_ORDER = [By.XPATH, './/div[contains(@class, "Order_Text")]']