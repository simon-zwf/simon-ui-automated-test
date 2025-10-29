# ==================================================
# !/usr/bin/env python
# @Author: simon.zhang
# @Date: 2025/10/27 15:46
# @FileName: conftest.py.py
# @Email: wangfu_zhang@ggec.com.cn
# ==================================================

import pytest
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.app_config import AppConfig


@pytest.fixture(scope="function")
def app_driver():
    """创建Appium驱动 - 使用新版本API"""
    driver = None
    try:
        print("启动Appium驱动...")
        print(f"连接Appium服务器: {AppConfig.APPIUM_SERVER}")
        print(f"设备配置: {AppConfig.DESIRED_CAPS}")

        # 使用新版本的Options方式
        options = UiAutomator2Options()

        # 设置能力
        for key, value in AppConfig.DESIRED_CAPS.items():
            options.set_capability(key, value)

        # 创建驱动
        driver = webdriver.Remote(
            command_executor=AppConfig.APPIUM_SERVER,
            options=options
        )

        print("Appium驱动创建成功")
        yield driver

    except Exception as e:
        print(f"创建Appium驱动失败: {e}")
        raise
    finally:
        # 关闭驱动
        if driver:
            print("关闭Appium驱动")
            driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """测试报告钩子"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            driver = item.funcargs.get('app_driver')
            if driver:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="failure_screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
                print("失败截图已保存")
        except Exception as e:
            print(f"截图失败: {e}")