from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, Chrome):
        self.driver = Chrome.driver
        self.downloads = Chrome.downloads

    def find_and_clic_element(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(EC.element_to_be_clickable(locator),
                                                message=f"Can't find element by locator {locator}")

    def find_element_in_children(self, locator, element):
        return element.find_element(*locator)

    def find_elements_in_children(self, locator, element):
        return element.find_elements(*locator)

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_element_with_text(self, locator, text, time=2, element=None):
        if not element:
            elements = self.find_elements(locator, time)
        else:
            elements = self.find_elements_in_children(locator, element)
        xpath = f'.//*[contains(text(), "{text}")]'

        for element_ in elements:
            try:
                blok_with_text = element_.find_element("xpath", xpath)
                return element_
            except:
                pass

    

    def is_text_in_element_by_locator(self, locator, text, time=10):
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


    def click_on_the_link(self, locator, text_link, tag_locator, element=None):
        element_ = self.find_element_with_text(locator, text_link, time=2, element=element)
        link = self.find_element_in_children(tag_locator, element_)
        if link:
            print(link.text)
            self.clic_element(link)


    def scroll_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def go_to_site(self, url):
        return self.driver.get(url)
    
    def get_title(self):
        return self.driver.title
    
    def refresh(self):
        self.driver.refresh()

    # def download_file(self, ):
    #     element = 1
    #     self.clic_element(element)

