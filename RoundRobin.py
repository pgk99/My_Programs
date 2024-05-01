from collections import deque

class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time

GanttChart = []

def round_robin(processes, quantum):
    queue = deque(processes)
    current_time = 0
    while queue:
        current_process = queue.popleft()
        execution_time = min(quantum, current_process.burst_time)
        GanttChart.append(current_process.pid)
        current_time += execution_time
        current_process.burst_time -= execution_time
        if current_process.burst_time > 0:
            queue.append(current_process)

if __name__ == "__main__":
    processes = [Process(1, 10), Process(2, 5), Process(3, 8), Process(4, 4)]
    quantum = 3
    round_robin(processes, quantum)
    print('Order of execution of processes : ')
    print(GanttChart)

