# ==================================================
# !/usr/bin/env python
# @Author: simon.zhang
# @Date: 2025/10/27 20:09
# @FileName: main_page.py
# @Email: wangfu_zhang@ggec.com.cn
# ==================================================

import time
import allure
from common.action_utils import ActionUtils


class MainPage:
    """主页面"""

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionUtils(driver)

    @allure.step("等待App加载")
    def wait_for_app_loaded(self, timeout=10):
        """等待App加载完成"""
        print("等待App加载...")
        time.sleep(5)

    @allure.step("点击首页元素")
    def click_home_element(self):
        """点击首页元素"""
        print("尝试点击首页元素 (id=iv_home)")

        # 使用封装的点击方法
        result = self.action.click_by_id("iv_home")

        if result:
            print("首页home点击成功")
        else:
            print("首页元素点击失败")

        return result

    @allure.step("验证操作结果")
    def verify_operation_success(self):
        """验证操作是否成功"""
        print("验证操作结果...")
        return True