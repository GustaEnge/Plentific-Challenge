*** Settings ***
Library    Collections
Library    SeleniumLibrary
Library    API_Adapter/API_Core.py    default

*** Variables ***
${result_api}
${board_api_id}=    63a23548adfc80018de2fa97
${board_web_id}=    XEnYSvuZ
${list_id}=    63a23549e01103010fe0bd79
@{id_card_list}

*** Test Cases ***
Create Board
    ${result_api}   API Create Board    name=Plentific Board    
    ${board_web_id}=    Set Variable    ${result_api}[0]
    ${board_api_id}=    Set Variable    ${result_api}[1]
    Set Global Variable    ${board_web_id}   
    Set Global Variable    ${board_api_id}  
Create List API
    ${result_api}   List Create    name=Solutions    idBoard=${board_api_id}    
    ${list_id}=    Set Variable    ${result_api}[0]
    Set Global Variable    ${list_id}

Create 3 Cards
    ${result_api}    API Create Card    name=Task 1    idList=${list_id}    
    ${card_id_1}=    Set Variable    ${result_api}[0]
    ${result_api}    API Create Card    name=Task 2    idList=${list_id}    
    ${card_id_2}=    Set Variable    ${result_api}[0]
    ${result_api}    API Create Card    name=Task 3    idList=${list_id}    
    ${card_id_3}=    Set Variable    ${result_api}[0]
    @{id_card_list}     Create List    ${card_id_1}    ${card_id_2}    ${card_id_3}
    Set Global Variable    @{id_card_list}
    

Update a Card
    ${result_api}    API Update Card    ${id_card_list}[0]    name=Task 4 

Delete a Card
    API Delete Card    ${id_card_list}[2]

Add a Comment
    API Create Comment    ${id_card_list}[0]    Worked!