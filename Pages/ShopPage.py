from Config.config import TestData
from Pages.BasePages import BasePages
from selenium.webdriver.common.by import By


class ShopPage(BasePages):

    PRODUCT_EL = "//div[@id='box-most-popular']//div[@class='image-wrapper']"
    BASKET_CART = (By.CSS_SELECTOR, "div[id='cart'] a[class='link']")


    def __init__(self,driver):
        super().__init__(driver)


    def get_pages(self):
        self.driver.get(TestData.BASE_URL)

    def select_product(self,index):
        self.click_element_index(self.PRODUCT_EL,index)

    def click_page_shopingcart(self):
        self.do_click(self.BASKET_CART)

