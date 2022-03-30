
import pytest
import random

from Pages.AddProductPages import AddProductPages
from Pages.ShopPage import ShopPage
from Pages.ShoppingCartPages import ShoppingCartPages


@pytest.mark.usefixtures("init_driver")
class Test_shopcart():


    def test_shopcart(self):
        self.ShopPage = ShopPage(self.driver)
        self.AddProductPages = AddProductPages(self.driver)
        self.ShoppingCartPages = ShoppingCartPages(self.driver)

        self.ShopPage.get_pages()

        waitindex = 1
        for el in range(3):
            index = random.randint(0, 4)

            self.ShopPage.select_product(index)

            if self.AddProductPages.find_select_element():
                self.AddProductPages.choose_select()
                self.AddProductPages.button_add_product()
                self.AddProductPages.change_shoping_cart(waitindex)
                self.AddProductPages.return_shoppages()
            else:
                self.AddProductPages.button_add_product()
                self.AddProductPages.change_shoping_cart(waitindex)
                self.AddProductPages.return_shoppages()

            waitindex += 1


        self.ShopPage.click_page_shopingcart()

        self.ShoppingCartPages.delete_product_on_table()






