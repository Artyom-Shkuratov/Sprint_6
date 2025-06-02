import allure
import pytest
from data import *
from pages.home_page import HomePage

class TestMainPage:
    @allure.title('Главная страница: раздел FAQ')
    @allure.description('Проверяем, что для каждого вопроса отображается правильный ответ')

    @pytest.mark.parametrize('num', range(8))
    def test_click_question_show_correct_answer(self, driver_main_page, num):
        main_page = HomePage(driver_main_page)
        main_page.scroll_to_down()
        main_page.click_to_question(num)
        text = main_page.get_answer_text(num)
        assert text == faq_answers_text[num]