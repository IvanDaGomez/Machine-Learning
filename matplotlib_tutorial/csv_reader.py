import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter
data = []
path = os.getcwd()
# print(path + '/data.csv')
with open(path + '/data.csv', 'r') as file:
  text = file.read()
  lines = text.split('\n')[1:-1] # the first one is header and last one is empty


  data = [line.split(',')[1].split(';') for line in lines]
c = Counter()
for element in data:
  c.update(element)
c = dict(sorted(c.items(), key=lambda item: item[1], reverse=False))
# print(c)
languages = c.keys()
popularity = c.values()
for key in c.keys():
  plt.barh(key, c[key], label=key)
# plt.barh(languages, popularity)
# plt.legend()
plt.title('List of languages with their popularity')
plt.xlabel('Popularity')
plt.ylabel('Languages')
plt.show()