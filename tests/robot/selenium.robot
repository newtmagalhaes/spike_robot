*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${URL}          https://dgg.gg
${BROWSER}      firefox


*** Tasks ***
Case 1: pesquisar algo
    Open Browser    ${URL}    ${BROWSER}
    Input Text    //*[@id\="searchbox_input"]    docker
    Click Element    /html/body/div/main/article/div[1]/div[1]/div/section[1]/form/div/div/button[2]
