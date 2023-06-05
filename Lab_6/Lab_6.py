import math

def estimate_task(a, m, b):
    E = (a + 4*m + b) / 6
    SD = (b - a) / 6
    return E, SD

def estimate_project(tasks):
    task_Es = []
    task_SDs = []
    for task in tasks:
        E, SD = estimate_task(*task)
        task_Es.append(E)
        task_SDs.append(SD)
    project_E = sum(task_Es)
    project_SD = math.sqrt(sum(sd**2 for sd in task_SDs))
    return project_E, project_SD

def confidence_interval(E, SE):
    lower_bound = E - 2 * SE
    upper_bound = E + 2 * SE
    return lower_bound, upper_bound

tasks = []
while True:
    a = float(input("Enter the optimistic estimate for a task (a): "))
    m = float(input("Enter the most likely estimate for a task (m): "))
    b = float(input("Enter the pessimistic estimate for a task (b): "))
    tasks.append((a, m, b))
    more_tasks = input("Are there more tasks to estimate? (y/n): ")
    if more_tasks.lower() == "n":
        break
project_E, project_SD = estimate_project(tasks)
project_lower_bound, project_upper_bound = confidence_interval(project_E, project_SD)

print("Project's estimated score: {:.2f} points".format(project_E))
print("Project's standard deviation: {:.2f} points".format(project_SD))
print("Project's 95% confidence interval: {:.2f} ... {:.2f} points".format(project_lower_bound, project_upper_bound))