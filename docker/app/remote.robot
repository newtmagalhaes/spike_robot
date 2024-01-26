*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${BROWSER}      firefox


*** Tasks ***
Case 1: Abrir Youtube e gravar Screenshot
    [Setup]    Open youtube
    # Faz algo
    Capture Page Screenshot    ${BROWSER}.png
    # Sleep    10s
    [Teardown]    Close Browser


*** Keywords ***
Open youtube
    Set Screenshot Directory    ./data
    Log To Console    REMOTO: %{REMOTE_URL=False}
    Open Browser    https://youtube.com    ${BROWSER}    remote_url=%{REMOTE_URL=False}
