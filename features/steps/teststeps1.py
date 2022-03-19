from custom_expected_conditions import visibility_of_n_elements_located
from behave import *
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

main_search_result_link = "#rso .g [data-header-feature] > div:first-child > a"
PAGE_LOAD_TIMEOUT = 5
locator_links = (By.CSS_SELECTOR, main_search_result_link) 


@Given('Google search is loaded')
def launch_browser(context):
    context.driver = Firefox()
    # setting a timeout exception in case google doesn't load
    context.driver.set_page_load_timeout(10)
    context.driver.get('https://www.google.com')
#   context.current_page = GoogleSearchHome(context.driver)

#   look for the standards of naming conventions on python


@When('I search for "{value}"')
def search_for(context, value):
    # declaring the value of context.value so that it can be used in other functions
    context.value = value
    # looking for value in the Google input search box
    search = context.driver.find_element(By.NAME, "q")
    search.send_keys(value)
    search.send_keys(Keys.RETURN)


@Then('There are at least {number:d} links that result from it are saved')
def save_links(context, number):
    result_anchors = WebDriverWait(context.driver, timeout=PAGE_LOAD_TIMEOUT) \
        .until(visibility_of_n_elements_located(locator_links, number))
    links = [result.get_attribute('href') for result in result_anchors]
    with open(context.output_filename, 'a') as f:
        print(f"\nResults for {context.value}:", file=f)
        for item in links:
            print(f"{item}", file=f)
