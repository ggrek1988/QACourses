import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

@pytest.fixture
def driver(request):

    # d = DesiredCapabilities.FIREFOX
    # d['loggingPrefs'] = {'browser': 'ALL'}
    # ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
    # op = webdriver.FirefoxOptions()
    # wd = webdriver.Firefox(capabilities=d, service=ser, options=op)

    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    ser = Service("C:\\driver_firefox_selenium\\chromedriver.exe")
    op = webdriver.ChromeOptions()
    wd = webdriver.Chrome(desired_capabilities=d, service=ser, options=op)

    wd.get("http://localhost:1234/litecart/admin/")

    wd.find_element_by_xpath("//input[@name='username']").send_keys("Admin")
    wd.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    wd.find_element_by_xpath("//button[@name='login']").click()
    wd.implicitly_wait(5)
    #close windows
    request.addfinalizer(wd.quit)
    return wd

def test_checkbrowses(driver):
    wait = WebDriverWait(driver, 10)  # seconds
    driver.find_element_by_xpath("//span[normalize-space()='Catalog']").click()
    driver.find_element_by_xpath("//a[contains(text(),'Rubber Ducks')]").click()

    wait.until(EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, "a[href*='category_id=1&product_id'][title='Edit']")))
    products = len(driver.find_elements_by_css_selector("a[href*='category_id=1&product_id'][title='Edit']"))

    for el in range(products):
        driver.find_elements_by_css_selector("a[href*='category_id=1&product_id'][title='Edit']")[el].click()
        try:
            for entry in driver.get_log('browser'):
                print(entry)
        except:
            print("no logs")

        driver.find_element_by_xpath("//button[@name='cancel']").click()