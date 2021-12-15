import random

# builds the restricted candidate list (RCL)
def restricted_candidate_list(candidates, costs, cmax, cmin, alpha):
	rcl = []

	for i in candidates:
		if costs[i] <= cmin + alpha*(cmax - cmin):
			rcl.append(i)

	return rcl

# returns true if the candidate fits in the bag
def fits(size, weights, actual_weight, candidate):
	return actual_weight + weights[candidate] <= size

# returns the value of a solution
def value_of_solution(solution, profits):
	value = 0

	for i in solution:
		value += profits[i]

	return value

# construction phase
def construction(alpha, costs, size, weights):
	solution = []
	actual_weight = 0
	candidates = [i for i in range(len(costs))]

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

def read_files(test):
	f_size = open(f'input/{test}/size.txt', "r")
	size = int(f_size.readline())

	weights = []
	with open(f'input/{test}/weights.txt', "r") as f_weights:
		for line in f_weights:
			weights.append(int(line))

	profits = []
	with open(f'input/{test}/profits.txt', "r") as f_profits:
		for line in f_profits:
			profits.append(int(line))

	return (size, weights, profits)

knapsack_capacity, weights, profits = read_files(8)
costs = [i / j for i, j in zip (weights, profits)]

best_solution = []
best_solution_value = 0

stop = int(input("Número máximo de iterações: "))
alpha = float(input("Valor de alpha: "))

for i in range(stop):
	solution = construction(alpha, costs, knapsack_capacity, weights)
	solution_value = value_of_solution(solution, profits)

	if (best_solution_value < solution_value):
		best_solution = solution
		best_solution_value = solution_value

	print(f'ITERACAO {i+1}:\n Solução testada: {solution}\n Melhor solução: {best_solution}\n Valor: {best_solution_value}\n\n')

best_solution.sort()
print(f'Solução final: {best_solution}')