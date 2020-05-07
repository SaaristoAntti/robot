*** Settings ***
Documentation     Example testcase 1:
...               use SeleniumLibrary and Robot Framework for web page testing
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      https://www.google.com
${BROWSER}        Chrome
${TITLE}          Google

*** Test Cases ***
Example 1
    [Documentation]     open webpage and verify page title
    Open Browser To Search Page
    Verify Page Title
    [Teardown]          Close Browser


*** Keywords ***
Open Browser To Search Page
    Open Browser        ${LOGIN URL}    ${BROWSER}

Verify Page Title
    Title Should Be     ${TITLE}