import numpy as np
import scipy
import matplotlib.pyplot as plt

lamda = 0.2 # 感染者每天能接触到易感人群的数量
sigma = 2.5 # 一个感染者在整个感染周期内能感染的人数
mu = lamda / sigma # 治愈率
y0 = 1e-4 # 初始感染人数
y1 = 0 # 初始康复人数
t = np.arange(0, 200, 1) # 时间范围

def dy_dt(y, t, lamda, mu):
    i, m = y # i为感染者数量， m为康复者数量
    di_dt = lamda * i * (1 - i - m) - mu * i
    dm_dt = mu * i
    return [di_dt, dm_dt]

y = scipy.integrate.odeint(dy_dt, [y0, y1], t, args=(lamda, mu))
deriv = np.array([dy_dt([y[i, 0], y[i, 1]], t[i], lamda, mu) for i in range(len(t))])

plt.plot(t, y[:, 0], 'b-', label='Infected Population')
plt.plot(t, y[:, 1], 'g-', label='Recovered Population')
plt.plot(t, deriv[:, 0], 'r--', label='Infection Rate')
plt.plot(t, deriv[:, 1], 'y--', label='Recovery Rate')
plt.xlabel('Time')
plt.ylabel('Population / Rate')
plt.title('SIR Model of Infection Spread')
plt.legend(loc='right')
plt.grid()
plt.show()