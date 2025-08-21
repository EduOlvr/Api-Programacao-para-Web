from flask import Flask, jsonify, request, render_template_string
import json
import os

app = Flask(__name__)

DATA_FILE = "tasks.json"

# Inicializa arquivo se não existir
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

# Funções auxiliares
def read_tasks():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Rota 1: Listar todas as tarefas (JSON)
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = read_tasks()
    return jsonify(tasks), 200

# Rota 2: Adicionar uma nova tarefa
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or "title" not in data or "description" not in data:
        return jsonify({"error": "Dados incompletos"}), 400
    tasks = read_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "description": data["description"]
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201

# Rota 3: Página HTML simples mostrando todas as tarefas
@app.route("/tasks/view", methods=["GET"])
def view_tasks():
    tasks = read_tasks()
    html = """
    <h1>Lista de Tarefas</h1>
    <ul>
    {% for task in tasks %}
      <li><b>{{task['title']}}</b>: {{task['description']}}</li>
    {% endfor %}
    </ul>
    """
    return render_template_string(html, tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)
