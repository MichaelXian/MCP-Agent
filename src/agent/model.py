from ollama import chat
from ollama import ChatResponse

def ask(message, debug=False):
    response: ChatResponse = chat(model='gpt-oss', messages=[
        {
            'role': 'user',
            'content': message,
        },
    ], think=debug)
    return response.message.content