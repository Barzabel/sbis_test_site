from tests.SbisPage import SearchHelper


OUR_REGION = "Нижегородская обл."
NEW_REGION = "Камчатский край"
REGION_CODE_IN_URL = "41"
START_URL = "https://sbis.ru/"

def test_sbis_second_script(browser):
    """
    1) Перейти на https://sbis.ru/ в раздел "Контакты"
    2) Проверить, что:
     - определился ваш регион;
     - есть список партнеров.
    3) Изменить регион на Камчатский край
    4) Проверить, что:
        - подставился выбранный регион; 
        - список партнеров изменился;
        - url и title содержат информацию выбранного региона.
    """
    main_page = SearchHelper(browser)
    main_page.go_to_site(START_URL)
    main_page.click_on_the_link_heder("Контакты")
    assert main_page.check_our_region(OUR_REGION)
    assert main_page.check_partners_exist()
    main_page.click_on_the_region_link()
    partners_old = main_page.get_partners_titlse()
    main_page.click_on_popup_region_link(NEW_REGION)
    partners_new = main_page.get_partners_titlse()
       
    assert main_page.check_our_region(NEW_REGION)
    assert partners_old != partners_new
    assert main_page.check_url(REGION_CODE_IN_URL)
    assert main_page.check_title(NEW_REGION)
    