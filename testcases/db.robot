*** Settings ***
Library     DatabaseLibrary

*** Variables ***
${DBNAME}       customers
${DBUSER}       root
${DBPASSWD}     example
${DBHOST}       localhost
${DBPORT}       3306
${DBTABLE}      customer
${DBMODULE}     pymysql
@{QUERY RESULTS}

*** Test Cases ***
Verify Table On Database
    Connect To Database     ${DBMODULE}     ${DBNAME}   ${DBUSER}   ${DBPASSWD}     ${DBHOST}   ${DBPORT}
    Table Must Exist    ${DBTABLE}
    Check If Exists In Database     SELECT * FROM ${DBTABLE}
    @{queryResults}     Query       SELECT * FROM ${DBTABLE}
    Log to console    @{QUERY RESULTS}[0]