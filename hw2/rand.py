"""Module allows for generating random arrays and sorting it"""
import subprocess


def random_array(arr):
    """
    This function shuffles an array to randomize it. This allows merge sort to sort it.

    Args:
        arr (list): A list of elements to shuffle.

    Returns:
        list: Returns the sorted list of elements.
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True, check="False")
        arr[i] = int(shuffled_num.stdout)
    return arr
