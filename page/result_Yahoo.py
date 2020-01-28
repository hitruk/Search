
from selenium.webdriver.common.by import By

class ResultYahooPage:

    RESULT_BLOCKS = (By.CSS_SELECTOR, '#web>ol>li')
    PHRASE_RESULT = (By.CSS_SELECTOR, '#yschsp')

    @classmethod
    def LiNK_TEXT(cls, phrase):
        xpath = f"//h3[@class='title']//*[contains(text(), '{phrase}')]"
        return (By.XPATH, xpath)

    def __init__(self, browser):
        self.browser = browser

    def result_blocks(self):
        blocks_result = self.browser.find_elements(*self.RESULT_BLOCKS)
        return len(blocks_result)

    def link_text(self, phrase):
        text_link = self.browser.find_elements(*self.LiNK_TEXT(phrase))
        return len(text_link)

    def result_phrase(self):
        phrase_result = self.browser.find_element(*self.PHRASE_RESULT)
        return phrase_result.get_attrubute('value')
