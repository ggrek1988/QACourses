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

def test_LoginAdmin(driver):
    driver.get("http://localhost:1234/litecart/admin")
    driver.find_element_by_xpath("//input[@name='username']").send_keys("Admin")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    driver.find_element_by_xpath("//button[@name='login']").click()
