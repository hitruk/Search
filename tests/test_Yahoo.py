
from selenium.webdriver.common.keys import  Keys


def test_search_yahoo(browser):

    URL = 'https://search.yahoo.com/'
    PHRASE = 'Hitruk'

    browser.get(URL)

    input_phrase = browser.find_element_by_id('yschsp')
    input_phrase.send_keys(PHRASE+Keys.RETURN)

    result_blocks = browser.find_elements_by_css_selector('#web>ol>li')
    assert len(result_blocks) > 0

    xpath = f"//h3[@class='title']//*[contains(text(), '{PHRASE}')]"
    link_text = browser.find_elements_by_xpath(xpath)
    assert len(link_text) > 0

    result_phrase = browser.find_element_by_css_selector('#yschsp')
    assert result_phrase.get_attribute('value') == PHRASE
