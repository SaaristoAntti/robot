*** Settings ***
Documentation   EXAMPLE REST testcase
Library         REST    https://jsonplaceholder.typicode.com

*** Variables ***
${EXPECTED_ID}          1
${EXPECTED_NAME}        Leanne Graham
${EXPECTED_USERNAME}    Bret

*** Test Cases ***
GET USER VALIDATE ID, NAME AND USERNAME
    GET             /users/1                # new instance
    Output schema   response body           # this will print out response
    Object          response body           # values are fully optional
    Integer         response body id          ${EXPECTED_ID}     # verify id value
    String          response body name        ${EXPECTED_NAME}   # verify name value
    String          response body username    ${EXPECTED_USERNAME}   # verify usernname
    #[Teardown]  Output schema             # note the updated response schema
