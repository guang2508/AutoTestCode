*** Settings ***
Library  SeleniumLibrary    #����SeleniumLivrary��
*** Test Cases ***
case1
    open browser  http://localhost:82/mgr/login/login.html   chrome     #��chrome�������������ַ
    set selenium implicit wait  10
    input text   id=username    auto        #��id��λ��������auto
    input text   id=password    sdfsdfsdf
    click element  css=.btn-success     #��css��λ�������
    click element  css=[ng-click="showAddOne=true"]
    input text  css=[ng-model="addData.name"]   robot       #��css��λ��������robot
    input text  css=[ng-model="addData.desc"]   RF���
    input text  css=[ng-model="addData.display_idx"]    1
    click element  css=[ng-click="addOne()"]
    close browser    #�ر������