from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados para simular um banco de dados

todos = [
    {"id": 1, "task": "Estudar Python",  "completed":False},
    {"id": 2, "task": "Criar API com Flask",  "completed":False},
    {"id": 3, "task": "Aprender WindowsForm",  "completed":False},
    {"id": 4, "task": "Dominar Flask",  "completed":False},
    {"id": 5, "task": "Usar Django",  "completed":False},
]

@app.route('/')
def home():
    return "Bem-vindo à API de Tarefas!"

# Rota para obter todas as tarefas
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Rota para obter uma tarefa pelo ID
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Tarefa não encontrada"}), 404
    return jsonify(todo)

# Rota para criar uma nova tarefa
@app.route('/todos', methods=['POST'])
def create_todo():
    new_todo = request.json
    new_todo["id"] = len(todos) + 1
    todos.append(new_todo)
    return jsonify(new_todo), 201

# Rota para atualizar uma tarefa existente
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Tarefa não encontrada"}), 404

    data = request.json
    todo.update(data)
    return jsonify(todo)

# Rota para deletar uma tarefa
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)