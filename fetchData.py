import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with open('housing.csv', 'r') as csvfile:
         reader = csv.reader(csvfile, delimiter=' ', quotechar='|')


housing = pd.read_csv('housing.csv')

'''
print(housing.describe())
'''

def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


train_set, test_set = split_train_test(housing, 0.2)
print(len(train_set), "train +", len(test_set), "test")


'''
using matplotlib you can show histogram data and outputs for regions
housing.hist(bins=50, figsize=(20,15))
plt.show()


find specific column numbers 
print(housing["ocean_proximity"].value_counts())

general info about data set
print(housing.info())

         for row in reader:
             print(row)

         for row in reader:
             print(row)

             print ', '.join(row)
'''
             
