
from Pages.BasePages import BasePages
from selenium.webdriver.common.by import By


class ShoppingCartPages(BasePages):

    LENGHT_ELEMENT = "li.shortcut"
    DELETE_EL = "//div[@class='viewport']//a"
    DELETE_BUTTON = (By.XPATH, "//button[@name='remove_cart_item']")

    def __init__(self,driver):
        super().__init__(driver)

    def delete_product_on_table(self):
        shortcut = self.lenght_elements(self.LENGHT_ELEMENT)

        for el in range(shortcut):
            name = self.get_attribute_element(self.DELETE_EL,'textContent')
            self.do_click(self.DELETE_BUTTON)
            Element = (By.XPATH,"//table[@class='dataTable rounded-corners']//td[text()='"+str(name)+"']")
            self.is_disable_table(Element)

