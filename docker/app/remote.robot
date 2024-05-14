*** Settings ***
Library     SeleniumLibrary


*** Tasks ***
Case 1: Abrir Youtube e gravar Screenshot
    [Setup]    Open youtube
    # Faz algo
    Sleep    15s
    Capture Page Screenshot
    [Teardown]    Close Browser


*** Keywords ***
Open youtube
    Set Screenshot Directory    /rpa/data
    Log To Console    REMOTO: %{REMOTE_URL=False}
    Open Browser    https://youtube.com    firefox    remote_url=%{REMOTE_URL=False}
