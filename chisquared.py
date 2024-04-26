import numpy as np
from scipy.stats import chisquare
pos_expected = np.array([2.9,19.6,2.9,69.8,2.2,2.6])
pos_actual = np.array([6.3,15.9,4.8,71.4,0.1,1.5])

neg_expected = np.array([10,43.2,7.6,37.3,0.9,1])
neg_actual = np.array([28.8,30.1,11,27.4,1.4,1.3])

overall_expected = np.array([7.3,34.4,5.9,49.5,1.5,1.4])
overall_actual = np.array([18.4,23.5,8.1,47.8,0.7,1.5])

print("Chi-Squared for positive tone:")
print(chisquare(f_obs= pos_actual, f_exp=pos_expected))

print("Chi-Squared for negative tone:")
print(chisquare(f_obs= neg_actual, f_exp=neg_expected))

print("Chi-Squared for overall tone:")
print(chisquare(f_obs= overall_actual, f_exp=overall_expected))