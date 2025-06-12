from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire en mémoire pour stocker les utilisateurs
users = {
    # Exemple initial, peut être vide si tu veux
    # "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route('/')
def home():
    return "Bienvenue sur l'API Flask !"

@app.route('/data')
def data():
    # On retourne la liste des usernames (clés du dictionnaire)
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Construire l'objet utilisateur à partir des données reçues
    user = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    users[username] = user

    return jsonify({"message": "User added", "user": user}), 201


if __name__ == '__main__':
    app.run()
