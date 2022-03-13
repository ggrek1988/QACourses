from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
import random
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
    op = webdriver.FirefoxOptions()
    wd = webdriver.Firefox(service=ser, options=op)

    #open page admin
    wd.get("http://localhost:1234/litecart/admin/")
    wd.find_element_by_xpath("//input[@name='username']").send_keys("Admin")
    wd.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    wd.find_element_by_xpath("//button[@name='login']").click()
    wd.implicitly_wait(5)
    #close windows
    request.addfinalizer(wd.quit)
    return wd

#@pytest.mark.skip
def test_addarticle(driver):

    driver.find_element_by_xpath("//span[normalize-space()='Catalog']").click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("//a[normalize-space()='Add New Product']").click()

    #GENERAL
    #1.Status
    driver.find_element_by_css_selector("input[type='radio'][value='1']").click()

    #2. Name
    name = "Product"+str(random.randrange(100))
    driver.find_element_by_css_selector("input[name='name[en]']").send_keys(str(name))

    #3.code
    code = 'PRO'+str(random.randrange(99999))
    driver.find_element_by_css_selector("input[name='code']").send_keys(str(code))

    #4. Categories
    driver.find_element_by_css_selector("input[name='categories[]'][value='1']").click()

    #5.Product Groups
    product_groups = random.randint(1,3)
    driver.find_element_by_css_selector("input[name='product_groups[]'][value='1-"+str(product_groups)+"']").click()

    #6 quantity
    driver.find_element_by_css_selector("input[name='quantity']").send_keys('3.00')

    #7 Date Valid From
    date_valid_from = driver.find_element_by_css_selector("input[name='date_valid_from']")
    driver.execute_script(f"arguments[0].setAttribute('value', '2022-03-01'); arguments[0].dispatchEvent(new Event('change'))",date_valid_from)

    #8
    # 7 Date Valid To
    date_valid_from = driver.find_element_by_css_selector("input[name='date_valid_to']")
    driver.execute_script(f"arguments[0].setAttribute('value', '2022-03-31'); arguments[0].dispatchEvent(new Event('change'))",date_valid_from)

    #Information
    #1 open tab
    driver.find_element_by_xpath("//a[normalize-space()='Information']").click()

    #2 Manufacturer
    select = Select(driver.find_element_by_name('manufacturer_id'))
    select.select_by_visible_text('ACME Corp.')

    #3 Keywords
    driver.find_element_by_css_selector("input[name='keywords']").send_keys('keywords')

    #4 Short Descriptions
    driver.find_element_by_css_selector("input[name='short_description[en]']").send_keys('short_description')

    #5 Description
    driver.find_element_by_css_selector("div[class='trumbowyg-editor']").send_keys('Description')

    #5 Head Title
    driver.find_element_by_css_selector("input[name='head_title[en]']").send_keys('Head Title')

    #6 Meta Description
    driver.find_element_by_css_selector("input[name='meta_description[en]']").send_keys('Meta Description')

    # Prices
    #1 open tab
    driver.find_element_by_xpath("//a[normalize-space()='Prices']").click()

    #2 Purchase Price
    driver.find_element_by_css_selector("input[name='purchase_price']").send_keys('3.00')
    select = Select(driver.find_element_by_name('purchase_price_currency_code'))
    select.select_by_visible_text('Euros')

    #3 Price, Price Incl. Tax (?)
    driver.find_element_by_css_selector("input[name='prices[USD]']").send_keys('10.00')
    driver.find_element_by_css_selector("input[name='prices[EUR]']").send_keys('10.00')

    #4 Campaigns
    driver.find_element_by_xpath("//a[@id='add-campaign']//i[@class='fa fa-plus-circle']").click()
    start_date = driver.find_element_by_css_selector("input[name='campaigns[new_1][start_date]']")
    driver.execute_script(
        f"arguments[0].setAttribute('value', '2022-03-17T01:02'); arguments[0].dispatchEvent(new Event('change'))",
        start_date)
    end_date = driver.find_element_by_css_selector("input[name='campaigns[new_1][end_date]']")
    driver.execute_script(
        f"arguments[0].setAttribute('value', '2022-03-31T01:02'); arguments[0].dispatchEvent(new Event('change'))",
        end_date)
    driver.find_element_by_css_selector("input[name='campaigns[new_1][USD]']").send_keys('10.00')

    #save product
    driver.find_element_by_xpath("//button[@name='save']").click()

    #assertion check the product on the list
    driver.implicitly_wait(2)
    print("//a[normalize-space()='"+str(name)+"']")
    product = len(driver.find_elements_by_xpath("//a[normalize-space()='"+str(name)+"']"))

    assert product == 1










