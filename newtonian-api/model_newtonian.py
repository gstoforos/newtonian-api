import numpy as np
from sklearn.linear_model import LinearRegression

def fit_newtonian(data):
    shear_rates = np.array(data.get("shear_rates", []))
    shear_stresses = np.array(data.get("shear_stresses", []))

    # Basic check
    if len(shear_rates) != len(shear_stresses) or len(shear_rates) < 2:
        return {"error": "Invalid or insufficient shear data."}

    model = LinearRegression()
    model.fit(shear_rates.reshape(-1, 1), shear_stresses)

    mu = model.coef_[0]  # Newtonian viscosity
    r_squared = model.score(shear_rates.reshape(-1, 1), shear_stresses)

    # Flow parameters
    flow_rate = data.get("flow_rate", 0)
    diameter = data.get("pipe_diameter", 0)
    density = data.get("density", 0)

    if flow_rate > 0 and diameter > 0 and density > 0:
        # Convert to SI
        Q = float(flow_rate)
        D = float(diameter)
        rho = float(density)
        Re = (4 * rho * Q) / (np.pi * D * mu)
    else:
        Re = None

    return {
        "model": "Newtonian",
        "mu": mu,
        "r_squared": r_squared,
        "reynolds": Re
    }

