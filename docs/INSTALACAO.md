# Instalação e publicação do Agente Replica Universal

## 1. Sem instalar nada (qualquer IA com campo de texto)

Copie [o prompt universal](../PROMPT_UNIVERSAL.md), substitua `[DESCREVA AQUI...]`
pelo seu pedido e envie ao assistente. Para tarefas complexas, também forneça
`AGENTS.md` e a `SKILL.md` de cada fase. Se não existir upload, cole os textos.

## 2. Em projetos de agentes de programação

Deixe o repositório aberto no ambiente de desenvolvimento. Os pontos de entrada
são `AGENTS.md` (agentes compatíveis), `CLAUDE.md`, `GEMINI.md`,
`.github/copilot-instructions.md` e `.cursor/rules/replica.mdc`. Os arquivos
explicam onde encontrar as 11 skills em `skills/`.

Cada fornecedor tem seus próprios recursos de autorização, execução e carregamento
de arquivos. Alguns ambientes exigem copiar `SKILL.md` manualmente ou adicionar
instruções à configuração do projeto.

## 3. Na linha de comando

É necessário Python 3.8 ou superior. **Não há dependências externas** para
`replica.py` nem para as ferramentas originais do pacote.

```sh
python3 replica.py list
python3 replica.py prompt recon --output prompt.txt
python3 replica.py init ./meu-app
python3 replica.py check
```

O comando `init` cria apenas novos documentos de projeto em `meu-app/replica/`;
se houver arquivos com os mesmos nomes, **não os sobrescreve**.

## 4. Hospedagem pública com GitHub

1. Entre em https://github.com e crie um repositório **público** com nome
   `replica-universal-agent` (ou outro, se desejar).
2. Descompacte `Replica_Universal_GitHub_PRONTO.zip`.
3. Envie o **conteúdo interno** de `replica-universal-agent/`, não só o ZIP.
4. Confira que `README.md`, `AGENTS.md`, `LICENSE`, `skills/` e as pastas ocultas
   `.github/`, `.cursor/` estão na raiz.
5. Em GitHub → Actions, observe a execução automática dos testes após o push,
   se os workflows do repositório estiverem habilitados.
6. Opcional: Settings → Pages → Deploy from a branch → `main` → `/docs`.
   Isso publica o site estático de apresentação em `docs/index.html`.

**Atenção:** páginas do GitHub são estáticas. Hospedar arquivos no GitHub
não hospeda modelos de IA nem permite executar o agente remotamente.

## 5. Segurança e licença

Não faça commit de `.env`, tokens, senhas, segredos ou dados pessoais.
O código e as instruções do projeto original são MIT e exigem manter a
atribuição e o texto de licença. Leia `LICENSE` e `NOTICE.md`.

## Problemas comuns

- IA não lê a skill: cole o conteúdo do módulo ou anexe o arquivo.
- IA não tem execução de código: os comandos serão apenas recomendações.
- GitHub Pages não aparece: confira repositório, branch e pasta `/docs`.
- Testes locais: `python3 -m unittest discover -s tests -v`.
