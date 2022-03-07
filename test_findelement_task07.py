import pytest
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture #(scope="session", autouse=True)
def driver(request):
    ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
    op = webdriver.FirefoxOptions()
    wd = webdriver.Firefox(service=ser, options=op)


    wd.get("http://localhost:1234/litecart/admin/")

    wd.find_element_by_xpath("//input[@name='username']").send_keys("Admin")
    wd.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    wd.find_element_by_xpath("//button[@name='login']").click()
    wd.implicitly_wait(5)

    request.addfinalizer(wd.quit)
    return wd




@pytest.mark.skip
def test_search_menu_items_example1(driver):


    menu_category = ['Appearence','Template','Logotype','Catalog','Catalog','Product Groups', 'Option Groups','Manufacturers',
   'Suppliers','Delivery Statuses','Sold Out Statuses','Quantity Units','CSV Import/Export',
    'Countries','Currencies','Customers','Customers','CSV Import/Export','Newsletter','Geo Zones','Languages',
    'Languages','Storage Encoding','Modules','Background Jobs', 'Customer','Shipping','Payment','Order Total','Order Success',
    'Order Action','Orders','Orders','Order Statuses','Pages','Reports','Monthly Sales','Most Sold Products','Most Shopping Customers','Settings',
    'Store Info','Defaults','General','Listings','Images','Checkout','Advanced','Security','Slides','Tax','Tax Classes','Tax Rates','Translations',
    'Search Translations','Scan Files','CSV Import/Export','Users','vQmods','vQmods']

    for row in menu_category:

        driver.find_element_by_xpath("//span[normalize-space()='"+str(row)+"']").click()
        element  = driver.find_element_by_tag_name("h1").text


        if row == 'Appearence':
            assert element == 'Template'
        elif row == 'Modules':
            assert element == 'Job Modules'
        elif row == 'Background Jobs':
            assert element == 'Job Modules'
        elif row == 'Customer':
            assert element == 'Customer Modules'
        elif row == 'Shipping':
            assert element == 'Shipping Modules'
        elif row == 'Payment':
            assert element == 'Payment Modules'
        elif row == 'Order Total':
            assert element == 'Order Total Modules'
        elif row == 'Reports':
            assert element == 'Monthly Sales'
        elif row == 'Order Success':
            assert element == 'Order Success Modules'
        elif row == 'Order Action':
            assert element == 'Order Action Modules'
        elif row == 'Store Info' or  row == 'Defaults' or  row == 'General' or  row == 'Listings' or  row == 'Images' or  row == 'Checkout' or  row == 'Advanced' or  row == 'Security':
            assert element == 'Settings'
        elif row == 'Tax':
            assert element == 'Tax Classes'
        elif row == 'Translations':
            assert element == 'Search Translations'
        elif row == 'Scan Files':
            assert element == 'Scan Files For Translations'
        else:
            assert element == row

def test_search_menu_items_example2(driver):

    element_menu = len(driver.find_elements_by_xpath("//div[@id='box-apps-menu-wrapper']/ul/li"))

    for elementmenu in range(element_menu):
        driver.find_elements_by_xpath("//div[@id='box-apps-menu-wrapper']/ul/li")[elementmenu].click()
        element_li = len(driver.find_elements_by_xpath("//ul[@class='docs']/li"))
        heading = driver.find_element_by_tag_name("h1").text
        print(heading)

        for elementli in range(element_li):
            driver.find_elements_by_xpath("//ul[@class='docs']/li")[elementli].click()
            heading = driver.find_element_by_tag_name("h1").text
            print(heading)




