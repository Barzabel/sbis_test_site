from tests.SbisPage import SearchHelper

START_URL = "https://sbis.ru/"

def test_sbis_first_script(browser):
    """ 1) Перейти на https://sbis.ru/ в раздел "Контакты"
        2) Найти баннер Тензор, кликнуть по нему
        3) Перейти на https://tensor.ru/
        4) Проверить, что есть блок "Сила в людях"
        5) Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается
        https://tensor.ru/about
        6) Находим раздел Работаем и проверяем, что у всех фотографии хронологии
        одинаковые высота (height) и ширина (width)"""
    main_page = SearchHelper(browser)
    main_page.go_to_site(START_URL)
    main_page.click_on_the_link_heder("Контакты")
    main_page.click_on_the_label_button()
    assert main_page.check_string('Сила в людях')
    main_page.click_on_the_about_link('Сила в людях')
    assert main_page.check_url("https://tensor.ru/about")
    imgs = main_page.get_img(main_page.get_element_by_h_in_container("Работаем"))
    assert main_page.is_size_img_equal(imgs)
