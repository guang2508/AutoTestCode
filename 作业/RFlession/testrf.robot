*** Settings ***
Library   SeleniumLibrary
Library  Collections
*** Test Cases ***
case1
    loginwebsite   auto     sdfsdfsdf
    sleep  2
    ${lessonses}     getLessions      xpath://*[@total-items="totalNum"]/td[2]/span
    LOG TO CONSOLE  ${lessonses}
    close browser
*** Keywords ***
loginwebsite
    [Arguments]   ${username}   ${password}
    open browser   http://localhost:82/mgr/login/login.html   chrome
    set selenium implicit wait  10
    INPUT TEXT   id=username    ${username}
    INPUT TEXT  id=password     ${password}
    click element   css:.btn

getLessions
    [Arguments]   ${couraddr}
    ${eles}   get webelements    ${couraddr}
    ${lessons}  create list
    FOR   ${ele}    IN    @{eles}
    Append To List  ${lessons}   ${ele.text}
    END
    [Return]    ${lessons}
