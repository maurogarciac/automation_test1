from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.support.ui import WebDriverWait

from custom_expected_conditions import visibility_of_n_elements_located

PAGE_LOAD_TIMEOUT = 5


class GoogleSearchResultPage(PageFactory):
    locators = {
        "resultTitle": ('CSS', '#rso .g [data-header-feature] > div:first-child > a')
    }

    def __init__(self,driver):
        self.driver = driver


    def find_links(self, number):
        
        result_anchors = WebDriverWait(self.driver, timeout = PAGE_LOAD_TIMEOUT) \
            .until(visibility_of_n_elements_located(self.locators["resultTitle"], number))
        return [result.get_attribute('href') for result in result_anchors]
