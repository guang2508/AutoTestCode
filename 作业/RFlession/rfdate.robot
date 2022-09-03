*** Test Cases ***
case1
    [Template]   dataDriven
    #不写关键字，只能写关键字的参数,不能写其他的
    20200100
    20200200
    20200300

*** Keywords ***
dataDriven
    [Arguments]   ${date}
    ${res}   evaluate   ${date}+1
    log to console    ${res}