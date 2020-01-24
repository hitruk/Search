from selenium.webdriver.common.by import By

class ResultGooglePage:

    RESULT_BLOCKS = (By.CSS_SELECTOR, '.rc')
    RESULT_PHRASE = (By.NAME, 'q')

    @classmethod
    def LINK_TEXT(cls, phrase):
        xpath = f"//div[@class='bkWMgd']//a//*[contains(text(), '{phrase}')]"
        return (By.XPATH, xpath)

    def __init__(self, browser):
        self.browser = browser

    def result_blocks(self):
        result_blocks = self.browser.find_elements(*self.RESULT_BLOCKS)
        return len(result_blocks)

    def link_text_count(self, phrase):
        link_text = self.browser.find_elements(*self.LINK_TEXT(phrase))
        return len(link_text)

    def result_phrase(self):
        phrase_result = self.browser.find_element(*self.RESULT_PHRASE)
        return phrase_result.get_attribute('value')