from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
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
def test_checksortingcountry(driver):
    # open page Countries
    driver.find_element_by_xpath("//span[text()='Countries']").click()

    list_countries = driver.find_elements_by_xpath("//table[@class='dataTable']//td[5]")
    list_country = []

    for x in list_countries:
        list_country.append(x.text)

    for count, value in enumerate(sorted(list_country)):
        name_countries = driver.find_elements_by_xpath("//table[@class='dataTable']//td[5]")[count]
        zones_count = driver.find_elements_by_xpath("//table[@class='dataTable']//td[6]")[count]


        assert value == name_countries.text

        if int(zones_count.text) > 0:

            driver.find_elements_by_xpath("//table[@class='dataTable']//td[5]//a")[count].click()
            driver.implicitly_wait(5)

            list_zonelocator = driver.find_elements_by_xpath("//table[@class='dataTable']//td[3]")
            list_zone = []
            for x in list_zonelocator:

                list_zone.append(x.text)

            del list_zone[-1:]

            for countzone, valuezone in enumerate(sorted(list_zone)):
                name_zone = driver.find_elements_by_xpath("//table[@class='dataTable']//td[3]")[countzone]

                assert valuezone == name_zone.text

            driver.find_element_by_xpath("//button[@name='cancel']").click()


def test_checksortinggeozone(driver):
    driver.find_element_by_xpath("//span[text()='Geo Zones']").click()

    list_countries = len(driver.find_elements_by_xpath("//table[@class='dataTable']//td[3]"))



    for count in range(list_countries):
        driver.find_elements_by_xpath("//table[@class='dataTable']//td[3]//a")[count].click()
        count_table = driver.find_elements_by_xpath("//table[@id='table-zones']//td[1]")
        list_id = []
        for x in count_table:
            list_id.append(x.text)

        list_select = []
        for count, value in enumerate(list_id):
            if value != '':

                select = Select(driver.find_element_by_xpath("//select[@name='zones["+str(value)+"][zone_code]']"))
                selected_option = select.first_selected_option
                list_select.append(selected_option.text)

            else:
                pass

        for count, value in enumerate(sorted(list_select)):
            if value != '':
                select = Select(driver.find_elements_by_css_selector("select[name$='[zone_code]']")[count])
                selected_option = select.first_selected_option
            else:
                pass

            assert selected_option.text == list_select[count]

        driver.find_element_by_xpath("//button[@name='cancel']").click()








