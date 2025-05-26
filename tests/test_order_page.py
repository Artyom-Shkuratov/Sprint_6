import allure
import pytest
import locators.order_page_locators as locators
import data
from pages.order_page import OrderPage

class TestOrderPage:
    @allure.title("Успешное создание заказа с параметризацией")
    @allure.description("Проверяем 2 позитивных сценария с двумя наборами данных пользователя. "
                        "Проверяем открытие формы заказа по нажатию кнопок 'Заказать' внизу страницы и в шапке")
    
    @pytest.mark.parametrize('order_button, order_data', [
        [locators.ORDER_BUTTON_HEADER, data.oleg_info],
        [locators.ORDER_DOWN_ON_MAIN_PAGE, data.elena_info]
    ] )
    
    def test_successful_order_creation_(self, driver_main_page, order_button, order_data):
        order_page = OrderPage(driver_main_page)
        order_page.open_order_form(order_button)
        order_page.fill_order_field(order_data)
        order_page.click_next_button()
        order_page.fill_rent_info(order_data)
        order_page.confirm_order()
        order_page.check_change_modal_window()
        order_text = order_page.get_successful_create_order_title()
        assert 'Номер заказа' in order_text

             
        