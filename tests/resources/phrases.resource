*** Variables ***
${MESSAGE}      Hello world!


*** Keywords ***
Falar Ola Mundo
    Log To Console    Aqui vai: ${MESSAGE}!

Falar adeus mundo
    Log To Console    Goodbye World
