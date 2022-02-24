Feature: Fetching the links from a Google search

    Fetching links from google

    Scenario Outline: First Five links
        Given Google search is loaded
        When I search for "<value>"
        Then There are at least <number> links that result from it are saved
        Examples:
            | value   | number |
            | Banana  | 5      |
            | Pera    | 7      |
            | Manzana | 2      |
            | Naranja | 1      |