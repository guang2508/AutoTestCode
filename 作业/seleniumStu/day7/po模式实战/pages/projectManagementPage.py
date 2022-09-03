# -*- coding: utf-8 -*-
# @project : script
# @author  : lenovo
# @file     : projectManagementPage.py
# @ide     : PyCharm
# @time    : 2020/5/29 21:30
"""
项目管理页面
"""
from study.seleniumStu.day7.po模式实战.pages.basePage import BasePage


class ProjectManagementPage(BasePage):

    def __init__(self, path="/project/manage"):
        """
        考勤管理页面类
        """
        super().__init__()
        self.path = self.url + path

    def to_page(self):
        self.driver.get(self.path)
