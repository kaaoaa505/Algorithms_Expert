# Minimum Waiting Time Algorithm 
- is a greedy strategy used to minimize the total waiting time for a series of tasks or processes, like in a queue. 
- This is especially common in scenarios like scheduling jobs on a single processor.

# 🔍 Problem:
- You are given a list of times it takes to complete each task. 
- You want to arrange the tasks in such a way that the total waiting time is minimized.

# ⏳ Key Concept:
- Waiting time for a task is the sum of the durations of all the previous tasks before it.
- The idea is to sort tasks in ascending order so that shorter tasks go first, which reduces the cumulative waiting time.

# Example:
    
    [3,2,1,2,6]

# 🔢 Step-by-step:
- Sort the list:

        [1, 2, 2, 3, 6]

- Calculate individual waiting times.

        Task 1: Wait time = 0

        Task 2: Wait time = 1

        Task 3: Wait time = 1 + 2 = 3

        Task 4: Wait time = 1 + 2 + 2 = 5

        Task 5: Wait time = 1 + 2 + 2 + 3 = 8

- ignore the last task, since no one waits after it.

# 🧠 Final Answer:
- The minimum total waiting time for [3, 2, 1, 2, 6] is 17.