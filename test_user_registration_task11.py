from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from faker import Faker


@pytest.fixture
def driver(request):
    ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
    op = webdriver.FirefoxOptions()
    wd = webdriver.Firefox(service=ser, options=op)

    #close windows
    #request.addfinalizer(wd.quit)
    return wd


def test_userregistration(driver):
    faker = Faker('pl_PL')
    driver.get("http://localhost:1234/litecart/en/")
    driver.find_elements_by_css_selector("[name='login_form'] td")[4].click()

    driver.find_element_by_css_selector("[name='firstname']").send_keys(faker.first_name())
    driver.find_element_by_css_selector("[name='lastname']").send_keys(faker.last_name())
    driver.find_element_by_css_selector("[name='address1']").send_keys(faker.street_address())
    driver.find_element_by_css_selector("[name='postcode']").send_keys('22-222')
    driver.find_element_by_css_selector("[name='city']").send_keys(faker.city())
    email = faker.email()
    driver.find_element_by_css_selector("[name='email']").send_keys(str(email))
    driver.find_element_by_css_selector("[name='phone']").send_keys('12345678')

    password = '123'
    driver.find_element_by_css_selector("[name='password']").send_keys(str(password))
    driver.find_element_by_css_selector("[name='confirmed_password']").send_keys(str(password))

    #create_account
    driver.find_element_by_css_selector("button[name='create_account").click()


    driver.implicitly_wait(5)
    #logout
    driver.find_element_by_xpath("//div[@class='content']//a[contains(text(),'Logout')]").click()

    #re-login
    driver.find_element_by_xpath("//input[@name='email']").send_keys(email)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(str(password))
    driver.find_element_by_xpath("//button[@name='login']").click()
    driver.find_element_by_xpath("//div[@class='content']//a[contains(text(),'Logout')]").click()















