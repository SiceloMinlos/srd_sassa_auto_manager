from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as x
from selenium.webdriver.support.ui import WebDriverWait

def personData():
    id_number = "your_id_number"
    cell_number = "your_cell_number"

    return id_number, cell_number


def check_online_status(id_number, cell_number):

    url = f'https://srd.sassa.gov.za/'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    WebDriverWait(driver, 10).until(x.element_to_be_clickable((By.XPATH, "//*[text()=' click here to check online ']"))).click()

    form_id_fill = driver.find_element(By.ID, 'mat-input-0')

    form_id_fill.send_keys(id_number)

    form_cell_number_fill = driver.find_element(By.ID, 'mat-input-1')

    form_cell_number_fill.send_keys(cell_number)

    submit_button = driver.find_element(By.CLASS_NAME, 'mat-button-wrapper')

    sleep(10)

    submit_button.click()

id_number, cell_number = personData()
check_online_status(id_number, cell_number)
