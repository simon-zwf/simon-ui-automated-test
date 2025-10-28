# ==================================================
# !/usr/bin/env python
# @Author: simon.zhang
# @Date: 2025/10/27 20:02
# @FileName: action_utils.py
# @Email: wangfu_zhang@ggec.com.cn
# ==================================================

import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotInteractableException
from common.element_finder import ElementFinder


class ActionUtils:
    """操作工具类"""

    def __init__(self, driver):
        self.driver = driver
        self.element_finder = ElementFinder(driver)

    def click_element(self, locator_type, locator_value, max_retries=2):
        """点击元素"""
        for attempt in range(max_retries):
            try:
                element = self.element_finder.find_element(locator_type, locator_value)
                element.click()
                print(f"✅ 成功点击元素: {locator_type}='{locator_value}'")
                time.sleep(1)
                return True
            except ElementNotInteractableException:
                if attempt < max_retries - 1:
                    print(f"⚠️ 元素不可点击，重试 {attempt + 1}/{max_retries}")
                    time.sleep(2)
                else:
                    print(f"❌ 元素无法点击: {locator_type}='{locator_value}'")
                    raise
            except Exception as e:
                print(f"❌ 点击元素失败: {e}")
                if attempt == max_retries - 1:
                    raise

    def click_by_id(self, element_id, max_retries=2):
        """通过ID点击元素"""
        return self.click_element("id", element_id, max_retries)

    def click_by_xpath(self, xpath, max_retries=2):
        """通过XPath点击元素"""
        return self.click_element("xpath", xpath, max_retries)

    def input_text(self, locator_type, locator_value, text, clear_first=True):
        """输入文本"""
        try:
            element = self.element_finder.find_element(locator_type, locator_value)

            if clear_first:
                element.clear()

            element.send_keys(text)
            print(f"✅ 成功输入文本: '{text}' 到元素 {locator_type}='{locator_value}'")
            return True
        except Exception as e:
            print(f"❌ 输入文本失败: {e}")
            raise

    def swipe_up(self, duration=1000):
        """向上滑动"""
        screen_size = self.driver.get_window_size()
        start_x = screen_size['width'] * 0.5
        start_y = screen_size['height'] * 0.8
        end_y = screen_size['height'] * 0.2

        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
        print("✅ 向上滑动完成")
        time.sleep(1)

    def swipe_down(self, duration=1000):
        """向下滑动"""
        screen_size = self.driver.get_window_size()
        start_x = screen_size['width'] * 0.5
        start_y = screen_size['height'] * 0.2
        end_y = screen_size['height'] * 0.8

        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
        print("✅ 向下滑动完成")
        time.sleep(1)