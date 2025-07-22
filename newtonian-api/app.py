# app.py
from flask import Flask, request, jsonify
from model_newtonian import fit_newtonian

app = Flask(__name__)

@app.route('/fit', methods=['POST'])
def fit():
    data = request.get_json()
    result = fit_newtonian(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run()

