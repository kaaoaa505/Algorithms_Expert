# O(n) time 
# O(n) space
input_array = [-7,-5,-4,3,6,8,9]

def solve(input_array):
    target_array = [0 for _ in input_array]

    smallest_index = 0
    largest_index = len(input_array) - 1
    target_index = largest_index

    while largest_index >= smallest_index:
        if abs(input_array[largest_index]) > abs(input_array[smallest_index]):
            target_array[target_index] = abs(input_array[largest_index])**2
            largest_index -= 1
        else:
            target_array[target_index] = abs(input_array[smallest_index])**2
            smallest_index += 1

        target_index -= 1

    return {
        'input': input_array,
        'output': target_array
    } 

result = solve(input_array)

print(result)