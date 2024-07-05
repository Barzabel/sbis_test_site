from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://sbis.ru/"

    def find_and_clic_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.element_to_be_clickable(locator),
                                                message=f"Can't find element by locator {locator}")
        

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")
    
    def is_text_in_element(self, locator, text, time=10):
        return WebDriverWait(self.driver,time).until(EC.text_to_be_present_in_element(locator, text),
                                                      message=f"Can't find element by locator {locator}")


    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def is_url_contains(self, url, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_contains(url),
                                                      message=f"Can't find url {url}")

    def switch_to_new_windows(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)


    def clic_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def go_to_site(self):
        return self.driver.get(self.base_url)