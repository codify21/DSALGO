def findMin(arr):
    start = arr[0]
    index = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] > start:
            left = mid + 1
        elif arr[mid] < start:
            index = mid
            start = arr[mid]
            right = mid - 1
        else:
            start = arr[left]  # storing the number
            index = left  # storing the index
            left = left + 1

    return start

if __name__ == '__main__':
    arr = [10,1,10,10,10,10]
    res = findMin(arr)
    print(res)


    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            a = []
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        a.append(i)
                        a.append(j)

                        return a

