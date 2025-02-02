def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def merge_k_lists(lists):
    num = len(lists)
    if num >= 2:
        merged_arr = merge(lists[0], lists[1])
        for i in range(2, num):
            merged_arr = merge(merged_arr, lists[i])
    return merged_arr

lists = [[1, 4, 5], [1, 3, 4], [2, 6], [1, 3, 7, 11, 15], [4, 8, 9, 12, 16, 17, 18]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)