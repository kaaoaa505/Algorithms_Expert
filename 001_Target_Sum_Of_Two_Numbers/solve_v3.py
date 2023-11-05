# O(n Log(n)) time 
# O(1) space
values_array = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

def solve(values_array, target):
    values_array.sort()

    left_pointer = 0
    right_pointer = len(values_array) - 1

    while left_pointer < right_pointer:
        first_number = values_array[left_pointer]
        second_number = values_array[right_pointer]

        current_sum = first_number + second_number

        if current_sum == target:
            return {
                    'available': True,
                    'values': [first_number, second_number]
                }
        elif current_sum < target:
            left_pointer += 1
        elif current_sum > target:
            right_pointer -= 1
        
    return {
        'available': False,
        'values': []
    } 


result = solve(values_array, target)
print(result)