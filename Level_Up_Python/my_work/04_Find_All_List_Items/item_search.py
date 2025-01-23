def index_all(input_list, target):
    """
    Finds all indices of a target element in a nested list.

    Args:
        input_list (list): The list to search through, which may contain nested lists.
        target (any): The target element to search for.

    Returns:
        list of lists: A list of index paths where the target element is found.
                       Each path is represented as a list of indices.

    Example:
        >>> index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2)
        [[0, 0, 1], [0, 1], [1, 1]]
    """
    results = []  # Stores the paths (indices) of the target element.

    def find_indicies(sublist, current_path):
        """
        Recursively searches for the target in a (possibly nested) sublist.

        Args:
            sublist (list): The current list (or sublist) being searched.
            current_path (list): The path of indices leading to the current sublist.
        """
        for i in range(len(sublist)):
            element = sublist[i]  # Access the element at index i.
            if element == target:
                # If the element matches the target, append the path to results.
                results.append(current_path + [i])
            elif isinstance(element, list):
                # If the element is a list, recurse with the updated path.
                find_indicies(element, current_path + [i])

    # Start the recursive search with the initial list and an empty path.
    find_indicies(input_list, [])

    return results

# Example usage
print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))

# A more complex example
complex_list = [
    [1, 2, [3, 4, [5, 2], 6], 2],
    [2, [3, [2, [1, 2]]], [4, 2]],
    [[[[2]]], 7],
    [8, 9, [10, [11, 2]]]
]
print(index_all(complex_list, 2))
print(index_all(complex_list, 3))
