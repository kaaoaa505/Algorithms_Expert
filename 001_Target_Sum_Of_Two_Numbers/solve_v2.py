# O(n^2) time 
# O(1) space
values_array = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

def solve(values_array, target):
    for i in range(len(values_array) - 1):
        first_number = values_array[i]

        for j in range(i + 1, len(values_array)):
            second_number = values_array[j]

            if first_number + second_number == target:
                return {
                    'available': True,
                    'values': [first_number, second_number]
                }
        
    return {
        'available': False,
        'values': []
    } 


result = solve(values_array, target)
print(result)