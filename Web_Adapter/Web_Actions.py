from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def click_button_by_class(driver, name):
    button = _wait_for_element_by_type(driver, 'class', name)
    button.click()

def click_button_by_id(driver, name):
    button = _wait_for_element_by_type(driver, 'id', name)
    button.click()

def write_text_by_id(driver, name, text):
    text_box = _wait_for_element_by_type(driver, 'id', name)
    text_box.clear()
    text_box.send_keys(text)

def write_text_by_name(driver, name, text):
    text_box = _wait_for_element_by_type(driver, 'name', name)
    text_box.clear()
    text_box.send_keys(text)

def write_text_by_class(driver, name, text):
    text_box = _wait_for_element_by_type(driver, 'class', name)
    text_box.clear()
    text_box.send_keys(text)

def write_text_by_xpath(driver, name, text):
    text_box = _wait_for_element_by_type(driver, 'xpath', name)
    text_box.clear()
    text_box.send_keys(text)

def click_button_by_xpath(driver, name, timeout = 5):
    try:
            button = _wait_for_element_by_type(driver, 'xpath', name, timeout)
            button.click()
    except:
        driver.execute_script(js_checkbox % name)

js_checkbox = '''
                let a = document.evaluate("%s", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                a.click();
              '''

def click_button_by_link_text(driver, name):
    button = _wait_for_element_by_type(driver, 'link_text', name)
    button.send_keys("\n")
    #button.click()

def get_text_by_class(driver, name):
    text = _wait_for_element_by_type(driver, 'class', name)
    return text.text

def get_text_by_id(driver, name):
    text = _wait_for_element_by_type(driver, 'id', name)
    return text.text

def get_text_by_xpath(driver, name):
    text = _wait_for_element_by_type(driver, 'xpath', name)
    return text.text


def _wait_for_element_by_type(driver, type, name, timeout = 15):
    if type == 'class'     : method = By.CLASS_NAME
    if type == 'id'        : method = By.ID
    if type == 'link_text' : method = By.LINK_TEXT
    if type == 'xpath'     : method = By.XPATH
    if type == 'name'      : method = By.NAME
    if type == 'css'      : method = By.CSS_SELECTOR
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((method, name))
        )
    except: TimeoutException
    return element

def _wait_for_elements_by_type(driver, type, name, timeout = 15):
    if type == 'class'     : method = By.CLASS_NAME
    if type == 'id'        : method = By.ID
    if type == 'link_text' : method = By.LINK_TEXT
    if type == 'xpath'     : method = By.XPATH
    if type == 'name'      : method = By.NAME
    if type == 'css'      : method = By.CSS_SELECTOR
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((method, name))
        )
    except: TimeoutException
    return element

def submit(driver,method,value):
    findElement(driver,method,value).submit()


def change_tab(driver):
    current_tab = driver.current_window_handle
    chwd = driver.window_handles
    for tab in chwd:
        if tab != current_tab:
            driver.switch_to.window(tab)

def waitPage(driver):
    """
    Wait the page till reach a state of complete rendering
    """
    wait = WebDriverWait(driver, 30)
    wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

def findElement(driver,type,value,many=False):
    try:
        element=None
        if not many: element =_wait_for_element_by_type(driver,type,value)
        else:  element = _wait_for_elements_by_type(driver,type,value)
    except: NoSuchElementException
    return  element

def checkBox_mark(driver,mode,value):
    try:
            element = findElement(driver,mode,value)
            if not element.is_selected(): element.click()
    except:
        if mode == 'xpath': driver.execute_script(js_checkbox % value)


js_checkbox = '''
                let a = document.evaluate("%s", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                let cond = a.getAttribute("aria-checked");
                if(!!cond) a.click();
              '''