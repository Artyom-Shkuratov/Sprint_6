import pytest
import allure
from selenium import webdriver
from data import main_page_url

@allure.title("Открываем  Firefox")
@pytest.fixture
def driver_main_page():
    driver = webdriver.Firefox()
    driver.get(main_page_url)
    yield driver
    driver.quit()
