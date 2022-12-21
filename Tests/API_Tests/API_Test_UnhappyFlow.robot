*** Settings ***
Library    Collections
Library    API_Adapter/API_Core.py    default

*** Variables ***
${result_api}
${board_api_id}=    63a23548adfc80018de2fa97
${board_web_id}=    XEnYSvuZ
${list_id}=    63a23549e01103010fe0bd79
@{id_card_list}

*** Test Cases ***

Create List API by using wrong idBoard
    Run Keyword And Expect Error    error 400 : invalid value for idBoard    List Create    name=Solutions    idBoard=something
    #Should Contain        ${result_api}    invalid value for idBoard

Create 1 Card without idList
    Run Keyword And Expect Error    error 400 : invalid value for idList    API Create Card    name=Task 1    
    
Create 1 Card with wrong idList
    Run Keyword And Expect Error    error 400 : invalid value for idList    API Create Card    name=Task 1    idList=something   

Delete a Card with id that doesn't exist
    Run Keyword And Expect Error    error 400 : invalid id    API Delete Card    321334

Add a Comment with wrong card_id
    Run Keyword And Expect Error    error 400 : invalid id    API Create Comment    something    Worked!

Add a Comment with not formatted/encoded params
    Run Keyword And Expect Error    error 400 : Malformed URL    API Create Comment    6392490c41691e0357445907    Worked%H1dds