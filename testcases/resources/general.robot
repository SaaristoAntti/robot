*** Keywords ***
Open Login Page
    Open Browser        ${LOGIN URL}    ${BROWSER}

Verify Page Title
    Title Should Be     ${TITLE}