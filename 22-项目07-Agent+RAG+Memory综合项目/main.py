"""综合 Agent 的命令行入口。"""

from agent import run_agent


def main():
    """读取用户输入并运行多轮 Agent。"""
    print("Agent 已启动，输入 exit 或 quit 退出。")
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
            print(f"助手：{run_agent(user_text)}")
        except Exception as error:
            print(f"运行失败：{error}")


if __name__ == "__main__":
    main()
