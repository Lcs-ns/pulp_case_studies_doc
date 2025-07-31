\* Vegetable_and_Non-Vegetable_Oils_Problem *\
Maximize
OBJ: oil_TOT
Subject To
CostPercentage: 130 oil_OIL1 + 110 oil_OIL2 + 115 oil_OIL3 - 150 oil_TOT
 + 110 oil_VEG1 + 120 oil_VEG2 <= 0
HardnessMax: 2 oil_OIL1 + 4.2 oil_OIL2 + 5 oil_OIL3 - 6 oil_TOT + 8.8 oil_VEG1
 + 6.1 oil_VEG2 <= 0
HardnessMin: 2 oil_OIL1 + 4.2 oil_OIL2 + 5 oil_OIL3 - 3 oil_TOT + 8.8 oil_VEG1
 + 6.1 oil_VEG2 >= 0
NonVegetableRefine: oil_OIL1 + oil_OIL2 + oil_OIL3 + oil_TOT <= 250
TotalSum: oil_OIL1 + oil_OIL2 + oil_OIL3 - oil_TOT + oil_VEG1 + oil_VEG2 = 0
VegetableRefine: oil_VEG1 + oil_VEG2 <= 200
End
