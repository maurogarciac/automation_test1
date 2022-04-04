from seleniumpagefactory.Pagefactory import PageFactory

from page_objects.GoogleSearchResultPage import GoogleSearchResultPage


class GoogleSearchHomePage(PageFactory):
    
    locators = {
        "input": ('NAME', 'q'),
        "submit": ('NAME', 'btnK'),
        "luckySubmit": ('NAME', 'btnI'),
        #"voiceSearch": ('CLASS', 'XDyW0e') #ARIA LABEL 'Search by voice' Totally useless
    }

    def __init__(self,driver):
        self.driver = driver

    
    def open_s(self):
        self.driver.get("https://www.google.com")
        

    def search(self, value, is_lucky = False):
        
        self.input.set_text(f"{value}")
        if is_lucky == True:
            self.luckySubmit.click_button()
        else:
            self.submit.click_button()
        return GoogleSearchResultPage(self.driver)