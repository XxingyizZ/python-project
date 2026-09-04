"""Function Tool Agent的命令行入口。"""

from agent import run_agent


def main():
    """读取用户任务并运行Agent。"""
    print("Function Tool Agent已启动，输入exit或quit退出。")

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
            print("请输入任务。")
            continue

        try:
            answer = run_agent(user_text)
            print(f"助手：{answer}")
        except Exception as e:
            print(f"Agent运行失败：{e}")


if __name__ == "__main__":
    main()
