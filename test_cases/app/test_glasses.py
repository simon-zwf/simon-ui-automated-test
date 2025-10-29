# ==================================================
# !/usr/bin/env python
# @Author: simon.zhang
# @Date: 2025/10/27 20:08
# @FileName: test_glasses.py
# @Email: wangfu_zhang@ggec.com.cn
# ==================================================

import pytest
import allure
import time
from page_objects.app.main_page import MainPage


@allure.feature("眼镜App测试")
class TestGlassesApp:
    """眼镜App测试用例"""

    @allure.story("打开App并点击首页")
    @allure.title("测试首页点击功能")
    def test_click_home_element(self, app_driver):
        """
        测试步骤：
        1. 打开指定App
        2. 等待App加载
        3. 点击首页元素(id=home)
        """
        # 初始化页面对象
        main_page = MainPage(app_driver)

        with allure.step("打开App并等待加载"):
            main_page.wait_for_app_loaded()
            print(" App打开成功")

        with allure.step("点击首页元素"):
            result = main_page.click_home_element()
            assert result, "点击首页元素失败"

        with allure.step("验证操作结果"):
            time.sleep(2)  # 等待页面响应
            verification_result = main_page.verify_operation_success()
            assert verification_result, "操作验证失败"

        print("测试用例执行完成！")