# O(nlogn) time 
# O(n) space
input_array = [-7,-5,-4,3,6,8,9]

def solve(input_array):
    target_array = [0 for _ in input_array]

    for input_index in range(len(input_array)):
        target_array[input_index] = abs(input_array[input_index]) ** 2

    target_array.sort()

    return {
        'input': input_array,
        'output': target_array
    } 

result = solve(input_array)

print(result)