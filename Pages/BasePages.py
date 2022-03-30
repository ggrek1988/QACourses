
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

"""This class is the parent of all class"""
class BasePages:

    def __init__(self,driver):
        self.driver = driver

    def isElementPresentxPath(self, by_locator):
        try:
            self.driver.find_element_by_xpath(by_locator)
            return True
        except NoSuchElementException:
            return False

    def text_change(self,by_locator,text):
        element = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((by_locator), str(text)))
        return bool(element)

    def is_disable_table(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((by_locator)))
        return bool(element)

    def click_element_index(self,by_locator,index):
        self.driver.find_elements_by_xpath(by_locator)[index].click()

    def do_click(self,by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by_locator))).click()

    def select_element(self,by_locator,text):
        select = Select(self.driver.find_element_by_name(by_locator))
        select.select_by_visible_text(text)

    def lenght_elements(self,by_locator):
        shortcut = len(self.driver.find_elements_by_css_selector(by_locator))
        return int(shortcut)

    def get_attribute_element(self,by_locator,attribute):
        name = self.driver.find_elements_by_xpath(by_locator)[1].get_attribute(attribute)
        return name


