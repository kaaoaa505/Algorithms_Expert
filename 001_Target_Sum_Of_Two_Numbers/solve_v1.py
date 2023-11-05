# O(n) time 
# O(n) space
values_array = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10

def solve(values_array, target):
    hash_array = []

    for element in values_array:
        required_match = target - element

        if required_match in hash_array:
            return {
                'available': True,
                'values': [element, required_match]
            }
        
        hash_array.append(element)
        
    return {
        'available': False,
        'values': []
    } 

result = solve(values_array, target)
print(result)