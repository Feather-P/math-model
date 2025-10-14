from sko.DE import DE

def obj_func(x):
    x1, x2, x3 = x
    return x1 * x1+ x2* x2 + x3 * x3

constraint_ueq = [
    lambda x: 1 - x[0] - x[1],
    lambda x: x[0] * x[1] - 5
]

constraint_eq = [
    lambda x: x[1] + x[2] - 10
]

de = DE(obj_func, 3, size_pop=50, max_iter=200, lb=[0, 0, 0], ub=[5, 5, 5], constraint_eq=constraint_eq, constraint_ueq=constraint_ueq)

best_x, best_y = de.run()
print('best_x:', best_x, '\n', 'best_y:', best_y)