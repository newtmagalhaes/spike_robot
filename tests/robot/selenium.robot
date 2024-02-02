*** Settings ***
Library     SeleniumLibrary
Library     ../libraries/FirefoxConfig.py


*** Variables ***
${URL}          https://dgg.gg
${BROWSER}      firefox
# ${firefox_profile}    c:\\Users\\aniltoncastro\\Desktop\\repos\\AccordBI\\RobosPy\\RoboSITRAM\\PerfilFireFox

*** Tasks ***
Case 1: pesquisar algo
    Open Browser    ${URL}    ${BROWSER}
    Input Text    //*[@id\="searchbox_input"]    docker
    Click Element    /html/body/div/main/article/div[1]/div[1]/div/section[1]/form/div/div/button[2]

Open Firefox Without Default Browser Check
    # Create WebDriver    Firefox    firefox_profile=${EXECDIR}/firefox_profile
    # ${OPTIONS}=    Get Firefox Options    #${firefox_profile}
    # Log To Console    ${OPTIONS}
    Open Browser    https://www.dadosmundiais.com/downloads/    firefox    remote_url=http://localhost:4444    #options=${OPTIONS}    #ff_profile_dir=${firefox_profile}
    # Sleep    5s
    
    Click Element    xpath=/html/body/div[1]/main/div[2]/div[1]/div[1]/div[2]/a
    # Go To    https://google.com
    [Teardown]    Close Browser


*** Keywords ***
# Create WebDriver
#     [Arguments]    ${browser}    ${firefox_profile}=NONE
#     ${options}=    Evaluate    sys.modules['selenium.webdriver'].FirefoxOptions()    sys, selenium.webdriver
#     Call Method    ${options}    set_preference    browser.shell.checkDefaultBrowser    False
#     ${profile}=    Create Dictionary    firefox_profile=${firefox_profile}
#     ${driver}=    Create Webdriver    ${browser}    options=${options}    desired_capabilities=${profile}
#     Set Suite Variable    ${driver}
#     RETURN    ${driver}
