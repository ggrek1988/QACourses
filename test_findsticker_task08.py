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

    driver.get("http://localhost:1234/litecart/")
    elementduck = len(driver.find_elements_by_xpath("//div[@class='content']//li[@class='product column shadow hover-light']"))
    salestikers_list = len(driver.find_elements_by_xpath("//li[@class='product column shadow hover-light']//div[@title='On Sale']"))
    newstiker_list = len(driver.find_elements_by_xpath("//li[@class='product column shadow hover-light']//div[@title='New']"))

    #checking if the number of stickers is equal to the number of articles
    assert elementduck == salestikers_list + newstiker_list

    for elduck in range(elementduck):
        elementduck1 = driver.find_elements_by_xpath("//div[@class='content']//div[@class='image-wrapper']")[elduck]
        element2 = len(elementduck1.find_elements_by_xpath(".//div[starts-with(@class, 'sticker')]"))

        assert element2 == 1



