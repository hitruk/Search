
from selenium.webdriver.common.keys import Keys
from page.search_Yandex import SearchYandexPage
def test_search_yandex(browser):

    PHRASE = 'Hitruk'
    # URL = 'https://yandex.ru/'

    # browser.get(URL)
    #
    # input_phrase = browser.find_element_by_id("text")
    # input_phrase.send_keys(PHRASE+Keys.RETURN)

    search_page = SearchYandexPage(browser)
    search_page.load_page()
    search_page.input_phrase(PHRASE)


    result_blocks = browser.find_elements_by_css_selector('li.serp-item')
    assert len(result_blocks) > 0

    xpath = f"//li[@class='serp-item']//a//*[contains(text(),'{PHRASE}')]"
    link_text = browser.find_elements_by_xpath(xpath)
    assert len(link_text) > 0

    result_phrase = browser.find_element_by_name('text')
    assert result_phrase.get_attribute('value') == PHRASE