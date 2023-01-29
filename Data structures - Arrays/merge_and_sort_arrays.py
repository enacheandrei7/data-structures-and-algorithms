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
    first_arr_item = first_arr[0]
    second_arr_item = second_arr[0]

    if len(first_arr) == 0 or len(second_arr) == 0:
        return first_arr + second_arr

    while i < len(first_arr) and j < len(second_arr):

        if first_arr_item <= second_arr_item:
            merged_arr.append(first_arr_item)
            i += 1
            first_arr_item = first_arr[i]
        elif second_arr_item < first_arr_item:
            merged_arr.append(second_arr_item)
            j += 1
            second_arr_item = second_arr[j]

    return merged_arr

print(merged_sorted_array([0, 3, 4, 31], [4, 6, 30]))