import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('state_data.csv')

names = data.ix[:, 0]
population = data.ix[:, 1]
votes = data.ix[:, 2]

ratio = [ (ppl/vote) for ppl, vote in zip(population, votes) ]

plt.plot(votes,population, 'ko')
plt.ylabel('State population')
plt.xlabel('State Electoral Votes')
plt.grid(True)
plt.show()

plt.plot(ratio)
plt.ylabel('State population per vote')
plt.yscale('linear')
plt.axis([0,50, 0 ,max(ratio)+1e5])
plt.grid(True)
plt.show()
