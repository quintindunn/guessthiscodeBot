import time

from selenium.common.exceptions import *
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def get_correct():
    create = """elemDiv = document.createElement('p');
elemDiv.innerText = rightLanguage;
elemDiv.id = "CorrectLanguage";
elemDiv.style.visibility = "hidden";
document.body.appendChild(elemDiv);"""
    remove = """document.getElementById("CorrectLanguage").remove();"""
    driver.execute_script(create)
    correct = driver.find_element(By.ID, 'CorrectLanguage').get_attribute('innerHTML')
    driver.execute_script(remove)
    return correct


def get_answers():
    answer_elements = driver.find_elements(By.XPATH, '/html/body/div/div[3]/button')
    answers = {}
    for element in answer_elements:
        answers[element.text] = element

    return answers


driver = Chrome()

site = "https://guessthiscode.com/"

driver.get(site)
time.sleep(2)

while True:
    try:
        get_answers()[get_correct()].click()
        driver.find_element(By.XPATH, '/html/body/div/div[4]/button[1]').click()
        time.sleep(1)
    except (ElementNotInteractableException, ElementClickInterceptedException):
        time.sleep(1)
        try:
            driver.find_element(By.XPATH, '/html/body/div/div[4]/button[1]').click()
        except Exception as e:
            print(e)
    except KeyError:
        time.sleep(1)
        pass

