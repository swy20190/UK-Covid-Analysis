import pandas as pd
import numpy as np

data_set = pd.read_csv("../data/simplified.csv")

# 185 rows, 6 columns
data_matrix = np.array(data_set)

test_neg = []
test_pos = []
real_pos = []
for i in range(185):
    test_neg.append(data_matrix[i][0]-data_matrix[i][1])
    test_pos.append(data_matrix[i][1])
    real_pos.append(data_matrix[i][2]+data_matrix[i][3]+data_matrix[i][4]+data_matrix[i][5])

# real_pos = test_pos*(1-P1) + test_neg*P2
# formalize so that real_pos/test_neg = (1-P1)*test_pos/test_neg + P2
y = []
x = []
for i in range(185):
    y.append(real_pos[i]/test_neg[i])
    x.append(test_pos[i]/test_neg[i])

xy_sum = []
x_sq_sum = []
for i in range(185):
    xy_sum.append(x[i]*y[i])
    x_sq_sum.append(x[i]**2)

# a=1-P1 b=P2
a = (np.mean(xy_sum)-np.mean(x)*np.mean(y))/(np.mean(x_sq_sum)-np.mean(x)**2)
b = np.mean(y)-a*np.mean(x)

print(a)
print(b)
