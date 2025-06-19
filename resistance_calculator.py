import math

def calc_reynolds_number(L, V, nu=1e-6):
    return (V * L) / nu

def calc_frictional_resistance(rho, V, S, Re):
    Cf = 0.075 / ((math.log10(Re) - 2) ** 2)
    return 0.5 * rho * V**2 * S * Cf

def calc_residual_resistance(Cr, rho, V, S):
    return 0.5 * rho * V**2 * S * Cr

def calc_total_resistance(rho, V, S, L, Cr=0.004):
    Re = calc_reynolds_number(L, V)
    Rf = calc_frictional_resistance(rho, V, S, Re)
    Rr = calc_residual_resistance(Cr, rho, V, S)
    Rt = Rf + Rr
    return Rt, Rf, Rr
