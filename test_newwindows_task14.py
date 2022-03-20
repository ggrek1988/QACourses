import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


@pytest.fixture
def driver(request):
    ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
    op = webdriver.FirefoxOptions()
    wd = webdriver.Firefox(service=ser, options=op)


    wd.get("http://localhost:1234/litecart/admin/")

    wd.find_element_by_xpath("//input[@name='username']").send_keys("Admin")
    wd.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    wd.find_element_by_xpath("//button[@name='login']").click()
    wd.implicitly_wait(5)
    #close windows
    request.addfinalizer(wd.quit)
    return wd

def test_newwindows(driver):
    wait = WebDriverWait(driver, 10)  # seconds

    driver.find_element_by_xpath("//span[normalize-space()='Countries']").click()
    pagesindex = random.randint(1,238)
    driver.find_elements_by_css_selector(".fa.fa-pencil")[pagesindex].click()

    element = len(driver.find_elements_by_css_selector(".fa.fa-external-link"))

    first_window = driver.current_window_handle
    main_title = driver.title

    for el in range(element):

        driver.find_elements_by_css_selector(".fa.fa-external-link")[el].click()

        #wait open new window
        wait.until(EC.number_of_windows_to_be(2))

        for second_window_handle in driver.window_handles:
            if second_window_handle != first_window:
                driver.switch_to.window(second_window_handle)
                wait.until(EC.presence_of_element_located((By.TAG_NAME, 'title')))
                #wait.until(EC.invisibility_of_element((By.TAG_NAME, 'title')))
                newtitle = driver.title
                driver.close()

        assert main_title != newtitle

        wait.until(EC.number_of_windows_to_be(1))
        driver.switch_to.window(first_window)


