#!/usr/bin/env python3
"""
GitHub 贡献补刷脚本 - 精细化模式
1. 每日 1~8 个 commit
2. 每 2~3 天设置一个空白天
"""

import subprocess
import random
import os
from datetime import date, timedelta

# 配置
START_DATE = date(2025, 3, 27)
END_DATE = date(2026, 6, 12)
REPO_DIR = "/home/ubuntu/suancaiyuwudinb"

# 提交消息列表
COMMIT_MESSAGES = [
    "Update README", "Fix typo", "Add notes", "Refactor code", "Improve documentation",
    "Minor changes", "Add feature", "Bug fix", "Code cleanup", "Update dependencies",
    "Add tests", "Optimize performance", "Fix issue", "Update config", "Add comments",
    "Remove unused code", "Improve structure", "Update logic", "Add utility functions",
    "Enhance readability", "Fix formatting", "Update styles", "Add examples",
    "Improve error handling", "Update workflow", "docs: enhance README", "feat: add core utils"
]

os.chdir(REPO_DIR)

# 重新初始化 git 仓库
subprocess.run(["rm", "-rf", ".git"], check=True)
subprocess.run(["git", "init"], check=True)
subprocess.run(["git", "config", "user.name", "SuancaiyuPro"], check=True)
subprocess.run(["git", "config", "user.email", "2389078986@qq.com"], check=True)

current_date = START_DATE
total_commits = 0
days_since_last_gap = 0
gap_interval = random.randint(2, 3)

while current_date <= END_DATE:
    # 检查是否到了空白天
    if days_since_last_gap >= gap_interval:
        days_since_last_gap = 0
        gap_interval = random.randint(2, 3)
        current_date += timedelta(days=1)
        continue
        
    # 每日随机 1~8 次提交
    num_commits = random.randint(1, 8)
    
    for i in range(num_commits):
        hour = random.randint(9, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        date_str = f"{current_date.strftime('%Y-%m-%d')}T{hour:02d}:{minute:02d}:{second:02d}"
        
        with open(os.path.join(REPO_DIR, "activity.log"), "a") as f:
            f.write(f"{date_str} - activity {i+1}\n")
        
        msg = random.choice(COMMIT_MESSAGES)
        
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = date_str
        env["GIT_COMMITTER_DATE"] = date_str
        
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(
            ["git", "commit", "-m", msg],
            env=env,
            check=True,
            capture_output=True
        )
        total_commits += 1
    
    days_since_last_gap += 1
    current_date += timedelta(days=1)

print(f"\n✅ 完成！共生成 {total_commits} 个精细化历史 commit")
