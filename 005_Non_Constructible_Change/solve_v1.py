# ⏱ Time Complexity:
# Sorting the coins → O(n log n)
# This is the dominant step. Sorting takes O(n log n) time.
# Looping through the coins → O(n)
# Each coin is processed once.

# ✔️ Overall Time Complexity:
# O(n log n), where n is the number of coins.

# 🧠 Space Complexity:
# Sorting uses space:
# Python’s .sort() is in-place for lists → O(1) extra space.

# Other variables:
# current_change_created is just a single integer → O(1) space.


def solve(coins):
    coins.sort()
    current_change_created = 0

    for coin in coins:
        if coin > current_change_created + 1:
            return current_change_created + 1
        current_change_created += coin

    return current_change_created + 1


print(solve([1, 2, 5]))  # ➞ 4
print(solve([1, 1, 1, 1, 1]))  # ➞ 6
print(solve([2]))  # ➞ 1
print(solve([1, 1, 2, 3, 5, 7, 22]))  # ➞ 20
print(solve([1, 1, 3]))  # ➞ 6
print(solve([1, 1, 4]))  # ➞ 3
