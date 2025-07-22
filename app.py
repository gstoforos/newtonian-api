from flask import Flask, request, jsonify
from model_newtonian import fit_newtonian

app = Flask(__name__)

@app.route('/fit', methods=['POST'])
def fit():
    try:
        data = request.get_json()
        result = fit_newtonian(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)

