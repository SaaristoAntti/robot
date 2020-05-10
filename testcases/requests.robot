*** Settings ***
Library               Collections
Library               RequestsLibrary

*** Test Cases ***
Get Requests
    Create Session    github         http://api.github.com
    ${resp}=          Get Request    github               /users/saaristoantti
    Request Should Be Successful     ${resp}
    Status Should Be  200            ${resp}
    Dictionary Should Contain Value  ${resp.json()}       SaaristoAntti