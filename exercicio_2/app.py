from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulando um banco de dados com uma lista
lista_compras = [
    {
        'id': 1,
        'Item': 'Arroz'
    },
    {
        'id': 2,
        'Item': 'Feijão'
    },
    {
        'id': 3,
        'Item': 'Cuscuz'
    },
    {
        'id': 4,
        'Item': 'Ovos'
    },
    {
        'id': 5,
        'Item': 'Carne'
    },
]

@app.route('/listadecompras', methods=['GET'])
def get_lista_compras():
    return jsonify(lista_compras)

@app.route('/listadecompras', methods=['POST'])
def adiciona_lista_compras():
    nova_lista_compra = request.json
    lista_compras.append(nova_lista_compra)
    return jsonify(nova_lista_compra), 201

@app.route('/listadecompras/<int:id>', methods=['DELETE'])
def deleta_lista_compras(id):
    lista_compra = next((lista for lista in lista_compras if lista['id'] == id), None)
    if lista_compra is None:
        return jsonify({"error": "Lista de Compras não encontrada"}), 404
    lista_compras.remove(lista_compra)
    return jsonify(lista_compra)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
