import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
plt.style.use('seaborn-v0_8-pastel')
x_labels = np.arange(20, 31)
x_indexes = np.arange(len(x_labels))
y_1_labels = np.random.randint(0, 100, size=len(x_labels))
print(len(x_labels))
y_2_labels = np.random.randint(0, 100, size=len(x_labels))
y_3_labels = np.random.randint(0, 100, size=len(x_labels))
width = 0.25

plt.bar(x_indexes - width, y_1_labels, width=width, color='k', label='1 Data')
plt.bar(x_indexes, y_2_labels, width=width, color='g',label='2 Data')
plt.bar(x_indexes + width, y_3_labels, width=width, color='y',label='3 Data')
plt.xticks(ticks=x_indexes, labels=x_labels)
plt.legend()
plt.xlabel('Data x')
plt.ylabel('Data y')
plt.tight_layout()
if __name__ == '__main__':
  plt.show()