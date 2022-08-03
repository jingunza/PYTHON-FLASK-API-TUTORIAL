# al inicio
from flask import Flask, jsonify, request
app = Flask(__name__)
import json

todos = [
    { "label": "Sample", "done": True }
]

# endpoint
@app.route('/todos', methods=['GET'])
def tasker():
    json_todos = jsonify(todos)
    return json_todos

# endpoint
@app.route('/todos', methods=['POST'])
def add_new_todo():
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    request_body = request.data
    print("Incoming request with the following body", request_body)
    json_todos = jsonify(todos)
    return json_todos

# endpoint
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[position]
    json_todos = jsonify(todos)
    return json_todos

# al final
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

# luego se ejecuta en el terminal: pipenv run python src/app.py