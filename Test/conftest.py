import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Config.config import TestData


@pytest.fixture(scope= 'class')
def init_driver(request):
    ser = Service(TestData.FIREFOX_EXECUTABLE_PATH)
    op = webdriver.FirefoxOptions()
    web_driver = webdriver.Firefox(service=ser, options=op)
    request.cls.driver = web_driver
    yield
    #web_driver.quit()