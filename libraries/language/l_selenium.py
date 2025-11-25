import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from libraries.date.time import (
    oneSeconds,
)  # Mantendo o import, assumindo que é usado em outro lugar

options = Options()
options.add_experimental_option("detach", True)
# Se você tiver outras opções, pode adicioná-las aqui:
# options.add_argument("--headless") # Para rodar o Chrome sem interface gráfica
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
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
