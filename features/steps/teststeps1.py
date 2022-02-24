from behave import *
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait

main_search_result_link = "#rso .g [data-header-feature] > div:first-child > a"
PAGE_LOAD_TIMEOUT = 5  # look how to declare as set constant


def after_scenario(context):
    context.browser.quit()


@Given('Google search is loaded')
def launch_browser(context):
    context.browser = Firefox()
    # setting a timeout exception in case google doesn't load
    context.browser.set_page_load_timeout(10)
    context.browser.get('https://www.google.com')


@When('I search for "{value}"')
def search_for(context, value):
    # declaring the value of context.value so that it can be used in other functions
    context.value = value
    # looking for value in the google input search box
    search = context.browser.find_element(By.NAME, "q")
    search.send_keys(value)
    search.send_keys(Keys.RETURN)


@Then('There are at least {number} links that result from it are saved')
def save_links(context, number):
    WebDriverWait(context.browser, timeout=PAGE_LOAD_TIMEOUT).until(presence_of_all_elements_located(By.CSS_SELECTOR, main_search_result_link))  # puede ser una custom expected condition
    result_anchors = context.browser.find_elements(By.CSS_SELECTOR, main_search_result_link)
    links = [result.get_attribute('href') for result in result_anchors]
    with open('test.txt', 'a') as f:
        print(f"\nResults for {context.value}:", file=f)
        for item in links[:int(number)]:
            print(f"{item}", file=f)
