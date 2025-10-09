import pulp as pp
import numpy as np

prob = pp.LpProblem(name="一个问题", sense=pp.LpMinimize)

x1 = pp.LpVariable(name="x1", lowBound=0)
x2 = pp.LpVariable(name="x2", lowBound=0)
x3 = pp.LpVariable(name="x3", lowBound=0)

prob += 2 * x1 + 3 * x2 + x3, "目标值"
prob += x1 + 2 * x2 + 4 * x3 == 101, "约束1"
prob += x1 + 4 * x2 + 2 * x3 >= 8, "约束2"
prob += 3 * x1 + 2 * x2 >= 6, "约束3"

prob.solve()

print(f"{pp.value(prob.objective)}")