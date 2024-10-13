import random

def minimization_function(x):
    return (x - 3) ** 2

def maximization_function(x):
    return -x ** 2 + 5

def generate_random_solution_min():
    return random.randint(-10, 10)

def generate_random_solution_max():
    return random.randint(-10, 10)

def mutate_solution_min(solution):
    return solution + random.choice([-1, 1])

def mutate_solution_max(solution):
    return solution + random.choice([-1, 1])

def hill_climb_min():
    best_sol = generate_random_solution_min()
    best_score = minimization_function(best_sol)

    while True:
        print(f"Current best: x = {best_sol}, f(x) = {best_score}")
        if best_score == 0:
            print("Global minimum found at x =", best_sol)
            break
        new_sol = mutate_solution_min(best_sol)
        new_score = minimization_function(new_sol)
        if new_score < best_score:
            best_sol = new_sol
            best_score = new_score

def hill_climb_max():
    best_solution = generate_random_solution_max()
    best_score = maximization_function(best_solution)

    while True:
        print(f"Current best: x = {best_solution}, f(x) = {best_score}")
        if best_score == 5:
            print("Found global maximum at x =", best_solution)
            break
        new_solution = mutate_solution_max(best_solution)
        new_score = maximization_function(new_solution)
        if new_score > best_score:
            best_solution = new_solution
            best_score = new_score




#Resource Allocation
def objective_function_maximize(selected_projects, projects):
    total_benefit = 0
    total_resources = 0

    for project in selected_projects:
        total_resources += projects[project]["resources"]
        total_benefit += projects[project]["benefit"]

    if total_resources > 100:
        return float('-inf')
    return total_benefit

def objective_function_minimize(selected_projects, projects):
    total_time = 0
    total_resources = 0

    for project in selected_projects:
        total_resources += projects[project]["resources"]
        total_time += projects[project]["time"]

    if total_resources > 100:
        return float('inf')
    return total_time

def generate_random_solution(project_ids):
    num_projects = len(project_ids)
    return random.sample(project_ids, random.randint(1,num_projects))


def mutate_solution(current_solution, project_ids):
    new_solution = current_solution.copy()

    mutation_type = random.choice(['add', 'remove', 'swap'])

    if mutation_type == 'add':
        num_projects_to_add = random.randint(1, len(project_ids)//2)
        for _ in range(num_projects_to_add):
            new_project = random.choice(project_ids)
            if new_project not in new_solution:
                new_solution.append(new_project)
    elif mutation_type == 'remove':
        num_projects_to_remove = random.randint(1, max(1, len(new_solution)//2))
        for _ in range(num_projects_to_remove):
            if new_solution:
                project_to_remove = random.choice(new_solution)
                new_solution.remove(project_to_remove)
    elif mutation_type == 'swap':
        if new_solution:
            project_to_remove = random.choice(new_solution)
            new_solution.remove(project_to_remove)
            project_to_add = random.choice(project_ids)
            while project_to_add in new_solution:
                project_to_add = random.choice(project_ids)
            new_solution.append(project_to_add)

    if not new_solution:
        new_solution.append(random.choice(project_ids))

    return new_solution

def randomized_hill_climbing(projects, objective_function, minimize=False):
    project_ids = list(projects.keys())

    best_solution = generate_random_solution(project_ids)
    best_score = objective_function(best_solution, projects)

    no_improvement_iterations = 0
    max_iterations_without_improvement = 25

    while no_improvement_iterations < max_iterations_without_improvement:
        print(f"Current best solution: {best_solution}, Score: {best_score}")

        new_solution = mutate_solution(best_solution, project_ids)
        new_score = objective_function(new_solution, projects)

        if new_score == float('-inf') or new_score == float('inf'):
            no_improvement_iterations += 1
            continue

        if minimize:
            if new_score < best_score:
                best_solution = new_solution
                best_score = new_score
                no_improvement_iterations = 0
            else:
                no_improvement_iterations += 1
        else:
            if new_score > best_score:
                best_solution = new_solution
                best_score = new_score
                no_improvement_iterations = 0
            else:
                no_improvement_iterations += 1

    print("Stopping due to no improvement. Final best solution:", best_solution, "Score:", best_score)

TestCase1 = {
    "1": {"resources": 20, "benefit": 40},
    "2": {"resources": 30, "benefit": 50},
    "3": {"resources": 25, "benefit": 30},
    "4": {"resources": 15, "benefit": 25},
}

TestCase2 = {
    "A": {"resources": 10, "time": 15},
    "B": {"resources": 40, "time": 60},
    "C": {"resources": 20, "time": 30},
    "D": {"resources": 25, "time": 35},
    "E": {"resources": 5, "time": 10},
}

TestCase3 = {
    "X": {"resources": 50, "benefit": 80},
    "Y": {"resources": 30, "benefit": 45},
    "Z": {"resources": 15, "benefit": 20},
    "W": {"resources": 25, "benefit": 35},
}

hill_climb_min()
hill_climb_max()
print("Randomized Hill Climbing Test Case 1 (Maximizing Benefits)")
randomized_hill_climbing(TestCase1, objective_function_maximize)
print("Randomized Hill Climbing Test Case 2 (Minimizing Time)")
randomized_hill_climbing(TestCase2, objective_function_minimize, minimize=True)
print("Randomized Hill Climbing Test Case 3 (Maximizing Benefits)")
randomized_hill_climbing(TestCase3, objective_function_maximize)


