# make a stack plot
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 6)
y1 = np.array([1, 2, 3, 4, 5])
y2 = np.array([2, 3, 4, 5, 6])
y3 = np.array([3, 4, 5, 6, 7])
plt.stackplot(x, y1, y2, y3, labels=['y1', 'y2', 'y3'], colors=['m', 'c', 'r'])
plt.legend(loc='upper left')
plt.title('Stack Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
plt.tight_layout()