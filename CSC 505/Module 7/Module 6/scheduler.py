
def schedule_tasks(tasks):
    # Sort the tasks by arrival time (FCFS order)
    tasks = sorted(tasks, key=lambda x: x['arrival'])
    current_time = 0
    for task in tasks:
        name = task['name']
        arrival = task['arrival']
        burst = task['burst']
        # If CPU is idle waiting for the task to arrive
        if current_time < arrival:
            current_time = arrival
        start_time = current_time
        finish_time = current_time + burst
        print(f"Task {name} started at time {start_time} and finished at time {finish_time}.")
        current_time = finish_time

# Example usage:
tasks = [
    {"name": "A", "arrival": 0, "burst": 4},
    {"name": "B", "arrival": 2, "burst": 3},
    {"name": "C", "arrival": 5, "burst": 2}
]
schedule_tasks(tasks)
