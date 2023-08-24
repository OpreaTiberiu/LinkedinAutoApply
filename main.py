import time
import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.common import InvalidSelectorException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

load_dotenv()


def easy_apply(driver):
    easy_apply_button = driver.find_element(
        by=By.CSS_SELECTOR,
        value="div.jobs-apply-button--top-card button"
    )
    easy_apply_button.click()

    time.sleep(2)

    phone_number_input = driver.find_element(
        by=By.CSS_SELECTOR,
        value="div div div div input"
    )
    phone_number_input.send_keys(os.environ["phone_number"])

    click_next_button(driver)
    click_next_button(driver)

    try:
        # Specific select for a job I actually tested this on
        select_element = driver.find_element(
            by=By.CSS_SELECTOR,
            value="div div div select"
        )
        select = Select(select_element)
        select.select_by_value("No")
    except InvalidSelectorException as e:
        print(e)

    click_next_button(driver)
    click_next_button(driver)


def click_next_button(driver):
    next_button = driver.find_element(
        by=By.CSS_SELECTOR,
        value="footer div button.artdeco-button--primary"
    )
    next_button.click()
    time.sleep(1)


driver = webdriver.Chrome()

driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3676396322&f_AL=true&f_C=1449&f_E=4&f_WT=2&geoId=105773754&keywords=remote&location=Bucharest%2C%20Romania")

time.sleep(2)

sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value="header nav div a.nav__button-secondary")
sign_in_button.click()

username_input = driver.find_element(by=By.ID, value="username")
username_input.send_keys(os.environ["email"])
pass_input = driver.find_element(by=By.ID, value="password")
pass_input.send_keys(os.environ["pass"])
sign_in_button = driver.find_element(
    by=By.CSS_SELECTOR,
    value="form div button.btn__primary--large.from__button--floating"
)
sign_in_button.click()

time.sleep(2)

job_list_element = driver.find_elements(
    by=By.CSS_SELECTOR,
    value="div.scaffold-layout__list ul.scaffold-layout__list-container li.jobs-search-results__list-item"
)

for job_element in job_list_element:
    job_element.click()
    # Insert whatever logic you want
    # easy_apply(driver)
    time.sleep(5)
