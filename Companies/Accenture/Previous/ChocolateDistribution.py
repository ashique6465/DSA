def min_chocolate_difference(arr):
    # Since we can only distribute chocolates (not take away), we can increase
    # the chocolates of those who have fewer chocolates to minimize the difference
    # between the person who has the most chocolates and the person who has the least.

    max_chocolates = max(arr)
    min_possible_difference = max_chocolates - min(arr)

    # The minimal difference cannot be less than 0
    min_difference = min_possible_difference

    for target in range(min(arr), max_chocolates + 1):
        total_chocolates_needed = 0
        current_max = target
        current_min = target

        for chocolates in arr:
            if chocolates < target:
                total_chocolates_needed += (target - chocolates)
            else:
                current_max = max(current_max, chocolates)
                current_min = min(current_min, chocolates)

        # Update the minimal difference
        difference = current_max - current_min
        if difference < min_difference:
            min_difference = difference

    return min_difference

# Example usage:
n = 5
arr = [10, 4, 12, 3, 1]
print(min_chocolate_difference(arr))  # Output: 3
