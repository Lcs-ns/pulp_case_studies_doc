import pulp as pl

Oils = ["VEG1", "VEG2", "OIL1", "OIL2", "OIL3", "TOT"]

costs = {
    "VEG1": 110,
    "VEG2": 120,
    "OIL1": 130,
    "OIL2": 110,
    "OIL3": 115
}

hardness = {
    "VEG1": 8.8,
    "VEG2": 6.1,
    "OIL1": 2.0,
    "OIL2": 4.2,
    "OIL3": 5.0
}

prob = pl.LpProblem("Vegetable and Non-Vegetable Oils Problem", pl.LpMaximize)

oil_vars = pl.LpVariable.dicts("oil", Oils, 0)

subset_tot = [i for i in Oils if i != "TOT"]
subset = [j for j in subset_tot if j not in ["VEG1", "VEG2"]]

prob += oil_vars["TOT"], "MaximizeTotalProduction"

prob += pl.lpSum(oil_vars[i] for i in subset_tot) == oil_vars["TOT"], "TotalSum"
prob += pl.lpSum(oil_vars[i] * costs[i] for i in subset_tot) <= 150 * oil_vars["TOT"], "CostPercentage"
prob += oil_vars["VEG1"] + oil_vars["VEG2"] <= 200, "VegetableRefine"
prob += pl.lpSum(oil_vars[i] for i in subset) <= 250, "NonVegetableRefine"
prob += pl.lpSum(oil_vars[i] * hardness[i] for i in subset_tot) <= 6 * oil_vars["TOT"], "HardnessMax"
prob += pl.lpSum(oil_vars[i] * hardness[i] for i in subset_tot) >= 3 * oil_vars["TOT"], "HardnessMin"

prob.solve()

prob.writeLP("OilModel.lp")

print(pl.LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

