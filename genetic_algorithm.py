import numpy as np

def binary_to_float(binary_str):
    return int(binary_str, 2) / (2**16 - 1)

def objective_function(x, y):
    return (x + y) * np.sin(5 * (x**2 + y**2))

def evaluate_fitness(individual):
    x = binary_to_float(individual[:16])
    y = binary_to_float(individual[16:])
    return objective_function(x, y)

def crossover(parent1, parent2, crossover_point):
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def mutate(individual, mutation_rate, mutation_decisions):
    mutated_individual = list(individual)
    for i in range(len(mutated_individual)):
        if np.random.rand() < mutation_rate:
            mutated_individual[i] = '1' if mutation_decisions[i] == 'T' else '0'
    return ''.join(mutated_individual)

# Given individuals
individuals = [
    "01001100010110010110010010001000",
    "00010100110110110100100010001010",
    "10110101001101100000111110011100",
    "01010010011000100010000100011001",
    "11000111000100001110011110100111"
]

# Step 1: Evaluate fitness of each individual
fitness_values = [evaluate_fitness(ind) for ind in individuals]

# Step 2: Recombine two individuals with the highest fitness at crossover point 13
highest_indices = np.argsort(fitness_values)[-2:]
parent1, parent2 = individuals[highest_indices[0]], individuals[highest_indices[1]]
crossover_point = 13
new_offspring = crossover(parent1, parent2, crossover_point)

# Step 3: Apply mutation
mutation_rate = 0.05
mutation_decisions = "FFF TFFFFFFFFFFFFFTFFFFFFFFFFFTF"
mutated_offspring = mutate(new_offspring, mutation_rate, mutation_decisions)

# Step 4: Evaluate fitness of the new offspring
new_fitness = evaluate_fitness(mutated_offspring)

# Step 5: Decide if the new value should survive to the next generation
if new_fitness > min(fitness_values):
    print("The new value should survive to the next generation.")
else:
    print("The new value should not survive to the next generation.")
