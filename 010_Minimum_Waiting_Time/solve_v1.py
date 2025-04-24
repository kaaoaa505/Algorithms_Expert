# Time Complexity: O(n log n)
# because of the sorting step.

# Space Complexity: O(1),
# because we only use a constant amount of extra space apart from the input list.


def solve(tasks):
    tasks.sort()

    wait_time = 0
    total_waiting_time = 0
    for i in range(len(tasks) - 1):
        wait_time += tasks[i]
        total_waiting_time += wait_time
    return total_waiting_time


tasks = [3, 2, 1, 2, 6]
print(solve(tasks))

# OUTPUT
# --------
# 17
