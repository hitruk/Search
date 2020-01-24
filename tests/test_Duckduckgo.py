from page.search_Duckduckgo import SearchDuckduckgoPage
from page.result_Duckduckgo import ResultDuckduckgoPage

def test_search_duckduckgo(browser):

    PHRASE = 'Hitruk'

    search_page = SearchDuckduckgoPage(browser)
    search_page.load_page()
    search_page.input_phrase(PHRASE)

    result_page = ResultDuckduckgoPage(browser)
    assert result_page.result_blocks() > 0
    assert result_page.link_text_count(PHRASE) > 0
    assert result_page.result_phrase() == PHRASE