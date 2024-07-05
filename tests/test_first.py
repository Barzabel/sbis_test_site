from tests.SbisPage import SearchHelper

def test_Sbis_search(browser):
    """First script"""
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.click_on_the_contacts_button()
    main_page.click_on_the_label_button()
    assert main_page.check_string('Сила в людях')
    main_page.click_on_the_about_link('Сила в людях')
    assert main_page.check_url("https://tensor.ru/about")
    imgs = main_page.get_img()
    assert main_page.is_size_img_equal(imgs)