"""MCP 基础项目的程序入口。"""

import asyncio

from client import run_client


def main():
    """运行 MCP Client 示例。"""
    try:
        asyncio.run(run_client())
    except KeyboardInterrupt:
        print("程序结束。")
    except Exception as error:
        print(f"MCP 运行失败：{error}")


if __name__ == "__main__":
    main()
