*** Settings ***
#Library    CustomSeleniumLibrary.py
Library    ..${/}..${/}Web_Adapter/Web_Core.py   Firefox   default
#Test Setup   Web Open Page

*** Test Cases ***
Verify that there are 2 cards on the board, Verify that there is a card with a comment And Set the card as DONE
    WEB Login    
    WEB Choose Board    Main Board
    WEB Verify Cards    TopListView    qtd=1
    WEB Add Card    Plentific
    WEB Verify Cards    TopListView    qtd=2
    WEB Add Comment    Plentific    Worked!
    WEB Verify Comment
    WEB Set Start Due Date    Casa    11/19/2022    11/19/2022    10:00 PM
    WEB Mark As Done    Casa    