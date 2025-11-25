# import time

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from libraries.date.time import oneSeconds

# options = Options()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)


import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from libraries.date.time import oneSeconds

options = Options()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


def expectedTime(iformTime):
    time.sleep(iformTime)


def writingInHTMLFieldsContainingTextTypeId(tagHTML, attribute, attributevalue, text):
    elements = driver.find_element(
        By.XPATH, f"//{tagHTML}[@{attribute}='{attributevalue}']"
    )
    elements.send_keys(text)
    assert elements.get_attribute("value") == text
    expectedTime(oneSeconds)


def writingInHTMLFieldsContainingText(tagHTML, attribute, attributevalue, text):
    elements = driver.find_element(
        By.XPATH, f"//{tagHTML}[{attribute}='{attributevalue}']"
    )
    elements.send_keys(text)
    assert elements.get_attribute("value") == text
    expectedTime(oneSeconds)


def ClickOnAnHTMLElementContainingText(tagHTML, elementsHTML, nameText):
    elements = driver.find_element(
        By.XPATH, f"//{tagHTML}[{elementsHTML}='{nameText}']"
    )
    elements.click()
    expectedTime(oneSeconds)


def ClickingOnHTMLElementsContainingXPHATContais(tagHTML, elementsHTML, nameText):
    elements = driver.find_element(
        By.XPATH, f" //{tagHTML}[{elementsHTML}(., '{nameText}')]"
    )
    elements.click()
    expectedTime(oneSeconds)


def clickOnSpecificHTMLElement(tagHTML):
    elements = driver.find_element(By.XPATH, tagHTML)
    elements.click()
    expectedTime(oneSeconds)


def clearHtmlFields(tagHTML, elementsHTML, nameText):
    driver.find_element(By.XPATH, f"//{tagHTML}[{elementsHTML}='{nameText}']").clear()
    expectedTime(oneSeconds)


def vistUrl(url):
    driver.get(url)
    driver.maximize_window()
    expectedTime(oneSeconds)


def closeSystem():
    driver.quit()
