"""
For the input list [1, 2, 3], the permutations are:

[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
"""


def gene_permutations(arr):
    # Base case: if the list is empty or has one element, return that list
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [arr]

    # List to store permutations
    permutations = []

    # Iterate through the list and recursively find permutations
    for i in range(len(arr)):
        # Extract the current element
        current = arr[i]
        # Remaining elements
        remaining = arr[:i] + arr[i + 1:]

        # Recursively find permutations of the remaining elements
        for p in gene_permutations(remaining):
            # Add current element to the front of each permutation
            permutations.append([current] + p)

    return permutations


if __name__ == '__main__':
    lst = [1, 2, 3]
    gene_permutations(lst)