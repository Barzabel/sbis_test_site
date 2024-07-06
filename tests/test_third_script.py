import os
from tests.SbisPage import SearchHelper


START_URL = "https://sbis.ru/"
NAME_TO_DOWNLOAD = "Веб-установщик"
FILE_NAME = "sbisplugin-setup-web.exe"
FILE_SIZE = 7570584


def test_sbis_third_script(browser):
    """
    1) Перейти на https://sbis.ru/
    2) в Footer'e найти и перейти "Скачать локальные версии"
    3) Скачать СБИС Плагин для вашей для windows, веб-установщик в папку c данным тестом
    4) Убедиться, что плагин скачался
    5) Сравнить размер скачанного файла в мегабайтах. Он должен совпадать c указанным на сайте (в примере 3.64 МБ).
    """
    main_page = SearchHelper(browser)
    main_page.go_to_site(START_URL)
    main_page.click_on_the_link_footer("Скачать локальные версии")
    main_page.download(NAME_TO_DOWNLOAD)
    assert main_page.is_file_downloaded(FILE_NAME)
    assert main_page.is_file_size_equel(FILE_NAME, FILE_SIZE)
    