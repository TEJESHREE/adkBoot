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

# Detailed Explanation of Binary Search

Binary search is an efficient algorithm for finding an item from a *sorted* list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

## How it works:
1.  **Start with the entire list**: Define two pointers, `left` at the beginning of the list (index 0) and `right` at the end of the list (index `len(arr) - 1`).
2.  **Find the middle element**: Calculate the middle index `mid = (left + right) // 2`.
3.  **Compare**:
    *   If the element at `mid` is the `target`, you've found it! Return `mid`.
    *   If the element at `mid` is *less than* the `target`, it means the target (if it exists) must be in the right half of the current sub-list. So, discard the left half by moving `left = mid + 1`.
    *   If the element at `mid` is *greater than* the `target`, it means the target (if it exists) must be in the left half of the current sub-list. So, discard the right half by moving `right = mid - 1`.
4.  **Repeat**: Continue steps 2 and 3 until `left` is greater than `right`. If the loop finishes and the target hasn't been found, it means the target is not in the list, so return -1.

## Dry Run Example:

Let's trace `binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17], 7)`:

`arr = [1, 3, 5, 7, 9, 11, 13, 15, 17]`
`target = 7`

**Iteration 1:**
*   `left = 0`, `right = 8`
*   `mid = (0 + 8) // 2 = 4`
*   `arr[mid]` (i.e., `arr[4]`) is `9`.
*   `9 > 7` (`arr[mid] > target`), so the target must be in the left half.
*   Update `right = mid - 1 = 4 - 1 = 3`.
*   New range: `left = 0`, `right = 3` (sub-list: `[1, 3, 5, 7]`)

**Iteration 2:**
*   `left = 0`, `right = 3`
*   `mid = (0 + 3) // 2 = 1`
*   `arr[mid]` (i.e., `arr[1]`) is `3`.
*   `3 < 7` (`arr[mid] < target`), so the target must be in the right half.
*   Update `left = mid + 1 = 1 + 1 = 2`.
*   New range: `left = 2`, `right = 3` (sub-list: `[5, 7]`)

**Iteration 3:**
*   `left = 2`, `right = 3`
*   `mid = (2 + 3) // 2 = 2`
*   `arr[mid]` (i.e., `arr[2]`) is `5`.
*   `5 < 7` (`arr[mid] < target`), so the target must be in the right half.
*   Update `left = mid + 1 = 2 + 1 = 3`.
*   New range: `left = 3`, `right = 3` (sub-list: `[7]`)

**Iteration 4:**
*   `left = 3`, `right = 3`
*   `mid = (3 + 3) // 2 = 3`
*   `arr[mid]` (i.e., `arr[3]`) is `7`.
*   `7 == 7` (`arr[mid] == target`), target found!
*   Return `mid`, which is `3`.
