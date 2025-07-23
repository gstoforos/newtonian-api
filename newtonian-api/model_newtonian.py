import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

def fit_newtonian(shear_rates, shear_stresses, flow_rate, diameter, density, re_critical=4000):
    def model(gamma_dot, mu):
        return mu * gamma_dot

    popt, _ = curve_fit(model, shear_rates, shear_stresses)
    mu_app = popt[0]

    predicted = model(np.array(shear_rates), *popt)
    r2 = r2_score(shear_stresses, predicted)

    # Newtonian-specific values
    tau0 = 0.0
    k = mu_app
    n = 1.0

    # Calculate Reynolds number
    velocity = flow_rate / (np.pi * (diameter / 2) ** 2)
    re = (density * velocity * diameter) / mu_app

    # Calculate q_critical (flow rate below which flow is laminar)
    q_critical = (np.pi * diameter**2 / 4) * ((re_critical * mu_app) / (density * diameter))

    equation = f"τ = {mu_app:.3f}·γ̇"

    return {
        "equation": equation,
        "tau0": tau0,
        "k": k,
        "n": n,
        "r2": r2,
        "mu_app": mu_app,
        "re": re,
        "re_critical": re_critical,
        "q_critical": q_critical
    }
