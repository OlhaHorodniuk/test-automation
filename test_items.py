import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_presence_button_basket(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
