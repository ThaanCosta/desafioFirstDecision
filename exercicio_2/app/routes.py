from flask import request, jsonify
from app import app, db
from app.models import DadosEscola

@app.route('/tasks', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'POST':
        task_data = request.get_json()
        new_task = DadosEscola(**task_data)
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created'}), 201
    
    tasks = DadosEscola.query.all()
    return jsonify([task.as_dict() for task in tasks])

@app.route('/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
def modify_task(task_id):
    task = DadosEscola.query.get(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404

    if request.method == 'PUT':
        task_data = request.get_json()
        task.update(task_data)
        db.session.commit()
        return jsonify({'message': 'Task updated'})

    if request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted'})
