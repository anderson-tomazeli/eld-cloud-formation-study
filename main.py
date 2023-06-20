from flask import Flask, jsonify
from collections import OrderedDict

app = Flask(__name__)

snacks = [
    OrderedDict([
        ("id", 1),
        ("name", "X-Tudo"),
        ("price", 14.00),
        ("combo_price", 30.00),
        ("description", "Pão brioche, burger de 150g, queijo, alface, tomate e cebola")
    ]),
    OrderedDict([
        ("id", 2),
        ("name", "X-Egg"),
        ("price", 13.75),
        ("combo_price", 24.99),
        ("description", "Pão francês, burger de 130g, ovo, alface, tomate e cebola")
    ]),
    OrderedDict([
        ("id", 3),
        ("name", "X-Salada"),
        ("price", 9.75),
        ("combo_price", 18.00),
        ("description", "Pão de forma, queijo, alface, tomate e cebola")
    ]),
]

@app.route('/snacks', methods=['GET'])
def get_snacks():
    snacks_list = [{"name": snack["name"], "price": snack["price"]} for snack in snacks]
    return jsonify(snacks_list)

@app.route('/snacks/<int:snack_id>', methods=['GET'])
def get_snack(snack_id):
    snack = next((s for s in snacks if s["id"] == snack_id), None)
    if snack:
        ordered_snack = OrderedDict([(k, snack[k]) for k in snack])
        return jsonify(ordered_snack)
    else:
        return jsonify({"error": "Snack not found."}), 404

if __name__ == '__main__':
    app.run()