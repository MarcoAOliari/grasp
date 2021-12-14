import random

def restricted_candidate_list(candidates, costs, cmax, cmin, alpha):
	rcl = []

	for i in candidates:
		if costs[i] <= cmin + alpha*(cmax - cmin):
			rcl.append(i)

	return rcl

def fits(size, weights, actual_weight, candidate):
	return actual_weight + weights[candidate] <= size

def value_of_solution(solution, profits):
	value = 0

	for i in solution:
		value += profits[i]

	return value

def construction(alpha, costs, size, weights):
	solution = []
	actual_weight = 0
	candidates = [i for i in range(len(costs))]
	chosen_candidates = []

	while candidates:
		cmin = min(costs)
		cmax = max(costs)

		rcl = restricted_candidate_list(candidates, costs, cmax, cmin, alpha)

		if rcl:
			random_candidate = random.choice(rcl)

			if fits(size, weights, actual_weight, random_candidate):
				solution.append(random_candidate)
				actual_weight += weights[random_candidate]

			candidates.remove(random_candidate)
		else:
			break

	return solution

knapsack_capacity = 165
weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
costs = [i / j for i, j in zip (weights, profits)]

best_solution = []
best_solution_value = 0

STOP = 10
alpha = 0.9

for i in range(STOP):
	solution = construction(alpha, costs, knapsack_capacity, weights)
	print(solution)
	solution_value = value_of_solution(solution, profits)

	if (best_solution_value < solution_value):
		best_solution = solution
		best_solution_value = solution_value

	print(f'ITERACAO {i+1}:\n Melhor solução: {best_solution}\n Valor: {best_solution_value}\n\n')
