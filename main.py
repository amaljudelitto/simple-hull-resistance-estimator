import json
import matplotlib.pyplot as plt
from resistance_calculator import calc_total_resistance

with open("example_input.json", "r") as f:
    ship = json.load(f)

rho = 1025  # seawater density
L = ship["Lpp"]
S = ship["wetted_surface_area"]

Vs = [v for v in range(2, 21)]  # speeds from 2 to 20 knots
Vs_mps = [v * 0.5144 for v in Vs]

Rt_list, Rf_list, Rr_list = [], [], []
for V in Vs_mps:
    Rt, Rf, Rr = calc_total_resistance(rho, V, S, L)
    Rt_list.append(Rt)
    Rf_list.append(Rf)
    Rr_list.append(Rr)

plt.plot(Vs, Rt_list, label="Total Resistance")
plt.plot(Vs, Rf_list, label="Frictional")
plt.plot(Vs, Rr_list, label="Residual")
plt.xlabel("Speed (knots)")
plt.ylabel("Resistance (N)")
plt.title("Resistance vs Speed")
plt.legend()
plt.grid()
plt.show()
