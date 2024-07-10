# O(n) time 
# O(1) space
main_array = [5, 1, 22, 25, 6, -1, 8, 10]
subsequence_array = [1, 6, -1, 10]

def solve(main_array, subsequence_array):
    main_array_index = 0
    subsequence_array_index = 0

    while(main_array_index < len(main_array) and subsequence_array_index < len(subsequence_array)):
        if(main_array[main_array_index] == subsequence_array[subsequence_array_index]):
            subsequence_array_index += 1

        if(subsequence_array_index == len(subsequence_array)):
            return {
                    'available': True,
                    'values': subsequence_array
                }

        main_array_index += 1

    return {
        'available': False,
        'values': []
    } 

result = solve(main_array, subsequence_array)

print(result)