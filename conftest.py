import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import main_page_url, order_page_url

@allure.title("Открываем  Firefox")
@pytest.fixture
def driver_main_page():
    driver = webdriver.Firefox()
    driver.get(main_page_url)
    yield driver
    driver.quit()

@allure.title("Открываем Firefox на  оформлении заказа")
@pytest.fixture
def driver_order_page():
    driver = webdriver.Firefox()
    driver.get(order_page_url)
    yield driver
    driver.quit()