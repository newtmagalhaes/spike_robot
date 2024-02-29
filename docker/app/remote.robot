*** Settings ***
Library     SeleniumLibrary
Library     ./library/BrowserUtils.py
Library     ./library/RemoteFileHandler/


*** Variables ***
${BROWSER}      firefox


*** Tasks ***
Case 1: Abrir Youtube e gravar Screenshot
    [Setup]    Open youtube
    # Faz algo
    Capture Page Screenshot    ${BROWSER}.png
    # Sleep    10s
    [Teardown]    Close Browser

Case 2: Abrir site e baixar o chrome
    [Setup]    Open mozilla

    Sleep    5s
    Click download button

    ${session_id}=    Get Session Id
    ${filenames}=    Await download    ${session_id}

    Get file from grid    ${session_id}    ${filenames}

    [Teardown]    Close Browser


*** Keywords ***
Open youtube
    Set Screenshot Directory    /rpa/data
    Log To Console    REMOTO: %{REMOTE_URL=False}
    Open Browser    https://youtube.com    ${BROWSER}    remote_url=%{REMOTE_URL=False}

Open mozilla
    Set Screenshot Directory    /rpa/data
    Log To Console    REMOTO: %{REMOTE_URL=False}

    ${OPTIONS}=    Get Default Firefox Options
    Set DownloadsEnabled Option    ${OPTIONS}

    Open Browser
    ...    https://www.mozilla.org/pt-BR/firefox/new/
    ...    ${BROWSER}
    ...    remote_url=%{REMOTE_URL=False}
    ...    options=${OPTIONS}

Click download button
    Click Element    xpath=/html/body/div[3]/main/section[1]/div/div[1]/div/div[1]/a
    Log To Console    Botão de download pressionado

Await download
    [Arguments]    ${session_id}

    ${filenames}=    List Download Files    ${session_id}

    WHILE    ${filenames} == []
        Log    Aguardando download    console=${True}
        Sleep    1s
        ${filenames}=    List Download Files    ${session_id}
    END

    Log    Arquivo(s) baixado(s): ${filenames}    console=${True}
    RETURN    ${filenames}

Get file from grid
    [Arguments]    ${session_id}    ${filenames}

    FOR    ${name}    IN    @{filenames}
        Retrieve Download Files    ${session_id}    ${name}
    END
