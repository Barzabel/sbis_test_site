from tests.SbisPage import SearchHelper


def test_sbis_second_script(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()