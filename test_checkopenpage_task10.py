from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    ser = Service("C:\\driver_firefox_selenium\\geckodriver.exe")
    op = webdriver.FirefoxOptions()
    wd = webdriver.Firefox(service=ser, options=op)

    #close windows
    request.addfinalizer(wd.quit)
    return wd

#@pytest.mark.skip
def test_checkopenware(driver):

    # open page
    driver.get("http://localhost:1234/litecart/en/")

    name = driver.find_element_by_css_selector("div#box-campaigns div.name")
    textproduct = name.text
    regular_price = driver.find_element_by_css_selector("div#box-campaigns s.regular-price")
    textregular_price = regular_price.text
    campaign_price = driver.find_element_by_css_selector("div#box-campaigns strong.campaign-price")
    textcampaign_price = campaign_price.text

    #check style price
    colorproce = regular_price.value_of_css_property('color')
    print(colorproce)
    campaign = campaign_price.value_of_css_property('color')
    print(campaign)

    # check tag name
    print(regular_price.tag_name)
    print(campaign_price.tag_name)

    #CLICK PRODUCT
    driver.find_element_by_css_selector("div#box-campaigns a.link").click()

    titleproduct = driver.find_element_by_css_selector("h1.title")
    regular_priceproduct = driver.find_element_by_css_selector("s.regular-price")
    campaign_priceproduct = driver.find_element_by_css_selector("strong.campaign-price")

    # check style price
    colorproce = regular_priceproduct.value_of_css_property('color')
    print(colorproce)
    campaign = campaign_priceproduct.value_of_css_property('color')
    print(campaign)

    #check tag name
    print(regular_priceproduct.tag_name)
    print(campaign_priceproduct.tag_name)



    #check name product
    assert titleproduct.text == textproduct

    #check regular price
    assert textregular_price == regular_priceproduct.text

    # check campaign price
    assert textcampaign_price == campaign_priceproduct.text


