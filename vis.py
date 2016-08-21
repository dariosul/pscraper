import matplotlib as mpl
import numpy as np

#names, population, votes = np.loadtxt('state_data.csv', dtype= ['str','int','int'],delimiter=',', usecols = (0,1,2), unpack = True)
population, votes = np.loadtxt('state_data.csv', dtype= 'int',delimiter=',', usecols = (1,2), unpack = True)
#names = np.loadtxt('state_data.csv', dtype= 'str',delimiter=',', usecols = (0), unpack = True)
