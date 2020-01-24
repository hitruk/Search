from page.search_Google import SearchGooglePage
from page.result_Google import ResultGooglePage

def test_search_google(browser):

    PHRASE = 'Hitruk'

    search_page = SearchGooglePage(browser)
    search_page.load_page()
    search_page.input_phrase(PHRASE)

    result_page = ResultGooglePage(browser)
    assert result_page.result_blocks() > 0
    assert result_page.link_text_count(PHRASE) > 0
    assert result_page.result_phrase() == PHRASE



