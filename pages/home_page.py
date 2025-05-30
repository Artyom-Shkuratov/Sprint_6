import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators import home_page_locators as home_locators
from locators.home_page_locators import (
    QUESTION_LOCATOR_TEMPLATE,
    ANSWER_LOCATOR_TEMPLATE,
    SCROLL_LOCATOR,
    IMG_SAMOCAT
)


class HomePage(BasePage):
    @allure.step("Кликаем по вопросу")
    def click_to_question(self, num):
        question_locator = self.format_locator(QUESTION_LOCATOR_TEMPLATE, num)
        element = self.find_element_with_wait(question_locator)
        self.scroll_to_element_center(element)
        self.wait_until_clickable(question_locator).click()

    @allure.step("Получаем текст ответа на вопрос")
    def get_answer_text(self, num):
        answer_locator = self.format_locator(ANSWER_LOCATOR_TEMPLATE, num)
        answer_text = self.get_text_from_element(answer_locator)
        with allure.step(f"Получаем текст ответа: «{answer_text}»"):
            return answer_text

    @allure.step("Прокручиваем страницу до секции FAQ")
    def scroll_to_down(self):
        element = self.find_element_with_wait(SCROLL_LOCATOR)
        self.scroll_to_element_center(element)
        
    @allure.step("Ожидаем загрузку главной страницы")
    def wait_for_homepage_loaded(self):
        self.find_element_with_wait(home_locators.SCROLL_LOCATOR)

        
        
    @allure.step("Ждём, пока загрузится картинка самоката")
    def wait_for_img_samocat(self):
        self.scroll_to_down()
        return self.find_element_with_wait(home_locators.IMG_SAMOCAT)
            
        
    @staticmethod
    def format_locator(locator_template, num):
        by, pattern = locator_template
        return by, pattern.format(num)