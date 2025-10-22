from agent.model import ask
import asyncio


async def run():
    print("MCP Agent (Ollama gpt-oss) — type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            break
        reply = await ask(user_input, True)
        print(f"Agent: {reply}\n")


async def main():
    await run()

asyncio.run(main())