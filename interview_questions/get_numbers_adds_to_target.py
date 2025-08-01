def two_sum_unique_pairs(arr, target):
    # Sort the array
    arr.sort()

    # List to store unique pairs
    result = []

    # Two pointers
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        # If we find a pair
        if current_sum == target:
            result.append((arr[left], arr[right]))

            # Move both pointers to look for new pairs
            left += 1
            right -= 1

            # Skip duplicate elements on both sides
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        # If the current sum is less than the target, move the left pointer to the right
        elif current_sum < target:
            left += 1
        # If the current sum is greater than the target, move the right pointer to the left
        else:
            right -= 1

    return result