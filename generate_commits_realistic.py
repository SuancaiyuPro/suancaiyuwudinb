#!/usr/bin/env python3
"""
GitHub 贡献补刷脚本 - 真实模式
1. 增加 20% 的空白天（无贡献）
2. 模拟真实的代码提交过程
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
    "Initial project structure",
    "Add core utility functions",
    "Implement API client class",
    "Update README with usage examples",
    "Fix minor bug in request handling",
    "Add type hints to utilities",
    "Optimize session management",
    "Add pyproject.toml for packaging",
    "Refactor error handling logic",
    "Update dependencies in pyproject.toml",
    "Add docstrings to main classes",
    "Improve timestamp formatting",
    "Add unit tests for API client",
    "Fix linting issues",
    "Update documentation",
    "Prepare for v1.0.0 release"
]

os.chdir(REPO_DIR)

# 重新初始化 git 仓库
subprocess.run(["rm", "-rf", ".git"], check=True)
subprocess.run(["git", "init"], check=True)
subprocess.run(["git", "config", "user.name", "SuancaiyuPro"], check=True)
subprocess.run(["git", "config", "user.email", "2389078986@qq.com"], check=True)

current_date = START_DATE
total_commits = 0

while current_date <= END_DATE:
    # 20% 的概率这一天没有贡献
    if random.random() < 0.20:
        current_date += timedelta(days=1)
        continue
        
    # 每天随机 1~6 次提交
    num_commits = random.randint(1, 6)
    
    # 周末提交更少
    if current_date.weekday() >= 5:
        num_commits = random.randint(0, 2)
        if num_commits == 0:
            current_date += timedelta(days=1)
            continue
    
    for i in range(num_commits):
        hour = random.randint(9, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        date_str = f"{current_date.strftime('%Y-%m-%d')}T{hour:02d}:{minute:02d}:{second:02d}"
        
        # 模拟修改文件
        with open(os.path.join(REPO_DIR, "activity.log"), "a") as f:
            f.write(f"{date_str} - development activity {i+1}\n")
        
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
    
    current_date += timedelta(days=1)

print(f"\n✅ 完成！共生成 {total_commits} 个真实感历史 commit")
