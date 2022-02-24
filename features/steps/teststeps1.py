from behave import *
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait


@Given('Google is loaded in the Firefox Browser')
def launch_browser(context):
    context.browser = Firefox() 
    context.browser.get('https://www.google.com')
    

@When('A search for "{value}" is completed')
def search_for(context,value):
    search = context.browser.find_element(By.NAME, "q")
    search.send_keys(value)
    search.send_keys(Keys.RETURN)
    isit = presence_of_all_elements_located((By.CLASS_NAME, "yuRUbf"))
    WebDriverWait(context.browser, timeout=5).until(isit)
    if isit == True:
        pass
    @Then('The first five links that result from it are saved')
    def save_links(context):
        results = context.browser.find_elements(By.CLASS_NAME, "yuRUbf")
        links = [result.find_element(By.TAG_NAME,'a').get_attribute('href') for result in results]
        for index, link in enumerate(links[:5], start=1):
            print(f"Link #{index}: {link} \n")
        context.browser.quit()
