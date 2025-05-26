import allure
from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators import header_locators as locators



class Header(BasePage):
    
    @allure.step('Нажимаем на лого Яндекса в шапке сайта')
    def click_yandex_logo(self):
        self.click_on_element(locators.LOGO_YANDEX)
        
    @allure.step('Нажимаем на лого Самокат в шапке сайта')
    def click_scooter_logo(self):
        self.click_on_element(locators.LOGO_SAMOKAT)
        
    @allure.step("Переходим на  открытую вкладку")
    def switch_the_last_open_page(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
    @allure.step("Проверяем, что мы на странице яндекса")
    def check_yandex_dzen_opened(self):
        try:
            self.find_element_with_wait(locators.REDIRECT_YANDEX)
        except TimeoutException:
            raise AssertionError("Элемент Яндекса не найден — редирект не сработал")