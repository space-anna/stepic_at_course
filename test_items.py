from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_user_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    add_to_cart_button_xpath="//*[@id='add_to_basket_form']/button"
    try:
        WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.XPATH,add_to_cart_button_xpath )))
    except TimeoutException:
        raise AssertionError("Can not find add to cart button")
    assert len(browser.find_elements_by_xpath(add_to_cart_button_xpath)) == 1,"Unexpected number of elements found"

