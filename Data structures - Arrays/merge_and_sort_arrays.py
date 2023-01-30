"""
Merge 2 arrays and sorts them
"""

def merged_sorted_array(first_arr, second_arr):
    """
    Merge 2 sorted arrays and keeps them sorted
    """
    merged_arr = []
    i = 0
    j = 0

    if len(first_arr) == 0 or len(second_arr) == 0:
        return first_arr + second_arr

    while i < len(first_arr) and j < len(second_arr):

        if first_arr[i] <= second_arr[j]:
            merged_arr.append(first_arr[i])
            i += 1
        elif second_arr[j] < first_arr[i]:
            merged_arr.append(second_arr[j])
            j += 1
    return merged_arr + first_arr[i:] + second_arr[j:]

print(merged_sorted_array([0, 3, 4, 31, 32], [4, 6, 30, 35]))
