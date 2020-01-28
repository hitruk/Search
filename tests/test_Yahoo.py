
from page.search_Yahoo import SearchYahooPage
from page.result_Yahoo import ResultYahooPage

def test_search_yahoo(browser):

    PHRASE = 'Hitruk'

    search_page = SearchYahooPage(browser)
    search_page.load_page()
    search_page.input_phrase(PHRASE)

    result_page = ResultYahooPage(browser)
    assert result_page.result_blocks() > 0
    assert result_page.link_text(PHRASE) > 0
    assert result_page.result_phrase() == PHRASE
