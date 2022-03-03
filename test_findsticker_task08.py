import pytest
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
    op = webdriver.FirefoxOptions()
    wd = webdriver.Firefox(service=ser, options=op)
    request.addfinalizer(wd.quit)
    return wd

def testfindstikers(driver):

    driver.get("http://localhost:82/litecart/")
    elementduck = len(driver.find_elements_by_xpath("//div[@id='content']//article[@class='product']"))
    salestikers_value = len(driver.find_elements_by_xpath("//article[@class='product']//div[@title='On Sale']"))
    newstiker_value = len(driver.find_elements_by_xpath("//article[@class='product']//div[@title='New']"))

    #checking if the number of stickers is equal to the number of articles
    assert elementduck == salestikers_value + newstiker_value

    for elduck in range(elementduck):
        elementduckone = driver.find_elements_by_xpath("//div[@id='content']//article[@class='product']")[elduck]
        element = len(elementduckone.find_elements_by_xpath(".//div[starts-with(@class, 'sticker')]"))

        assert element == 1

