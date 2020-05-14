*** Settings ***
Documentation     Login to webpage

Library           SeleniumLibrary
#Library           lib/StaticSeleniumLibrary
Resource          resources/general.robot

*** Variables ***
#${LOGIN URL}        http://127.0.0.1:5500/login.html
${LOGIN URL}        https://saaristoantti.github.io/robot/testpages/login.html
${BROWSER}          Chrome
${TITLE}            login testpage
${USERNAME}         user
${PASSWORD}         password

# https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html
*** Test Cases ***
Login example
    [Documentation]     input username and password with id selectors
    [Tags]  id
    Open Login Page
    Verify Page Title
    Input Username And Password With Id
    Validate Login
    [Teardown]          Close Browser

Login example With CSS
    [Documentation]     input username and password with css selectors
    [Tags]  css
    Open Login Page
    Verify Page Title
    Input Username And Password With CSS
    Validate Login
    [Teardown]          Close Browser

Login Example With Xpath
    [Documentation]     input username and password with xpath selectors
    [Tags]  xpath
    Open Login Page
    Input Username And Password With Xpath
    Validate Login
    [Teardown]          Close Browser

*** Keywords ***
Input Username And Password With Xpath
    Wait Until Element Is Visible   xpath=//*[@class='usernameclass']
    Input Text                      xpath=//*[@class='usernameclass']     ${USERNAME}
    Input Text                      xpath=//*[@class='passwordclass']     ${PASSWORD}
    Click Button                    //input[@value='Login']

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