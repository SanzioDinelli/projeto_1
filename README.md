# 📁 Projeto 1 - Gerador de Pastas

> Um utilitário Python para criar múltiplas pastas de projeto de forma rápida e eficiente.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

## 📋 Descrição

Este projeto fornece uma ferramenta simples e intuitiva para gerar múltiplas pastas de projeto na pasta pai do diretório atual. Ideal para criar estruturas de projetos rapidamente sem ter que criar cada pasta manualmente.

## ✨ Características

- ✅ Criação em massa de pastas de projeto
- ✅ Parâmetros configuráveis via linha de comando
- ✅ Nomenclatura automática e organizada
- ✅ Evita duplicação de pastas existentes
- ✅ Feedback visual do processo

## 🚀 Como Usar

### Instalação

Nenhuma dependência externa necessária! O script usa apenas bibliotecas padrão do Python.

```bash
# Clone ou copie o repositório
cd projeto_1
```

### Uso Básico

Criar 5 projetos (padrão):
```bash
python main.py
```

### Com Parâmetros

Criar um número específico de projetos:
```bash
# Forma abreviada
python main.py -n 10

# Forma completa
python main.py --num-projects 10
```

## 📊 Exemplos de Saída

```
✓ Pasta criada: C:\Users\seu_usuario\dev\projetos\projeto_2
✓ Pasta criada: C:\Users\seu_usuario\dev\projetos\projeto_3
✓ Pasta criada: C:\Users\seu_usuario\dev\projetos\projeto_4
✓ Pasta criada: C:\Users\seu_usuario\dev\projetos\projeto_5
✓ Pasta criada: C:\Users\seu_usuario\dev\projetos\projeto_6

Todas as pastas foram criadas com sucesso!
```

## 🔧 Parâmetros

| Parâmetro | Forma Longa | Tipo | Padrão | Descrição |
|-----------|-------------|------|--------|-----------|
| `-n` | `--num-projects` | int | 5 | Número de projetos a criar |

## 📁 Estrutura do Projeto

```
projeto_1/
├── main.py
├── pyproject.toml
└── README.md
```

## 💡 Exemplos de Uso Avançado

Criar 20 projetos:
```bash
python main.py -n 20
```

Criar apenas 1 projeto:
```bash
python main.py -n 1
```

## 🤝 Contribuições

Sinta-se à vontade para fazer fork, create issues e enviar pull requests!

## 📝 Licença

Este projeto está sob a licença MIT. Veja detalhes em LICENSE.

---

<div align="center">

**[⬆ voltar ao topo](#-projeto-1---gerador-de-pastas)**

</div>
