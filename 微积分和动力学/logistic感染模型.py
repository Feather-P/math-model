import scipy
import numpy as np
import matplotlib.pyplot as plt

lamda = 1.0 
y0 = 1e-7 # 初始感染人数
t = np.arange(0, 100, 1) # 时间范围

def dy_dt(y, t):
    return lamda * y * (1 - y)

y = scipy.integrate.odeint(dy_dt, y0, t)
deriv = dy_dt(y, t)

plt.plot(t, y, 'b-', label='Infected Population')
plt.plot(t, deriv.flatten(), 'r--', label='Infection Rate')
plt.xlabel('Time')
plt.ylabel('Population / Rate')
plt.title('Logistic Model of Infection Spread')
plt.legend(loc='upper right')
plt.grid()
plt.show()