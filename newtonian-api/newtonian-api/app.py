from flask import Flask, request, jsonify
from model_fitter import fit_newtonian

app = Flask(__name__)

@app.route('/fit', methods=['POST'])
def fit():
    data = request.get_json()

    shear_rates = data.get("shear_rates", [])
    shear_stresses = data.get("shear_stresses", [])
    flow_rate = data.get("flow_rate", None)
    pipe_diameter = data.get("pipe_diameter", None)
    fluid_density = data.get("fluid_density", None)

    if not (shear_rates and shear_stresses):
        return jsonify({"error": "Missing shear data"}), 400

    result = fit_newtonian(shear_rates, shear_stresses, flow_rate, pipe_diameter, fluid_density)
    return jsonify(result)

if __name__ == "__main__":
    app.run()
