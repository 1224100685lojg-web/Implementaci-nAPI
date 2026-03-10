from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def inicio():
    return "Mi primera API con Flask"

@app.route('/api', methods=['GET'])
def api():
    return jsonify({
        "mensaje": "API funcionando correctamente",
        "autor": "Owen",
        "curso": "Desarrollo de APIs"
    })

if __name__ == '__main__':
    app.run(debug=True)
