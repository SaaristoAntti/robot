*** Settings ***
Documentation     Login example:
...               login to webpage
Library           SeleniumLibrary
Resource          resources/general.robot

*** Variables ***
${LOGIN URL}        http://127.0.0.1:5500/login.html
${BROWSER}          Chrome
${TITLE}            login testpage
${USERNAME}         username
${PASSWORD}         password


*** Test Cases ***
Login example
    [Documentation]     open webpage and verify page title
    Open Login Page
    Verify Page Title
    Input Username And Password
    [Teardown]          Close Browser


*** Keywords ***
Input Username And Password
    Wait Until Element Is Visible   id=password
    Input Text                      id=username     ${USERNAME}
    Input Text                      id=password     ${PASSWORD}
    Click Button                    id=submit
