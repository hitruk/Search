
from selenium.webdriver.common.by import By

class ResultYandexPage:

    RESULT_BLOCKS = (By.CSS_SELECTOR, 'li.serp-item')
    RESULT_PHRASE = (By.NAME, 'text')

    @classmethod
    def LINK_TEXT(cls, phrase):
        xpath = f"//li[@class='serp-item']//a//*[contains(text(),'{phrase}')]"
        return (By.XPATH, xpath)

    def __init__(self, browser):
        self.browser = browser

    def result_blocks(self):
        blocks_result = self.browser.find_elements(*self.RESULT_BLOCKS)
        return len(blocks_result)

    def link_text_count(self, phrase):
        count_link_text = self.browser.find_elements(*self.LINK_TEXT(phrase))
        return len(count_link_text)

    def result_phrase(self):
        phrase_result = self.browser.find_element(*self.RESULT_PHRASE)
        return phrase_result.get_attribute('value')

