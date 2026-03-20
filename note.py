import numpy as np

matrix = np.array([[170,76],[183,86],[181,78],[176,80]])

res1 = matrix[matrix[:,1] >= 80]
res2 = matrix[matrix[:,0] >= 180]

print(res1)
print(res2)