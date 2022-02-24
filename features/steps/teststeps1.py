from behave import *
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException as ex

@Given('Google is loaded in the Firefox Browser')
def launch_browser(context):
    context.browser = Firefox()
    try:
    #setting a timeout exception in case google doesn't load
        context.browser.set_page_load_timeout(10)
        context.browser.get('https://www.google.com')
    except ex:
    #printing the error and closing the browser window
        print("An exception has been thrown. " + str(ex))
        context.browser.close()

@When('A search for "{value}" is completed')
def search_for(context,value):
#declaring the value of context.value so that it can be used in other functions
    context.value = value
#looking for value in the google input search box
    search = context.browser.find_element(By.NAME, "q")
    search.send_keys(value)
    search.send_keys(Keys.RETURN)
#waiting at most 5 seconds for the div to load in the page
    is_it_there = presence_of_all_elements_located((By.CLASS_NAME, "yuRUbf"))
    WebDriverWait(context.browser, timeout=5).until(is_it_there)
    
    @Then('The first five links that result from it are saved')
    def save_links(context):
        try:
        #looking for the div that has a specific Class assigned
            results = context.browser.find_elements(By.CLASS_NAME, "yuRUbf")
            links = [result.find_element(By.TAG_NAME,'a').get_attribute('href') for result in results]
            for index, link in enumerate(links, start=1):
                print(f"Link #{index}: {link} \n")
        #create a container for the links
            add_these_lines = []
            add_these_lines += links[:5]
        #save all the links to a txt file
            with open('test.txt', 'a') as f:
                f.write(f"\n{str(context.value)} \n")
                for item in add_these_lines:
                    f.writelines("%s\n" % item) 
        except:
        #if less than 5 links were found, fail the step and close the browser
            add_these_lines.count() >= 4
            print("Not enough links were available.")
            context.browser.quit()   
        finally:
            context.browser.quit()
