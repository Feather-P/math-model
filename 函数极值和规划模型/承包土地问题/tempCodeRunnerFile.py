import pulp as pp
import  numpy as np

def transportation_problem_with_dicts(costs, supply, demand):
    num_supply = len(supply)
    num_demand = len(demand)

    prob = pp.LpProblem('种植问题', sense=pp.LpMaximize)

    routes = [(i, j) for i in range(num_supply) for j in range(num_demand)]
    
    x = pp.LpVariable.dict(name="route",indices=routes, lowBound=0)

    prob += pp.lpSum([costs[i][j] * x[(i, j)] for i, j in routes]), "总利润"

    for i in range(num_supply):
        prob += pp.lpSum(x[(i, j)] for j in range(num_demand)) == supply[i]
    
    for j in range(num_demand):
        prob += pp.lpSum(x[(i,j)] for i in range(num_supply)) == demand[j]

    prob.solve()

    result_table = np.zeros((num_supply, num_demand))
    for i, j in routes:
        result_table[i][j] = pp.value(x[(i, j)])
        
    return {
        'objective': pp.value(prob.objective),
        'var': result_table.tolist()
    }

def main():
    costs = np.array([
        [500,550,630,1000,800,700],
        [800,700,600,950,900,930],
        [1000,960,840,650,600,700],
        [1200,1040,980,860,880,780]
    ])
    supply = [76, 88, 96, 40]
    demand = [42, 56, 44, 39, 60, 59]
    
    res = transportation_problem_with_dicts(costs=costs, supply=supply, demand=demand)

    print(f'最大利润为: {res["objective"]}')
    print("种植方案表：")
    for row in res['var']:
        print(row)
if __name__ == "__main__":
    main()