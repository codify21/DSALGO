from typing import List


def find_boundary(arr: List[str]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left = 0
    right = len(arr) - 1
    mid = 0
    while left != right:
        mid = left + (right - left) // 2
        if arr[mid] == 'true':
            right = mid
        else:
            left = mid + 1

    if arr[left] == 'true':
        return left
    return -1


def binary_search(arr: List[str], target: int) -> int:
    left, right = 0, len(arr) - 1
    first_true_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]:
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return first_true_index


if __name__ == '__main__':
    arr = ['false', 'false', 'true', 'true', 'true']
    res = find_boundary(arr)
    print(res)

