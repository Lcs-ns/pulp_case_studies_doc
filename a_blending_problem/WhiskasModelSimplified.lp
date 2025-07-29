\* The_Whiskas_Problem *\
Minimize
OBJ: 0.008 BeefPercent + 0.013 ChikenPercet
Subject To
FatRequirement: 0.1 BeefPercent + 0.08 ChikenPercet >= 6
FibreRequirement: 0.005 BeefPercent + 0.001 ChikenPercet <= 2
PercentageSum: BeefPercent + ChikenPercet = 100
ProteinRequirement: 0.2 BeefPercent + 0.1 ChikenPercet >= 8
SaltRequirement: 0.005 BeefPercent + 0.002 ChikenPercet <= 0.4
Bounds
 0 <= ChikenPercet
Generals
ChikenPercet
End
