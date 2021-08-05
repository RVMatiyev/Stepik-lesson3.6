import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_contain_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("form#add_to_basket_form>button")
    time.sleep(10)


    assert button, "Кнопка не найдена"



