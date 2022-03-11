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
    page1_colorprice = regular_price.value_of_css_property('color')
    page1_text_decoration = regular_price.value_of_css_property('text-decoration')

    page1_colorcampaign = campaign_price.value_of_css_property('color')
    page1_colorcampaign_text_decoration = campaign_price.value_of_css_property('text-decoration')


    #CLICK PRODUCT
    driver.find_element_by_css_selector("div#box-campaigns a.link").click()

    titleproduct = driver.find_element_by_css_selector("h1.title")
    regular_priceproduct = driver.find_element_by_css_selector("s.regular-price")
    campaign_priceproduct = driver.find_element_by_css_selector("strong.campaign-price")

    # check style price
    page2_colorprice = regular_priceproduct.value_of_css_property('color')
    page2_text_decoration = regular_priceproduct.value_of_css_property('text-decoration')
   
    page2_colorcampaign = campaign_priceproduct.value_of_css_property('color')
    page2_colorcampaign_text_decoration = campaign_priceproduct.value_of_css_property('text-decoration')




    #check name product
    assert titleproduct.text == textproduct

    #check regular price
    assert textregular_price == regular_priceproduct.text

    # check campaign price
    assert textcampaign_price == campaign_priceproduct.text

    #check style $20
    #text
    if page1_text_decoration == page2_text_decoration:
        assert True
    else:
        print("Styl is not equal value $20")

    #color
    if page1_colorprice == page2_colorprice:
        assert True
    else:
        print("Styl color is not equal value $20")

    # check style $18
    # text
    if page1_colorcampaign == page2_colorcampaign:
         assert True
    else:
        print("Styl is not equal value $18")

        # color
    if page1_colorcampaign_text_decoration == page2_colorcampaign_text_decoration:
        assert True
    else:
        print("Styl color is not equal value $18")






