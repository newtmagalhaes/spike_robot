*** Settings ***
# <- exemplo de comentário de código
Documentation       <-hello_world->

Resource            ../resources/phrases.resource

Suite Setup         Log To Console    suite setup
Suite Teardown      Log To Console    suite teardown
Test Setup          Log To Console    test setup
Test Teardown       Log To Console    test teardown


*** Test Cases ***
Case 1: hello_world
    [Documentation]    Escreve "olá mundo"
    ...    e pode ser mais de uma linha
    [Tags]    hello_world
    [Setup]    Log To Console    running setup

    Falar Ola Mundo

    [Teardown]    Log To Console    running teardown

Case 2: goodbye_world
    [Documentation]    Escreve "adeus mundo"

    Falar adeus mundo
    Falhar no teste


*** Keywords ***
Falhar no teste
    [Documentation]    Faz uma verificação
    ...    e falha
    Should Be True    ${False}    msg=Sempre falha
