from agent.model import ask

def run():
    print("MCP Agent (Ollama gpt-oss) — type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break
        reply = ask(user_input)
        print(f"Agent: {reply}\n")


if __name__ == "__main__":
    run()