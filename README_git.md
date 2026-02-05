# 🚀 Guia: Salvando seu Projeto Python no GitHub

> Conversa com o Gemini sobre como fazer deploy do seu projeto Python no GitHub

![GitHub](https://img.shields.io/badge/GitHub-Workflow-blue?style=flat-square)
![Git](https://img.shields.io/badge/Git-Guide-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-Project-green?style=flat-square)

## ❓ A Pergunta

> Como faço para salvar meu projeto python no github? Já tenho as CLI do git e do github instalados na máquina.

## ✅ A Resposta

Ótima escolha em usar a CLI do GitHub (`gh`), ela facilita muito o processo! Como você já tem tudo instalado, o caminho é bem direto.

Aqui está o passo a passo para transformar sua pasta local em um repositório no GitHub:

---

## 1️⃣ Autenticação

Antes de tudo, certifique-se de que sua conta do GitHub está conectada no terminal:

```bash
gh auth login
```

💡 **Siga as instruções na tela:**
- Escolha `GitHub.com`
- Escolha `HTTPS`
- Escolha `Login with a web browser`

---

## 2️⃣ Prepare o Terreno - O Arquivo `.gitignore`

Em projetos Python, é fundamental não enviar lixo para o servidor (como ambientes virtuais e pastas de cache). Crie um arquivo `.gitignore` na raiz do projeto e adicione:

```plaintext
__pycache__/
venv/
.env
*.pyc
```

💡 **Dica:** Se quiser um arquivo completo, use:

```bash
gh gitignore python > .gitignore
```

---

## 3️⃣ Ciclo de Vida do Git

Agora, vamos preparar os arquivos localmente. Execute os comandos **na ordem**:

### Passo a Passo:

| Ordem | Comando | Descrição |
|-------|---------|-----------|
| 1️⃣ | `git init` | Iniciar o repositório Git |
| 2️⃣ | `git add .` | Adicionar todos os arquivos |
| 3️⃣ | `git commit -m "Initial commit"` | Fazer o primeiro commit |

```bash
git init
git add .
git commit -m "Initial commit"
```

---

## 4️⃣ Criar o Repositório no GitHub e Enviar

Agora vem a mágica da GitHub CLI! Você não precisa ir ao site para criar o repositório:

```bash
gh repo create
```

### Menu Interativo - O que Selecionar:

| Pergunta | Resposta | Nota |
|----------|----------|------|
| **What would you like to do?** | `Push an existing local repository to GitHub` | Já tem código local |
| **Path to local repository:** | `.` | Pressione Enter (pasta atual) |
| **Repository name:** | `seu-projeto` | Nome do seu projeto |
| **Visibility:** | `Public` ou `Private` | Você escolhe |
| **Add a remote?** | `Yes` | Para conectar com GitHub |
| **What should the new remote be called?** | `origin` | Nome padrão |
| **Would you like to push commits?** | `Yes` | Enviar para GitHub agora |

---

## 🎯 Resumo Visual do Fluxo

```
Local Repository          GitHub
     ↓                        ↓
  git init           ──→  gh repo create
  git add .          ──→  Criar repositório
  git commit -m "..."  ──→  (automático)
  (automático)        ──→  Push! 🎉
```

---

## ✨ Pronto!

Seu projeto está no GitHub! 🚀

### Próximas Vezes:

Para fazer alterações e enviar:

```bash
git add .
git commit -m "Sua mensagem aqui"
git push
```

---

<div align="center">

**[⬆ voltar ao topo](#-guia-salvando-seu-projeto-python-no-github)**

</div>