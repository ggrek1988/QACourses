import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import TestBase
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
    op = webdriver.FirefoxOptions()
    wd = webdriver.Firefox(service=ser, options=op)

    #close windows
    request.addfinalizer(wd.quit)
    return wd

def test_shopcart(driver):

    driver.get("http://localhost:1234/litecart/en/")
    wait = WebDriverWait(driver, 10)  # seconds
    waitindex = 1
    for el in range(3):
        index = random.randint(0,4)


        driver.find_elements_by_xpath("//div[@id='box-most-popular']//div[@class='image-wrapper']")[index].click()

        #wait for element quantity
        if TestBase.isElementPresentxPath(driver,"//select[@name='options[Size]']"):
            select = Select(driver.find_element_by_name('options[Size]'))
            select.select_by_visible_text('Small')
            driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
            #wait
            wait.until(EC.text_to_be_present_in_element((By.XPATH, "//span[@class='quantity']"), str(waitindex)))
            driver.find_element_by_xpath("//img[@title='My Store']").click()

        else:
            driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
            wait.until(EC.text_to_be_present_in_element((By.XPATH,"//span[@class='quantity']"),str(waitindex)))
            driver.find_element_by_xpath("//img[@title='My Store']").click()
        waitindex += 1

    driver.find_element_by_css_selector("div[id='cart'] a[class='link']").click()

    #delete products
    for el in range(3):

        name = driver.find_elements_by_xpath("//div[@class='viewport']//a")[1].get_attribute('textContent')
        driver.find_element_by_xpath("//button[@name='remove_cart_item']").click()
        # wait
        wait.until(EC.invisibility_of_element_located((By.XPATH,"//table[@class='dataTable rounded-corners']//td[text()='"+str(name)+"']")))




