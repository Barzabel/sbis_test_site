from tests.BaseApp import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
import time


class SbisSeacrhLocators:
    LOCATOR_FIELD = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content")                                     
    LOCATOR_LABEL_BUTTON = (By.CSS_SELECTOR, "a.sbisru-Contacts__logo-tensor")
    LOCATOR_ABOUT_LINK = (By.CLASS_NAME, "tensor_ru-link")  
    LOCATOR_IMG_CONTENT = (By.CSS_SELECTOR, "img.tensor_ru-About__block3-image")
    LOCATOR_CONTAINER = (By.CLASS_NAME, "tensor_ru-container")
    LOCATOR_HEADING = (By.CLASS_NAME, "tensor_ru-header-h2")
    LOCATOR_PARTNER = (By.XPATH, '//div[@item-parent-key="-2"]')

    # second script
    LOCATOR_PARTNER_TITLE = (By.CLASS_NAME, "sbisru-Contacts-List__name")
    LOCATOR_POPUP_REGION_LINK = (By.CSS_SELECTOR, "li.sbis_ru-Region-Panel__item")
    LOCATOR_REGION_LINK = (By.CSS_SELECTOR, "span.sbis_ru-Region-Chooser__text")
    LOCATOR_CONTAINER_SBIS = (By.CLASS_NAME, "controls-ListViewV__itemsContainer")
    LOCATOR_HEDER_LINKS  = (By.CSS_SELECTOR, "li.sbisru-Header__menu-item")
    LOCATOR_A = (By.TAG_NAME, "a")
    LOCATOR_SPAN = (By.TAG_NAME, "span")



class SearchHelper(BasePage):

    def get_element_by_h_in_container(self, heading_text):
        elements = self.find_elements(SbisSeacrhLocators.LOCATOR_CONTAINER, time=2)
        for element in elements:
            try: 
                h = self.find_element_in_children(SbisSeacrhLocators.LOCATOR_HEADING, element)
                if heading_text in h.text:
                    return element
            except NoSuchElementException: 
                continue

    def get_img(self, element):
        img_elements = element.find_elements(By.TAG_NAME, "img")
        return img_elements

    def is_size_img_equal(self,img_elements):
        size_imgs = [(img.get_attribute("height"), img.get_attribute("width")) for img in img_elements]
        return all(x == size_imgs[0] for x in size_imgs)

    def check_string(self, string):
        return self.is_text_in_element(SbisSeacrhLocators.LOCATOR_FIELD, string, time=2)
    
    def check_our_region(self, region):
        return self.is_text_in_element(SbisSeacrhLocators.LOCATOR_REGION_LINK, region, time=2)

    def check_partners_exist(self):
        elements = self.find_elements(SbisSeacrhLocators.LOCATOR_CONTAINER_SBIS, time=2)
        for element in elements:
            try: 
                partner = self.find_element_in_children(SbisSeacrhLocators.LOCATOR_PARTNER, element)
                if partner:
                    return True
            except NoSuchElementException: 
                pass
        return False

    def check_title(self, title):
        return title in self.get_title()

    def get_partners_titlse(self):
        self.scroll_page()
        elements = self.find_elements(SbisSeacrhLocators.LOCATOR_CONTAINER_SBIS, time=3)
        for element in elements:
            try: 
                partners = self.find_elements_in_children(SbisSeacrhLocators.LOCATOR_PARTNER, element)
                partners_title = [self.find_element_in_children(SbisSeacrhLocators.LOCATOR_PARTNER, x).text for x in partners]
                return partners_title
            except NoSuchElementException: 
                pass


    def click_on_the_about_link(self, string):
        elements = self.find_elements(SbisSeacrhLocators.LOCATOR_FIELD, time=2)
        for element in elements:
            if string in element.text:
                link =  self.find_element_in_children(SbisSeacrhLocators.LOCATOR_ABOUT_LINK, element)
                self.clic_element(link)
                break
        return True

    def click_on_the_region_link(self):
        element = self.find_element(SbisSeacrhLocators.LOCATOR_REGION_LINK, time=2)
        self.clic_element(element)
        return True

    def click_on_popup_region_link(self, region):
        elements = self.find_elements(SbisSeacrhLocators.LOCATOR_POPUP_REGION_LINK, time=2)
        for element in elements:
            if region in element.text:
                span = self.find_element_in_children(SbisSeacrhLocators.LOCATOR_SPAN, element)
                self.clic_element(span)
                time.sleep(1)   
                self.refresh()
                break
        return True

    def check_url(self, url):
        return self.is_url_contains(url)

    def click_on_the_link(self, text_link):
        elements = self.find_elements(SbisSeacrhLocators.LOCATOR_HEDER_LINKS, time=2)
        
        for element in elements:
            a = self.find_element_in_children(SbisSeacrhLocators.LOCATOR_A, element)
            if text_link in element.text:
                self.clic_element(a)
                break
        return True
    
    def click_on_the_label_button(self):
        element = self.find_and_clic_element(SbisSeacrhLocators.LOCATOR_LABEL_BUTTON, time=2)
        self.clic_element(element)
        self.switch_to_new_windows()

        return True


