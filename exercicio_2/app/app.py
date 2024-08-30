from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def add_task():
    task = request.json
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        task = tasks.pop(task_id)
        return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
