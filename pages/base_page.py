from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Ожидает, пока элемент станет видимым, и возвращает его
    def find_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    # Ожидает, пока элемент станет кликабельным, и кликает по нему
    def click_on_element(self, locator):
        element = (WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)))
        element.click()

    # Получает и возвращает текст из видимого элемента
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    # Заполняет текстовое поле указанным текстом
    def fill_text_to_field(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # Переходит по указанному URL
    def go_to_url(self, url):
        self.driver.get(url)

    # Прокручивает страницу, чтобы сделать указанный элемент видимым
    def scroll_to_element(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.find_element_with_wait(locator))
        self.find_element_with_wait(locator)

    # Заполняет поле текстом и нажимает клавишу Enter
    def fill_the_field_and_click_enter(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)
        element.send_keys(Keys.ENTER)
        
    def get_current_url(self):
        return self.driver.current_url
    
    def wait_until_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
    
    def scroll_and_click(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).click()
        
        
    def switch_to_last_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
