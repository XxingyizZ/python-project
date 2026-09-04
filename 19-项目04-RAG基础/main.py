"""RAG命令行程序入口。"""

from rag import answer_question


def main():
    """读取问题并输出RAG回答。"""
    print("RAG学习助手已启动，输入exit或quit退出。")

    while True:
        try:
            question = input("问题：").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n程序结束。")
            break

        if question.lower() in {"exit", "quit"}:
            print("程序结束。")
            break
        if not question:
            print("请输入问题。")
            continue

        try:
            print(f"回答：{answer_question(question)}")
        except Exception as e:
            print(f"处理失败：{e}")


if __name__ == "__main__":
    main()
