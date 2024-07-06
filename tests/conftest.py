import pytest
from selenium import webdriver
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Chrome:
    driver: webdriver.Chrome
    downloads: Path


@pytest.fixture(scope="function")
def browser(tmp_path):
    options = webdriver.ChromeOptions()
    options.add_argument("--allow-running-insecure-content")  # Allow insecure content
    options.add_argument("--unsafely-treat-insecure-origin-as-secure=https://sbis.ru")  
    options.add_experimental_option("prefs", {
        "download.default_directory": str(tmp_path),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    driver = webdriver.Chrome(options=options)
    yield Chrome(driver=driver, downloads=tmp_path)
    driver.quit()