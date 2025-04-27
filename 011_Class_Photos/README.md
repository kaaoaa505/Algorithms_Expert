## Function: `Class Photos`

This function checks the validity of an arrangement for students in two rows for a class photo, based on their heights. It assumes there are two groups of students, one wearing red shirts and the other wearing blue shirts. The goal is to arrange the students such that the front row is always shorter than the back row.

### Parameters
- `red_shirt_heights`: A list of heights for the students in red shirts.
- `blue_shirt_heights`: A list of heights for the students in blue shirts.

### Function Logic

1. **Input Validation**:
   - The function first ensures that the two input lists (`red_shirt_heights` and `blue_shirt_heights`) have the same number of students. If the lists have different lengths, the function returns a dictionary indicating that the arrangement is invalid.
   
2. **Sorting Heights**:
   - Both the `red_shirt_heights` and `blue_shirt_heights` lists are sorted in **descending order**. This helps to easily determine which group has taller students, making it easier to determine the front and back rows.

3. **Determine Front Row Color**:
   - The function then determines which group should be in the front row. If the tallest student in the red group is shorter than the tallest student in the blue group, the front row will be the red-shirted students, otherwise, the blue-shirted students will be in the front row.

4. **Height Validation**:
   - After sorting, the function checks whether the heights meet the condition for the front row. The condition is that the front row should have shorter students than the back row. If this condition is violated at any point (i.e., a student in the front row is taller than or equal to a student in the back row), the arrangement is marked as invalid.

5. **Prepare Front and Back Row Heights**:
   - Depending on which group is determined to be in the front row, the function assigns the respective heights to `front_row_heights` and `back_row_heights`.

6. **Return Results**:
   - Finally, the function returns a dictionary with the following keys:
     - `is_valid`: A boolean indicating whether the arrangement is valid or not.
     - `front_row_color`: The color of the shirts in the front row (`'RED'` or `'BLUE'`).
     - `front_row_heights`: A list of the heights for the students in the front row.
     - `back_row_heights`: A list of the heights for the students in the back row.

### Example Usage

```python
red_shirts = [5, 8, 1, 3, 4]
blue_shirts = [6, 9, 2, 4, 5]

result = class_photos(red_shirts, blue_shirts)
print(result)
