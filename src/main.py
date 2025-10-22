from agent.model import ask
import asyncio
from dotenv import load_dotenv

load_dotenv()

async def run():
    print("MCP Agent (Ollama qwen3:30b) — type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            break
        reply = await ask(user_input, True)
        print(f"Agent: {reply}\n")


async def main():
    await run()

asyncio.run(main())