# ==================================================
# !/usr/bin/env python
# @Author: simon.zhang
# @Date: 2025/10/27 19:57
# @FileName: app_config.py
# @Email: wangfu_zhang@ggec.com.cn
# ==================================================

# config/app_config.py
class AppConfig:
    """App配置"""

    # Appium 服务器地址
    APPIUM_SERVER = "http://127.0.0.1:4723/wd/hub"

    # 设备配置 - 使用新版本的格式
    DESIRED_CAPS = {
        "platformName": "Android",
        "appium:platformVersion": "15",
        "appium:deviceName": "11467253AU000413",
        "appium:appPackage": "com.example.besglasses",
        "appium:appActivity": "com.example.besglasses.ui.HomeActivity",
        "appium:automationName": "UiAutomator2",
        "appium:noReset": True
    }