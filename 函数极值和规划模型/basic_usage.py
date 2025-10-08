from scipy.optimize import linprog
import numpy as np

c = np.array([-72, -64])
A = np.array([[1, 1], [12, 8]])
b = np.array([[50], [480]])
bounds = (np.array([0, 100/3.0]), np.array([0, np.inf]))

result = linprog(c=c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

if result.success:
    optimal_value = result.fun
    print(f"最优目标函数值 (fun): {optimal_value}")

    optimal_solution = result.x
    print(f"最优解 (x): {optimal_solution}")

    iterations = result.nit
    print(f"迭代次数 (nit): {iterations}")
else:
    print("求解失败:", result.message)