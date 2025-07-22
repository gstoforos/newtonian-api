import numpy as np
from scipy.optimize import curve_fit

def fit_newtonian(shear_rates, shear_stresses, flow_rate=None, pipe_diameter=None, fluid_density=None):
    gamma = np.array(shear_rates)
    sigma = np.array(shear_stresses)

    # Model: σ = μ * γ̇
    def model(g, mu): return mu * g
    popt, _ = curve_fit(model, gamma, sigma)
    mu = float(popt[0])

    predictions = model(gamma, mu)
    residuals = sigma - predictions
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((sigma - np.mean(sigma))**2)
    r2 = 1 - (ss_res / ss_tot)

    mu_app = mu  # for Newtonian, apparent = constant

    # Reynolds number only if all flow params are present
    Re = None
    if all(v is not None for v in [flow_rate, pipe_diameter, fluid_density]):
        if flow_rate == 0 or pipe_diameter == 0 or fluid_density == 0:
            Re = None
        else:
            velocity = flow_rate / (np.pi * (pipe_diameter / 2)**2)
            Re = (fluid_density * velocity * pipe_diameter) / mu

    return {
        "model": "Newtonian",
        "mu": round(mu, 6),
        "mu_app": round(mu_app, 6),
        "r2": round(r2, 6),
        "Re": round(Re, 2) if Re is not None else None,
        "equation": "σ = μ · γ̇"
    }
