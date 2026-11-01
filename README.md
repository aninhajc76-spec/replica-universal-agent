# Replica Universal Agent / Agente Replica Universal

**11 módulos de engenharia de software, independentes de um único fornecedor de IA.**
Um repositório público de instruções e ferramentas para estudar funcionalidades
públicas e criar aplicações **originais**. Português como idioma principal.

> **O que este repositório oferece:** metodologia, instruções portáveis,
> scripts Python locais, testes e uma página estática de apresentação.
> **O que não oferece:** um modelo de IA hospedado, uma API de inferência,
> acesso automático a terceiros ou garantia de uso sem adaptação em toda IA.

## Comece em 30 segundos

**ChatGPT, Claude, Gemini, Llama, Mistral ou qualquer chat que aceite texto:**
abra [PROMPT_UNIVERSAL.md](PROMPT_UNIVERSAL.md), copie o conteúdo e complete
`Meu pedido`. Se o assistente permitir anexar arquivos, envie `AGENTS.md` e
as skills relevantes. Para uso persistente, adicione as instruções aos
projetos/agentes personalizados do respectivo serviço.

**IA que trabalha dentro do repositório:**
- **Codex e agentes compatíveis com AGENTS.md:** leia automaticamente `AGENTS.md`
  quando seu ambiente oferecer esse suporte.
- **Claude Code:** `CLAUDE.md` e a distribuição em `skills/`; a configuração
  `.claude-plugin/plugin.json` permite adaptar ao ecossistema Claude.
- **Gemini CLI:** `GEMINI.md`.
- **GitHub Copilot:** `.github/copilot-instructions.md`.
- **Cursor:** `.cursor/rules/replica.mdc` (ou `AGENTS.md`).
- **Outras IAs:** cole o prompt universal e forneça as skills da fase.

> Compatibilidade significa **instruções portáveis**, não execução automática
> do mesmo conjunto de ferramentas em todos os provedores.

## 11 fases

| Comando | Função |
| --- | --- |
| `/replica-recon` | Mapear telas, tarefas, fluxos, estados e fontes públicas |
| `/replica-architect` | Planejar stack, banco, segurança e APIs |
| `/replica-design` | Criar tokens, componentes e visual próprios |
| `/replica-build` | Implementar funcionalidades originais |
| `/replica-backend` | Construir autenticação, banco e integrações autorizadas |
| `/replica-test` | Testar fluxos, casos extremos e erros |
| `/replica-diff` | Medir diferenças e paridade funcional |
| `/replica-entrepreneur` | Analisar oportunidades com fontes verificáveis |
| `/replica-brand` | Criar identidade original e verificar heranças |
| `/replica-launch` | Preparar lançamento e comunicação |
| `/replica-deploy` | Verificar requisitos e publicar com autorização |

### Ferramenta Python local (sem dependências externas)

```bash
python3 replica.py list
python3 replica.py prompt recon
python3 replica.py prompt design --output meu_prompt.txt
python3 replica.py init /caminho/do/meu-projeto
python3 replica.py check
python3 -m unittest discover -s tests -v
```

Os seis utilitários originais estão em `skills/replica-*/` e podem ser
executados com Python 3.8+; por exemplo:

```bash
python3 skills/replica-diff/parity.py replica/features.csv
python3 skills/replica-design/contrast.py replica/design/tokens.json
```

## Publicar no GitHub

1. Descompacte o ZIP **mantendo todos os arquivos, inclusive `.github/` e `.cursor/`**.
2. Crie um repositório público chamado `replica-universal-agent` no GitHub.
3. Envie os arquivos da pasta extraída para a **raiz** do repositório.
4. Opcionalmente ative **Settings → Pages → Deploy from a branch → main /docs**.
5. O GitHub publica os arquivos e o site de documentação; **não executa IA**.

Para um bot acessível por URL, seria necessário um serviço de backend e uma API
de modelo, com autenticação, gastos e segurança configurados à parte.

Mais detalhes: [docs/INSTALACAO.md](docs/INSTALACAO.md) e
[docs/COMPATIBILIDADE.md](docs/COMPATIBILIDADE.md).

## Licença e atribuição

Distribuição derivada do projeto [Replica Skill de Jake Schincariol](https://github.com/Jakeschincariol/replica-skill), sob licença MIT.
O texto original da licença e seu copyright foram mantidos em [LICENSE](LICENSE).
Veja [NOTICE.md](NOTICE.md). Esta adaptação não é oficial.

---

**English quick start:** Copy [PROMPT_UNIVERSAL.md](PROMPT_UNIVERSAL.md) into any
text-based AI assistant; repo-integrated assistants can read the relevant
adapter (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, Copilot, Cursor). The repository
provides **portable instructions**, not a hosted AI service. Source is MIT,
with upstream credit in [NOTICE.md](NOTICE.md).
