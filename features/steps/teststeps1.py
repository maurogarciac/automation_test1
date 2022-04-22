from behave import Given, Then, When
from page_objects.GoogleSearchHomePage import GoogleSearchHomePage
from selenium.webdriver import Firefox


@Given('Google search is loaded')
def google_instance(context):
    driver = Firefox()
    context.driver = driver
    context.currentpage = GoogleSearchHomePage(context.driver)
    context.currentpage.open_s()
    

@When('I search for "{value}"')
def search_for(context, value):
    context.value = value
    context.currentpage = context.currentpage.search(value)


@Then('There are at least {number:d} links that result from it are saved')
def save_links(context, number):
    context.number = number
    links = context.currentpage.find_links(context.number)
    with open(context.output_filename, 'a') as f:
            print(f"\nResults for {context.value}:", file = f)
            for item in links:
                print(f"{item}", file = f)
