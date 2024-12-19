import numpy as np
import pandas as pd

df = pd.read_csv('data/day1.csv')

arr = df.to_numpy()

col1 = arr[:, 0]
col2 = arr[:, 1]

sort1 = np.sort(col1, axis = 0)
sort2 = np.sort(col2, axis = 0)

# part 1 result
res = np.sum(np.abs(sort2 - sort1))
print(res)

unique = np.unique(col1)

sumit = np.sum(col2[:, np.newaxis] == unique, axis=0)

# part 2 result
res2 = np.sum(sumit * unique)
print(res2)

