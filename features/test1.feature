Feature: Fetching the links from a Google search

    Fetching links from google 

    Scenario Outline: First Five links
        Given Google is loaded in the Firefox Browser
        When A search for "<value>" is completed
            Examples:
            | value   |
            | Banana  |
            | Pera    |
            | Manzana |
            | Naranja |
       
        Then The first five links that result from it are saved