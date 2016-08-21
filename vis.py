import matplotlib as mpl
import numpy as np
import pandas as pd
#import retreive_data.py

##names, population, votes = np.loadtxt('state_data.csv', dtype= ['str','int','int'],delimiter=',', usecols = (0,1,2), unpack = True)
#population, votes = np.loadtxt('state_data.csv', dtype= 'int',delimiter=',', usecols = (1,2), unpack = True)
##names = np.loadtxt('state_data.csv', dtype= 'str',delimiter=',', usecols = (0), unpack = True)

data = pd.read_csv('state_data.csv').as_matrix()

names = [];
population = [];
votes = [];

# for row in data:
#     names.append(row[0])
#     population.append(row[1])
#     votes.append(row[2])

obj = [(names.append(row[0]), population.append(row[1]),votes.append(row[2]) ) for row in data]
