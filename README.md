# AppLembrer ✦

Aplicação web acadêmica para organização de lembretes pessoais, estudos, trabalho, compromissos e horários de medicamentos **sem oferecer orientação médica**.

## Funcionalidades

- Criar lembretes com título, descrição, categoria, data e horário
- Listar, pesquisar e filtrar lembretes
- Editar e excluir lembretes
- Marcar lembretes como concluídos ou pendentes
- Guardar os dados localmente em banco SQLite
- Layout responsivo para computadores e celulares

> **Limitações desta versão:** os campos de repetição são informativos; não há notificações automáticas, contas de usuário ou autenticação. Não utilizar como único meio de lembrar medicamentos importantes.

## Tecnologias

Python, Flask, SQLite, HTML, CSS e JavaScript puro. A aplicação separa rotas/controladores (`app/routes.py`), persistência (`app/__init__.py`) e apresentação (`app/templates`, `app/static`).

## Como executar (Windows)

1. Instale Python 3.10 ou superior.
2. Abra um terminal na pasta `applembrer`.
3. Execute:

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

4. Acesse **http://127.0.0.1:5000** no navegador.

Se a ativação do ambiente virtual estiver bloqueada, use `.venv\Scripts\python.exe -m pip install -r requirements.txt` e `.venv\Scripts\python.exe run.py`.

## Como executar (macOS/Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python run.py
```

## Testes automatizados

```bash
python -m pytest -q
```

## Estrutura do projeto

```text
applembrer/
├── app/
│   ├── __init__.py        # Criação da aplicação e banco de dados
│   ├── routes.py          # Rotas e validações
│   ├── templates/
│   │   └── index.html     # Interface
│   └── static/
│       ├── css/style.css  # Estilos responsivos
│       └── js/app.js      # Interações com a API
├── docs/                  # Documentação acadêmica
├── tests/test_app.py      # Testes automatizados
├── .gitignore
├── requirements.txt
├── run.py
└── README.md
```

## GitHub

Após testar o projeto, crie um repositório **vazio** no GitHub e execute na pasta `applembrer`:

```bash
git init
git add .
git commit -m "Versão inicial do AppLembrer"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
git push -u origin main
```

Substitua a URL pelo endereço verdadeiro do seu repositório. O arquivo `.gitignore` impede que o banco local e o ambiente virtual sejam enviados.

## Observações acadêmicas

Este código é uma implementação inicial. Não registrar avaliações de usuários ou correções como realizadas antes dos testes reais. Consulte `docs/PLANO_DE_TESTES.md`.

## Segurança

Esta versão é destinada a demonstração local. Para publicar na internet, desative `debug=True`, configure uma chave secreta segura e adicione autenticação, autorização e proteções apropriadas antes de armazenar dados pessoais.
