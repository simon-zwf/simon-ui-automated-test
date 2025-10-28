# ==================================================
# !/usr/bin/env python
# @Author: simon.zhang
# @Date: 2025/10/27 15:47
# @FileName: run.py.py
# @Email: wangfu_zhang@ggec.com.cn
# ==================================================
# run_test.py
import subprocess
import sys


def run_test():
    """运行测试"""

    cmd = [
        "pytest",
        "test_cases/app/test_glasses.py",
        "-v",
        "-s",  # 显示print输出
        "--alluredir=reports/allure_results"
    ]

    print("🎯 开始执行测试...")
    print(f"执行命令: {' '.join(cmd)}")

    # 运行测试
    result = subprocess.run(cmd)

    # 生成报告
    if result.returncode == 0:
        subprocess.run([
            "allure", "generate",
            "reports/allure_results",
            "-o", "reports/html_report",
            "--clean"
        ])
        print("📊 测试报告生成完成")
        print("📁 报告位置: reports/html_report/index.html")
    else:
        print("❌ 测试执行失败")

    return result.returncode


if __name__ == "__main__":
    exit_code = run_test()
    sys.exit(exit_code)