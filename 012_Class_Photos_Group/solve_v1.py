def arrange_class_photo_with_rows(red_shirts, blue_shirts):
    # Sort both groups by height
    red_shirts.sort()
    blue_shirts.sort()

    # Find the split index (half the number of students)
    n = len(red_shirts)  # Same length for red_shirts and blue_shirts
    
    # Front row is the first half, back row is the second half
    red_front = red_shirts[:n//2]  # Shorter students in red shirts (front row)
    red_back = red_shirts[n//2:]   # Taller students in red shirts (back row)
    
    blue_front = blue_shirts[:n//2]  # Shorter students in blue shirts (front row)
    blue_back = blue_shirts[n//2:]   # Taller students in blue shirts (back row)

    # Return the rows
    return red_front, red_back, blue_front, blue_back

# Example usage
red_shirts = [5, 8, 1, 3, 4]
blue_shirts = [6, 9, 2, 4, 5]

red_front, red_back, blue_front, blue_back = arrange_class_photo_with_rows(red_shirts, blue_shirts)

print("Red shirts front row (shorter students):", red_front)
print("Red shirts back row (taller students):", red_back)
print("Blue shirts front row (shorter students):", blue_front)
print("Blue shirts back row (taller students):", blue_back)
