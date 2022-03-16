from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidSelectorException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def isElementPresentxPath(driver,locator:str):
    try:

        driver.find_element_by_xpath(locator)

        return True
    except NoSuchElementException:
        return False

def areElementsPresentxPath(driver,locator:str):
    try:
        element = driver.find_elements_by_xpath(locator)
        if len(element) > 0:
            return True
    except InvalidSelectorException:
        return False
