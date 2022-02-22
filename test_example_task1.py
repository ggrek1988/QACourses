import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver(request):
    ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
    op = webdriver.FirefoxOptions()
    wd = webdriver.Firefox(service=ser, options=op)
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("https://www.google.com/")


