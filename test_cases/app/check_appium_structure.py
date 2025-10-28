# ==================================================
# !/usr/bin/env python
# @Author: simon.zhang
# @Date: 2025/10/28 08:21
# @FileName: check_appium_structure.py
# @Email: wangfu_zhang@ggec.com.cn
# ==================================================
# check_version.py
import appium

print(f"Appium Python Client 版本: {appium.__version__}")

# 根据版本选择不同的导入方式
if appium.__version__.startswith('2.'):
    print("✅ 使用 Appium 2.x 版本")
    from appium.options.android import UiAutomator2Options
    print("✅ UiAutomator2Options 导入成功")
else:
    print("ℹ️ 使用 Appium 1.x 版本")