from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

def _element_if_visible(element, visibility=True):
    return element if element.is_displayed() == visibility else False


def visibility_of_n_elements_located(locator: tuple[By, str], number: int):
    """ An expectation for checking that the required number of elements are present on the DOM of a
    page and visible. Visibility means that the elements are not only displayed
    but also has a height and width that is greater than 0.

    :param locator: Used to find the elements
    :param number: Used to declare the necessary amount of visible matching elements.

    :returns: A list of {number} Visible WebElements once they are located and visible.
    """

    def _predicate(driver):
        try:
            elements = driver.find_elements(*locator)
            if len(elements) < number:
                return False
            result = []
            for element in elements:
                if _element_if_visible(element):
                    result.append(element)
                    if len(result) >= number:
                        return result
            return False
        except StaleElementReferenceException:
            return False

    return _predicate