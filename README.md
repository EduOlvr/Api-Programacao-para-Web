# API de Gerenciamento de Tarefas

## Descrição
Esta é uma API RESTful simples para gerenciamento de tarefas, desenvolvida como atividade acadêmica.  
Permite adicionar, listar, atualizar e remover tarefas. A API utiliza Python e Flask e salva os dados em memória ou em arquivo JSON local.

O objetivo é praticar conceitos de APIs RESTful, métodos HTTP, manipulação de dados em JSON e documentação.

---

## Rotas da API

| Método | Rota               | Descrição                            | Exemplo de Requisição                                                                                  | Exemplo de Resposta                        |
|--------|-------------------|--------------------------------------|-------------------------------------------------------------------------------------------------------|-------------------------------------------|
| GET    | `/tasks`          | Lista todas as tarefas em JSON       | `curl http://127.0.0.1:5000/tasks`                                                                  | `[{"title": "Comprar pão"}]`              |
| POST   | `/tasks`          | Adiciona uma nova tarefa             | `curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title": "Estudar"}'` | `{"message": "Tarefa adicionada com sucesso"}` |
| GET    | `/tasks/view`     | Mostra todas as tarefas em HTML      | Acessar no navegador `http://127.0.0.1:5000/tasks/view`                                             | Página HTML listando tarefas              |
| PUT    | `/tasks/<int:id>` | Atualiza uma tarefa existente       | `curl -X PUT http://127.0.0.1:5000/tasks/0 -H "Content-Type: application/json" -d '{"title": "Estudar Flask"}'` | `{"message": "Tarefa atualizada com sucesso"}` |
| DELETE | `/tasks/<int:id>` | Remove uma tarefa pelo ID            | `curl -X DELETE http://127.0.0.1:5000/tasks/0`                                                      | `{"message": "Tarefa removida com sucesso"}` |

---

## Como executar localmente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
````

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Instale as dependências:

```bash
pip install Flask
```

> Opcional: crie um arquivo `requirements.txt` para facilitar futuras instalações:

```bash
pip freeze > requirements.txt
```

4. Execute a aplicação:

```bash
python app.py
```

5. Teste as rotas usando curl ou navegador:

* JSON: `curl http://127.0.0.1:5000/tasks`
* HTML: `http://127.0.0.1:5000/tasks/view`

---

## Exemplos de uso

* Adicionar uma tarefa:

```bash
curl -X POST http://127.0.0.1:5000/tasks \
-H "Content-Type: application/json" \
-d '{"title": "Ler livro"}'
```

* Atualizar uma tarefa:

```bash
curl -X PUT http://127.0.0.1:5000/tasks/0 \
-H "Content-Type: application/json" \
-d '{"title": "Estudar Flask"}'
```

* Deletar uma tarefa:

```bash
curl -X DELETE http://127.0.0.1:5000/tasks/0
```

---

## Possíveis usos da nossa API

Esta API pode ser utilizada por estudantes, professores ou pequenos negócios que precisam de um **gerenciador de tarefas simples**.

Exemplos:

* Um professor pode acompanhar tarefas e atividades dos alunos.
* Um empreendedor pode organizar tarefas diárias da equipe.
* Um usuário comum pode controlar afazeres pessoais, lembretes e listas de compras.

Mesmo sendo simples, esta API ensina conceitos reais de manipulação de dados, métodos HTTP e endpoints RESTful que podem ser escalados em sistemas mais complexos.

---

## Observações

* Use o método HTTP correto para cada ação (GET para leitura, POST para criação, PUT para atualização, DELETE para remoção).
* A API salva os dados em memória ou arquivo local, portanto os dados persistem apenas no mesmo ambiente de execução.
* Sempre forneça dados JSON válidos ao adicionar ou atualizar tarefas.

```

---

