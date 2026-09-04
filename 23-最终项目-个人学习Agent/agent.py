"""Agent 协调 LLM、Memory、RAG、本地 Tool 和可选 MCP Tool。"""

import json

from config import ENABLE_MCP, MAX_STEPS, MCP_SERVER_PATH
from llm_client import create_response
from memory import add_conversation, memory_context
from tools import TOOL_SCHEMAS, execute_local_tool


INSTRUCTIONS = "你是个人学习助手。需要学习知识时使用 search_knowledge，需要计算时使用 calculate，需要记忆时使用 Memory 工具。不要编造工具结果。"


async def run_agent(user_text):
    if not isinstance(user_text, str) or not user_text.strip():
        raise ValueError("用户问题不能为空。")
    add_conversation("user", user_text)
    local_schemas = list(TOOL_SCHEMAS)
    mcp_calls = {}
    mcp_client = None
    if ENABLE_MCP:
        from mcp_client import load_mcp_tools
        mcp_schemas, mcp_calls, mcp_client = await load_mcp_tools(MCP_SERVER_PATH)
        local_schemas.extend(mcp_schemas)

    input_data = [{"role": "user", "content": f"Memory Context：{memory_context()}\n用户问题：{user_text}"}]
    response = None
    try:
        for _ in range(MAX_STEPS):
            response = create_response(input_data, INSTRUCTIONS, local_schemas, getattr(response, "id", None))
            calls = [item for item in response.output if getattr(item, "type", None) == "function_call"]
            if not calls:
                add_conversation("assistant", response.output_text)
                return response.output_text
            outputs = []
            for call in calls:
                try:
                    arguments = json.loads(call.arguments)
                    if call.name in mcp_calls:
                        result = json.dumps({"result": await mcp_calls[call.name](call.name, arguments)}, ensure_ascii=False)
                    else:
                        result = execute_local_tool(call.name, arguments)
                except (TypeError, ValueError, json.JSONDecodeError) as error:
                    result = json.dumps({"error": str(error)}, ensure_ascii=False)
                outputs.append({"type": "function_call_output", "call_id": call.call_id, "output": result})
            input_data = outputs
    finally:
        if mcp_client is not None:
            from mcp_client import close_mcp_client
            await close_mcp_client(mcp_client)
    raise RuntimeError("Agent 超过最大工具调用步数。")
