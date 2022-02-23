Feature: Fetching the first five links from a google search

    Getting the five links saved in a variable for each 

    Scenario: Looking for bananas?
        Given Google is loaded in the Firefox Browser
        When A search is completed
        Then The first five links that result from that are saved
        And The browser closes

    Scenario: Looking for oranges?
        Given Google is loaded in the Firefox Browser
            When A search is completed
            Then The first five links that result from that are saved
            And The browser closes

    Scenario: Looking for apples?
        Given Google is loaded in the Firefox Browser
            When A search is completed
            Then The first five links that result from that are saved
            And The browser closes

    Scenario: Looking for torta?
         Given Google is loaded in the Firefox Browser
            When A search is completed
            Then The first five links that result from that are saved
            And The browser closes

    Scenario: Looking for pan dulce?
        Given Google is loaded in the Firefox Browser
           When A search is completed
           Then The first five links that result from that are saved
           And The browser closes