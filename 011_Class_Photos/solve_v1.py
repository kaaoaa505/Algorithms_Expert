# Time Complexity: O(n log n)

# Space Complexity: O(n)

def class_photos(red_shirt_heights, blue_shirt_heights):
    # Ensure both lists have the same number of students
    if len(red_shirt_heights) != len(blue_shirt_heights):
        return {
            "is_valid": False,
            "front_row_color": None,
            "front_row_heights": [],
            "back_row_heights": []
        }
    
    # Sort both lists in descending order
    red_shirt_heights.sort(reverse=True)
    blue_shirt_heights.sort(reverse=True)

    # Determine which row should be in the front
    front_row_color = 'RED' if red_shirt_heights[0] < blue_shirt_heights[0] else 'BLUE'
    
    # Check the heights condition for each pair of students
    is_valid = True
    for i in range(len(red_shirt_heights)):
        red_height = red_shirt_heights[i]
        blue_height = blue_shirt_heights[i]

        if front_row_color == 'RED':
            if red_height >= blue_height:  # Front row should be shorter
                is_valid = False
                break
        else:
            if red_height <= blue_height:  # Front row should be shorter
                is_valid = False
                break

    # Prepare the front and back row heights
    if front_row_color == 'RED':
        front_row_heights = red_shirt_heights
        back_row_heights = blue_shirt_heights
    else:
        front_row_heights = blue_shirt_heights
        back_row_heights = red_shirt_heights

    # Return the results as a dictionary
    return {
        "is_valid": is_valid,
        "front_row_color": front_row_color,
        "front_row_heights": front_row_heights,
        "back_row_heights": back_row_heights
    }

# Example usage
red_shirts = [5, 8, 1, 3, 4]
blue_shirts = [6, 9, 2, 4, 5]

result = class_photos(red_shirts, blue_shirts)
print(result)
