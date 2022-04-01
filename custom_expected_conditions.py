from ctypes import Union
from seleniumpagefactory.Pagefactory import PageFactory
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from typing import Union

def _element_if_visible(element, visibility=True):
    return element if element.is_displayed() == visibility else False


def visibility_of_n_elements_located(locator: tuple[Union[By, str], str], number: int):
    """ An expectation for checking that the required number of elements are present on the DOM of a
    page and visible. Visibility means that the elements are not only displayed
    but also has a height and width that is greater than 0.

    :param locator: Used to find the elements
    :param number: Used to declare the necessary amount of visible matching elements.

    :returns: A list of {number} Visible WebElements once they are located and visible.
    """

    def _predicate(driver):
        result = False
        try:
            [by, selector] = locator #pattern matching
            elements = driver.find_elements(by if isinstance(by, By) else PageFactory.TYPE_OF_LOCATORS[by.lower()], selector)
            if len(elements) >= number:
                result = []
                e_iter = iter(elements)
                while (element := next(e_iter, None)) is not None and len(result) < number:
                    if _element_if_visible(element):
                        result.append(element)
            result = False if len(result) < number else result
        except StaleElementReferenceException:
            result = False
        return result
    
    return _predicate
