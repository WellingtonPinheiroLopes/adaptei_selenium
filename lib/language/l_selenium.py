import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from lib.date.time import oneSeconds

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


def expectedTime(iformTime):
    time.sleep(iformTime)


def writingInHTMLFieldsContainingTextTypeId(tagHTML, attribute, attributevalue, text):
    driver.find_element(
        By.XPATH, f"//{tagHTML}[@{attribute}='{attributevalue}']"
    ).send_keys(text)
    expectedTime(oneSeconds)


def writingInHTMLFieldsContainingText(tagHTML, attribute, attributevalue, text):
    driver.find_element(
        By.XPATH, f"//{tagHTML}[{attribute}='{attributevalue}']"
    ).send_keys(text)
    expectedTime(oneSeconds)


def ClickOnAnHTMLElementContainingText(tagHTML, elementsHTML, nameText):
    driver.find_element(By.XPATH, f"//{tagHTML}[{elementsHTML}='{nameText}']").click()
    expectedTime(oneSeconds)


def clearHtmlFields(tagHTML, elementsHTML, nameText):
    driver.find_element(By.XPATH, f"//{tagHTML}[{elementsHTML}='{nameText}']").clear()
    expectedTime(oneSeconds)


def vistUrl(url):
    driver.get(url)
    driver.maximize_window()
    expectedTime(oneSeconds)
