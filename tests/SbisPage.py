from tests.BaseApp import BasePage
from selenium.webdriver.common.by import By

class SbisSeacrhLocators:
    LOCATOR_FIELD = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content")
    LOCATOR_CONTACTS_BUTTON = (By.CLASS_NAME, "sbisru-Header__menu-link")                                         
    LOCATOR_LABEL_BUTTON = (By.CSS_SELECTOR, "a.sbisru-Contacts__logo-tensor")
    LOCATOR_ABOUT_LINK = (By.CLASS_NAME, "tensor_ru-link")  
    LOCATOR_IMG_CONTENT = (By.CSS_SELECTOR, "img.tensor_ru-About__block3-image")
    


class SearchHelper(BasePage):

    def get_img(self,):
        img_elements = self.find_elements(SbisSeacrhLocators.LOCATOR_IMG_CONTENT, time=4)
        return img_elements

    def is_size_img_equal(self,img_elements):
        size_imgs = [(img.get_attribute("height"), img.get_attribute("width")) for img in img_elements]
        return all(x == size_imgs[0] for x in size_imgs)

    def check_string(self, string):
        return self.is_text_in_element(SbisSeacrhLocators.LOCATOR_FIELD, string, time=2)
    
    def click_on_the_about_link(self, string):
        elements = self.find_elements(SbisSeacrhLocators.LOCATOR_FIELD, time=2)
        for element in elements:
            if string in element.text:
                about_link = element.find_element(*SbisSeacrhLocators.LOCATOR_ABOUT_LINK)
                print(about_link.text)
                self.clic_element(about_link)
                break
        return True


    def check_url(self, url):
        return self.is_url_contains(url)

    def click_on_the_contacts_button(self):
        elements = self.find_elements(SbisSeacrhLocators.LOCATOR_CONTACTS_BUTTON, time=2)
        for element in elements:
            if "Контакты" in element.text:
                element.click()
                break
        return True
    
    def click_on_the_label_button(self):
        self.find_and_clic_element(SbisSeacrhLocators.LOCATOR_LABEL_BUTTON, time=2).click()
        self.switch_to_new_windows()

        return True

