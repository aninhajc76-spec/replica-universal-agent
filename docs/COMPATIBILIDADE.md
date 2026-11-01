# Matriz de compatibilidade

| Ambiente | Arquivo de entrada | Como funciona |
| --- | --- | --- |
| Codex/AGENTS.md-compatible | `AGENTS.md` | Contexto por repositório, se suportado |
| Claude Code | `CLAUDE.md` e `.claude-plugin/plugin.json` | Contexto e pacote de skills |
| Gemini CLI | `GEMINI.md` | Contexto por projeto |
| GitHub Copilot | `.github/copilot-instructions.md` | Instruções do repositório |
| Cursor | `.cursor/rules/replica.mdc` | Regra de projeto |
| ChatGPT em conversa | `PROMPT_UNIVERSAL.md` | Colar prompt; anexar módulos se preciso |
| Claude/Gemini/LLMs em chat | `PROMPT_UNIVERSAL.md` | Colar prompt; anexar módulos se preciso |
| Modelos locais (Ollama etc.) | `PROMPT_UNIVERSAL.md` | Usar como mensagem de sistema, quando permitido |

**Limitação:** os comandos `/replica-...` são *nomes de fases*, não comandos
nativos garantidos em todo assistente. Para que a fase funcione, o sistema
precisa carregar o arquivo Markdown apropriado ou receber seu texto.

O repositório não exige conta, login, API ou execução de rede para os scripts
locais. Para geração automática de código, um assistente/LLM deve ser usado
separadamente. Acesso à internet, execução de testes, leitura de arquivos e
publicação dependem das ferramentas autorizadas em cada plataforma.

**Fontes de formatos:**
- AGENTS.md: https://agents.md/
- GitHub Copilot: https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/customize-copilot/configure-custom-instructions/add-repository-instructions-in-your-ide
- Cursor: https://docs.cursor.com/context/rules-for-ai
- Gemini CLI: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md
- Codex: https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide
