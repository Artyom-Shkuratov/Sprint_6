import allure
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import header_locators as locators
from selenium.webdriver.support.ui import WebDriverWait
from locators import home_page_locators as home_locators


class Header(BasePage):
    
    @allure.step('Нажимаем на лого Яндекса в шапке сайта')
    def click_yandex_logo(self):
        self.click_on_element(locators.LOGO_YANDEX)
        
    @allure.step('Нажимаем на лого Самокат в шапке сайта')
    def click_scooter_logo(self):
        self.click_on_element(locators.LOGO_SAMOKAT)
        self.find_element_with_wait(home_locators.SCROLL_LOCATOR)
        
    @allure.step("Переходим на  открытую вкладку")
    def switch_the_last_open_page(self):
        self.switch_to_last_tab()
        
    @allure.step("Проверяем, что мы на странице яндекса")
    def check_yandex_dzen_opened(self):
        try:
            self.find_element_with_wait(locators.REDIRECT_YANDEX)
        except TimeoutException:
            raise AssertionError("Элемент Яндекса не найден — редирект не сработал")