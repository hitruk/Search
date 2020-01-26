
from page.search_Yandex import SearchYandexPage
from page.result_Yandex import ResultYandexPage

def test_search_yandex(browser):

    PHRASE = 'Hitruk'

    search_page = SearchYandexPage(browser)
    search_page.load_page()
    search_page.input_phrase(PHRASE)

    result_page = ResultYandexPage(browser)
    assert result_page.result_blocks() > 0
    assert result_page.link_text_count(PHRASE) > 0
    assert result_page.result_phrase() == PHRASE
