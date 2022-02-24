from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait
import traceback

def cosito(loook_for):
    driver = webdriver.Firefox()
    try:
        driver.get("https://google.com.ar")
        print(f"{driver.title} is loaded")
        search = driver.find_element(By.NAME, "q")
        search.send_keys(loook_for)
        search.send_keys(Keys.RETURN)
        WebDriverWait(driver, timeout=5).until(presence_of_all_elements_located((By.CLASS_NAME, "yuRUbf")))

        results = driver.find_elements(By.CLASS_NAME, "yuRUbf")
        links = [result.find_element(By.TAG_NAME,'a').get_attribute('href') for result in results]

        for index, link in enumerate(links[:5], start=1): #print the links in a list
            print(f"Link #{index}: {link} \n")
    except:
        print("no anda nada", traceback.format_exc())
    finally:
        driver.quit()