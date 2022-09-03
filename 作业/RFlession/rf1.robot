*** Settings ***
Library  SeleniumLibrary
*** Test Cases ***
测试1：
    open browser  http://www.baidu.com  chrome
    set selenium implicit wait  10
    input text  id=kw   松勤\n
    ${var}  get text    id=1
    should contain  ${var}  松勤网     #判断前者中是否包含后者
    close browser