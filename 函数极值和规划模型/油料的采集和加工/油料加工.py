from scipy.optimize import linprog
import numpy as np

c = np.array([
    110, 120, 130, 110, 115, -150
])
A = np.array([
    [1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [-8.8, -6.1, -2.0, -4.2, -5.0, 3],
    [8.8, 6.1, 2.0, 4.2, 5.0, -6]
])
b = np.array([
    200,
    250,
    0,
    0
])
aeq = np.array([[
    1, 1, 1, 1, 1, -1
]])
beq = np.array([[0]])
bounds = (
    np.array([0, np.inf]),
    np.array([0, np.inf]),
    np.array([0, np.inf]),
    np.array([0, np.inf]),
    np.array([0, np.inf]),
    np.array([0, 450])
)

result = linprog(c=c, A_ub=A, b_ub=b, A_eq=aeq, b_eq=beq, bounds=bounds)

if result.success:
    optimal_value = result.fun
    print(f"最优目标函数值 (fun): {optimal_value}")

    optimal_solution = result.x
    print(f"最优解 (x): {optimal_solution}")

    iterations = result.nit
    print(f"迭代次数 (nit): {iterations}")
else:
    print("求解失败:", result.message)