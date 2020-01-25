
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SearchYandexPage:

    URL = 'https://yandex.ru/'
    INPUT_PHRASE = (By.NAME, 'text')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def input_phrase(self, phrase):
        phrase_input = self.browser.find_element(*self.INPUT_PHRASE)
        phrase_input.send_keys(phrase+Keys.RETURN)
