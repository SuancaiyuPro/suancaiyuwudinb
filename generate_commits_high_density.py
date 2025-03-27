#!/usr/bin/env python3
"""
GitHub 贡献补刷脚本 - 高密度模式
从 2025-03-27 到 2026-03-18，每天随机生成 15~30 次 commit
"""

import subprocess
import random
import os
from datetime import date, timedelta

# 配置
START_DATE = date(2025, 3, 27)
END_DATE = date(2026, 3, 18)
REPO_DIR = "/home/ubuntu/suancaiyuwudinb"

# 提交消息列表
COMMIT_MESSAGES = [
    "Update README", "Fix typo", "Add notes", "Refactor code", "Improve documentation",
    "Minor changes", "Add feature", "Bug fix", "Code cleanup", "Update dependencies",
    "Add tests", "Optimize performance", "Fix issue", "Update config", "Add comments",
    "Remove unused code", "Improve structure", "Update logic", "Add utility functions",
    "Enhance readability", "Fix formatting", "Update styles", "Add examples",
    "Improve error handling", "Update workflow", "Refactor module", "Update assets",
    "Add validation", "Fix security issue", "Optimize database", "Update API",
    "Add localization", "Improve UI", "Fix cross-browser issues", "Update build script"
]

os.chdir(REPO_DIR)

# 清空旧的 log.txt 并重新初始化 git 仓库以确保干净的提交历史
subprocess.run(["rm", "-rf", ".git"], check=True)
subprocess.run(["git", "init"], check=True)
subprocess.run(["git", "config", "user.name", "SuancaiyuPro"], check=True)
subprocess.run(["git", "config", "user.email", "2389078986@qq.com"], check=True)

with open(os.path.join(REPO_DIR, "log.txt"), "w") as f:
    f.write("High density contribution log\n")

current_date = START_DATE
total_commits = 0

while current_date <= END_DATE:
    # 每天随机 15~30 次提交（高密度）
    num_commits = random.randint(15, 30)
    
    for i in range(num_commits):
        # 随机时间（7:00 ~ 23:59）
        hour = random.randint(7, 23)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        
        date_str = f"{current_date.strftime('%Y-%m-%d')}T{hour:02d}:{minute:02d}:{second:02d}"
        
        # 修改文件内容
        with open(os.path.join(REPO_DIR, "log.txt"), "a") as f:
            f.write(f"{date_str} - high density commit {i+1}\n")
        
        msg = random.choice(COMMIT_MESSAGES)
        
        # 设置 commit 时间并提交
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
        
        subprocess.run(["git", "add", "log.txt"], check=True)
        subprocess.run(
            ["git", "commit", "-m", msg],
            env=env,
            check=True,
            capture_output=True
        )
        total_commits += 1
    
    if current_date.day % 30 == 0 or current_date == END_DATE:
        print(f"进度: {current_date} | 已生成 {total_commits} 个高密度 commit")
    
    current_date += timedelta(days=1)

print(f"\n✅ 完成！共生成 {total_commits} 个高密度历史 commit")
