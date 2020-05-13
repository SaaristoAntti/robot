*** Settings ***
Documentation     Login to webpage

Library           SeleniumLibrary
Resource          resources/general.robot

*** Variables ***
${LOGIN URL}        http://127.0.0.1:5500/login.html
${BROWSER}          Chrome
${TITLE}            login testpage
${USERNAME}         user
${PASSWORD}         password


*** Test Cases ***
Login example
    [Documentation]     open webpage and verify page title
    Open Login Page
    Verify Page Title
    Input Username And Password With Id
    Validate Login
    [Teardown]          Close Browser

Login example With CSS
    [Documentation]     open webpage and verify page title
    [Tags]  css
    Open Login Page
    Verify Page Title
    Input Username And Password With CSS
    Validate Login
    [Teardown]          Close Browser

*** Keywords ***
Input Username And Password With Id
    Wait Until Element Is Visible   id=password
    Input Text                      id=username     ${USERNAME}
    Input Text                      id=password     ${PASSWORD}
    Click Button                    id=submit

Input Username And Password With CSS
    Wait Until Element Is Visible   class=passwordclass
    Input Text                      class=usernameclass     ${USERNAME}
    Input Text                      class=passwordclass     ${PASSWORD}
    Click Button                    class=buttonclass