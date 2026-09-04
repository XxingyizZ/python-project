"""个人学习 Agent 的命令行入口。"""

import asyncio

from agent import run_agent


def main():
    print("个人学习 Agent 已启动，输入 exit 或 quit 退出。")
    while True:
        try:
            user_text = input("你：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n程序结束。")
            break
        if user_text.lower() in {"exit", "quit"}:
            print("程序结束。")
            break
        if not user_text:
            print("请输入问题。")
            continue
        try:
            print(f"助手：{asyncio.run(run_agent(user_text))}")
        except Exception as error:
            print(f"运行失败：{error}")


if __name__ == "__main__":
    main()
