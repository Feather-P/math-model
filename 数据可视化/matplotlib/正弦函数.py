import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(- 2 * np.pi, 2 * np.pi, 50)
y = np.sin(x)

plt.figure(figsize=[8, 6])
plt.scatter(x=x, y=y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = sin(x)')
plt.show()