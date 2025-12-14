def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    target_1 = 7
    target_2 = 10

    print(f"List: {my_list}")
    print(f"Target {target_1} found at index: {binary_search(my_list, target_1)}")
    print(f"Target {target_2} found at index: {binary_search(my_list, target_2)}")
