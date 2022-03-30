
from Pages.BasePages import BasePages
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddProductPages(BasePages):

    SHOPPAGE = (By.XPATH,"// img[ @ title = 'My Store']")
    SIZE_LOCATOR = "//select[@name='options[Size]']"
    SELECT_LOCATOR = "options[Size]"
    SELECT_TEXT = "Small"
    ADD_CART_PRODUCT = (By.XPATH,"//button[@name='add_cart_product']")
    SHOP_CART = (By.XPATH, "//span[@class='quantity']")

    def __init__(self,driver):
        super().__init__(driver)


    def find_select_element(self):
        element = self.isElementPresentxPath(self.SIZE_LOCATOR)
        return bool(element)

    def choose_select(self):
        select = Select(self.driver.find_element_by_name(self.SELECT_LOCATOR))
        select.select_by_visible_text(self.SELECT_TEXT)

    def button_add_product(self):
        self.do_click(self.ADD_CART_PRODUCT)

    def change_shoping_cart(self,index):
        self.text_change(self.SHOP_CART,index)

    def return_shoppages(self):
        self.do_click(self.SHOPPAGE)




