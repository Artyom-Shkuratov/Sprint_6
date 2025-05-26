import allure
from pages.base_page import BasePage
from locators.home_page_locators import (
    QUESTION_LOCATOR_TEMPLATE,
    ANSWER_LOCATOR_TEMPLATE,
    SCROLL_LOCATOR
)
from data import main_page_url as url


class HomePage(BasePage):

    def click_to_question(self, num):
        question_locator = self.format_locator(QUESTION_LOCATOR_TEMPLATE, num)
        question_text = self.get_text_from_element(question_locator)
        with allure.step(f"Кликаем на вопрос: «{question_text}»"):
            self.click_on_element(question_locator)

    def get_answer_text(self, num):
        answer_locator = self.format_locator(ANSWER_LOCATOR_TEMPLATE, num)
        answer_text = self.get_text_from_element(answer_locator)
        with allure.step(f"Получаем текст ответа: «{answer_text}»"):
            return answer_text

    @allure.step("Прокручиваем страницу до секции FAQ")
    def scroll_to_down(self):
        element = self.find_element_with_wait(SCROLL_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @staticmethod
    def format_locator(locator_template, num):
        by, pattern = locator_template
        return by, pattern.format(num)