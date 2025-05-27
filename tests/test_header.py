import allure
from pages.header import Header
from pages.home_page import HomePage



class TestHeaderRedirect:
    @allure.title("Проверка открытия Яндекс Дзена в новой вкладке по клику на логотип Яндекса")
    def test_redirect_by_yandex_logo(self, driver_main_page):
        header = Header(driver_main_page)
        header.click_yandex_logo()
        header.switch_the_last_open_page() 
        header.check_yandex_dzen_opened()
        current_url = driver_main_page.current_url
        assert "dzen.ru" in current_url, f"Редирект не сработал. Текущий URL: {current_url}"
        
    @allure.title('Проверка редиркета на основную страницу при нажатие на логотип Самокат')
    def test_check_redirect_on_main_page(self, driver_order_page):
        header = Header(driver_order_page) 
        home_page_redirect = HomePage(driver_order_page) 
        header.click_scooter_logo()  
        home_page_redirect.scroll_to_down()
        home_page_redirect.click_to_question(0)
        faq = home_page_redirect.get_answer_text(0)
        assert '400 рублей' in faq