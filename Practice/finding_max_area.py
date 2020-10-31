import numpy as np
import pandas as pd
import pickle
from sklearn.utils.extmath import cartesian
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.spatial as ss

# 1. Assume that the maximum boundary value is a thousand first, then generate numpy arrays to contain the integer values and their cartesian product.
max_range_num = 1000
x_range = np.arange(-max_range_num, max_range_num + 1, 1)
y_range = np.arange(-max_range_num, max_range_num + 1, 1)
coordinates = cartesian([x_range, y_range]) 
# print(len(coordinates)) 4004001


# 2. Convert the combined coordinates into a dataframe for vectorised operations.
df_coordinates = pd.DataFrame(data=coordinates)
df_coordinates.columns = ['x', 'y']
df_coordinates = df_coordinates[1:-1] #4003999


# 3. Assign boolean values indicating whether the sum is less than or equal to 23 accordingly.
def digitise_and_sum(num):  
    sum = 0
    num = abs(num)
    for digit in str(num): 
        sum += int(digit)     
    return sum
    
def safe_area_threshold(x, y):
    print(x, y)
    digit_sum = digitise_and_sum(x) + digitise_and_sum(y)
    if digit_sum <= 23:
        return True
    else:
        return False

# df_coordinates['sum_of_digits'] = df_coordinates.apply(lambda row: safe_area_threshold(row[0], row[1]), axis = 1)
# safe_area_true_only = df_coordinates[df_coordinates.sum_of_digits == True]
# safe_area_true_only.to_pickle('./safe_area_true_only.pkl.gz', compression='gzip')

safe_area_true_only = pd.read_pickle('./safe_area_true_only.pkl.gz', compression='gzip')
# print(safe_area_true_only.shape) 1257751 coordinates are safe from the mines.

mgdf = df_coordinates.merge(safe_area_true_only, how='left', on=['x','y'])

sampledf = mgdf.iloc[:100]
# print(sampledf)


def area_count(df):
    for index, row in df.iterrows():
        count=0
        if row.sum_of_digits == True and any([(row.x, row.y + 1) == True, (row.x + 1, row.y) == True, (row.x, row.y - 1) == True, (row.x - 1, row.y) == True]):
            print('hi')
            count += 1
            print(count)
        # else:
            # return 0
        
a = area_count(sampledf)
print(a)