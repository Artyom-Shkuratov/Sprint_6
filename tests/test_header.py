import allure
from locators import home_page_locators as home_locators, order_page_locators as order_locators
from pages.header import Header
from pages.home_page import HomePage
from pages.order_page import OrderPage



class TestHeaderRedirect:
    @allure.title("Проверка открытия Яндекс Дзена в новой вкладке по клику на логотип Яндекса")
    def test_redirect_by_yandex_logo(self, driver_main_page):
        header = Header(driver_main_page)
        header.click_yandex_logo()
        header.switch_the_last_open_page()
        header.check_yandex_dzen_opened()
        current_url = header.get_current_url()
        assert "dzen.ru" in current_url, f"Редирект не сработал. Текущий URL: {current_url}"
        
    @allure.title('Проверка редиректа на главную страницу при нажатии на логотип Самокат')
    def test_check_redirect_on_main_page(self, driver_main_page):
        header = Header(driver_main_page)
        home_page = HomePage(driver_main_page)
        order_form = OrderPage(driver_main_page)
        home_page.click_on_element(home_locators.CLOSE_COOCKIE_WINDOW)
        order_form.open_order_form(order_locators.ORDER_BUTTON_HEADER)
        header.click_scooter_logo()
        home_page.wait_for_img_samocat()
        img_element = home_page.wait_for_img_samocat()
        assert img_element.is_displayed(), "Изображение самоката не отображается на главной странице"