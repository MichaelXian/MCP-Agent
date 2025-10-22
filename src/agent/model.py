from dolphin_mcp import run_interaction

async def ask(message, debug=False):
    result = await run_interaction(
        user_query=message,
        model_name="gpt-oss",
        quiet_mode=not debug,
        log_messages_path="./logs.txt"
    )
    return result