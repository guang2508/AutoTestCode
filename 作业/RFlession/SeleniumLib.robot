*** Settings ***
Library  SeleniumLibrary    #导入SeleniumLivrary库
*** Test Cases ***
case1
    open browser  http://localhost:82/mgr/login/login.html   chrome     #打开chrome浏览器并进入网址
    set selenium implicit wait  10
    input text   id=username    auto        #用id定位，并输入auto
    input text   id=password    sdfsdfsdf
    click element  css=.btn-success     #用css定位，并点击
    click element  css=[ng-click="showAddOne=true"]
    input text  css=[ng-model="addData.name"]   robot       #用css定位，并输入robot
    input text  css=[ng-model="addData.desc"]   RF框架
    input text  css=[ng-model="addData.display_idx"]    1
    click element  css=[ng-click="addOne()"]
    close browser    #关闭浏览器