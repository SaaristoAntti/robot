*** Variables ***
${WELCOME MESSAGE}      Welcome user!

*** Keywords ***
Open Login Page
    Open Browser        ${LOGIN URL}    ${BROWSER}

Verify Page Title
    Title Should Be     ${TITLE}

Validate Login
    Handle Alert
    Wait Until Page Contains        ${WELCOME MESSAGE}