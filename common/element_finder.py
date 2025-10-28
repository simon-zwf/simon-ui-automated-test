# ==================================================
# !/usr/bin/env python
# @Author: simon.zhang
# @Date: 2025/10/27 19:59
# @FileName: element_finder.py
# @Email: wangfu_zhang@ggec.com.cn
# ==================================================

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class ElementFinder:
    """元素查找器 - 使用 AppiumBy"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_by_id(self, element_id):
        """通过ID定位元素"""
        try:
            locator = (AppiumBy.ID, element_id)
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise NoSuchElementException(f"未找到ID为 '{element_id}' 的元素")

    def find_by_xpath(self, xpath):
        """通过XPath定位元素"""
        try:
            locator = (AppiumBy.XPATH, xpath)
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise NoSuchElementException(f"未找到XPath为 '{xpath}' 的元素")

    def find_by_class(self, class_name):
        """通过Class Name定位元素"""
        try:
            locator = (AppiumBy.CLASS_NAME, class_name)
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise NoSuchElementException(f"未找到Class为 '{class_name}' 的元素")

    def find_by_accessibility_id(self, accessibility_id):
        """通过Accessibility ID定位元素"""
        try:
            locator = (AppiumBy.ACCESSIBILITY_ID, accessibility_id)
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise NoSuchElementException(f"未找到Accessibility ID为 '{accessibility_id}' 的元素")

    def find_by_ui_automator(self, uiautomator_text):
        """通过UI Automator定位元素"""
        try:
            locator = (AppiumBy.ANDROID_UIAUTOMATOR, uiautomator_text)
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise NoSuchElementException(f"UI Automator定位失败: '{uiautomator_text}'")

    def find_element(self, locator_type, locator_value):
        """通用元素定位方法"""
        locator_map = {
            "id": AppiumBy.ID,
            "xpath": AppiumBy.XPATH,
            "class": AppiumBy.CLASS_NAME,
            "accessibility_id": AppiumBy.ACCESSIBILITY_ID,
            "uiautomator": AppiumBy.ANDROID_UIAUTOMATOR
        }

        if locator_type not in locator_map:
            raise ValueError(f"不支持的定位类型: {locator_type}")

        try:
            return self.wait.until(
                EC.element_to_be_clickable((locator_map[locator_type], locator_value))
            )
        except TimeoutException:
            raise NoSuchElementException(f"未找到元素: {locator_type}='{locator_value}'")