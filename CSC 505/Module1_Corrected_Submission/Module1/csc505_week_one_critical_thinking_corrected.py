import random

def random_list():
    """
    Generate a list of 10 random integers between 1 and 100.
    Returns:
        list[int]: A list of random integers.
    """
    return [random.randint(1, 100) for _ in range(10)]

def sort_list(lst):
    """
    Sort a list of integers in ascending order.

    Args:
        lst (list[int]): The list to sort.

    Returns:
        list[int]: A sorted list.
    """
    return sorted(lst)

# Main execution
if __name__ == "__main__":
    random_numbers = random_list()
    print("Random List:", random_numbers)

    # Sort the list
    sorted_numbers = sort_list(random_numbers)
    print("Sorted List:", sorted_numbers)
