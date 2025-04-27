### Algorithm Description: `Arrange Class Photos`

The function `arrange_class_photo_with_rows` is designed to arrange a group of students wearing red and blue shirts into two rows based on their height. The goal is to create two rows for each shirt color: one for shorter students (front row) and one for taller students (back row).

Here's how the algorithm works:

1. **Input Parameters:**
   - `red_shirts`: A list of integers representing the heights of students wearing red shirts.
   - `blue_shirts`: A list of integers representing the heights of students wearing blue shirts.

2. **Sorting Heights:**
   - Both the `red_shirts` and `blue_shirts` lists are sorted in increasing order based on the heights of the students. This ensures that the students are ordered from shortest to tallest within each color group.

3. **Splitting the Groups:**
   - The function assumes both lists (`red_shirts` and `blue_shirts`) have the same number of students. The number of students is stored in `n` (length of one of the lists, since both have the same size).
   - The sorted `red_shirts` and `blue_shirts` lists are divided into two halves:
     - **Front row**: The first half of the students (shorter students).
     - **Back row**: The second half of the students (taller students).

4. **Returning the Rows:**
   - The function returns four lists:
     - `red_front`: Shorter students in red shirts (front row).
     - `red_back`: Taller students in red shirts (back row).
     - `blue_front`: Shorter students in blue shirts (front row).
     - `blue_back`: Taller students in blue shirts (back row).

### Example Execution:

Given two lists:
```python
red_shirts = [5, 8, 1, 3, 4]
blue_shirts = [6, 9, 2, 4, 5]
```

1. After sorting:
   - `red_shirts` becomes: `[1, 3, 4, 5, 8]`
   - `blue_shirts` becomes: `[2, 4, 5, 6, 9]`

2. The students are split into two groups for each shirt color:
   - **Red front row** (shorter): `[1, 3]`
   - **Red back row** (taller): `[4, 5, 8]`
   - **Blue front row** (shorter): `[2, 4]`
   - **Blue back row** (taller): `[5, 6, 9]`

3. The function returns these groups:
   ```python
   return ([1, 3], [4, 5, 8], [2, 4], [5, 6, 9])
   ```

### Example Output:
```python
Red shirts front row (shorter students): [1, 3]
Red shirts back row (taller students): [4, 5, 8]
Blue shirts front row (shorter students): [2, 4]
Blue shirts back row (taller students): [5, 6, 9]
```

### Summary:
This function efficiently arranges the students into two rows per shirt color by sorting and splitting them based on their height, ensuring the shorter students are in the front and the taller students are in the back.