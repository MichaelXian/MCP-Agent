## Prerequisites

- Install [Ollama](https://ollama.ai)
- Pull the model:
  ```bash
  ollama pull qwen3:30b
  ```
If you want to use a different model, change the mcp_config accordingly

Add environment variables to the .env file, as shown in .env.example

- Install all npm packages globally so server startup does not timeout
```bash
npm i -g \
  @modelcontextprotocol/server-filesystem \
  brave-search-mcp \
  puppeteer-mcp-server \
  @notionhq/notion-mcp-server \
  @modelcontextprotocol/server-sequential-thinking
```

- Install Python/Docker



# Debugging
If you can't find the logs from the Dolphin MCP client, temporarily replace the logger in it's client.py with the following to log to file:
```python
class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def _write(self, level, msg):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"[{level}] {msg}\n") 

    def info(self, msg):
        self._write("INFO", msg)

    def warning(self, msg):
        self._write("WARNING", msg)

    def error(self, msg):
        self._write("ERROR", msg)

    def debug(self, msg):
        self._write("DEBUG", msg)

logger = FileLogger("mcp_log.txt")
```