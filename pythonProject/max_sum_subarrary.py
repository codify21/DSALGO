
def maxSubArray(nums):
    window_size=0
    max_sum_array=nums[0]

    for i in nums:
        window_size = window_size+max_sum_array
        max_sum_array = max(max_sum_array,window_size)

        if window_size<0:
            window_size=0


    return max_sum


if __name__ == '__main__':
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    res = maxSubArray(arr)
    print(res)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None




        pos=0
        temp=head
        checkList={}

        while temp :
            if temp in checkList.keys():
                return temp

            checkList[temp]=pos
            temp=temp.next
            pos=pos+1

        return None

#
