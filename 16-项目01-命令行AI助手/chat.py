"""命令行多轮聊天逻辑。"""

from llm_client import ask_llm


def start_chat():
    """不断读取用户输入，直到用户主动退出。"""
    previous_response_id = None
    print("命令行AI助手已启动，输入exit或quit退出。")

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
            print("请输入内容。")
            continue

        try:
            answer, previous_response_id = ask_llm(
                user_text,
                previous_response_id=previous_response_id,
            )
            print(f"助手：{answer}")
        except Exception as e:
            # API错误不会让程序直接崩溃，用户仍然可以选择退出。
            print(f"调用失败：{e}")
