## Prerequisites

- Install [Ollama](https://ollama.ai)
- Pull the model:
  ```bash
  ollama pull gpt-oss
  
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