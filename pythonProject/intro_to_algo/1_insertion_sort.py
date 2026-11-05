


def insertion_sort(arr):

    for i in range(1,len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            temp= arr[j]
            arr[j]=arr[j-1]
            arr[j-1]=temp
            j=j-1
    return arr

def insertion_sort_2(arr):

    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

nums = [23,0,-2,43,10,-5,46]

# print(insertion_sort(nums.copy()))
print(insertion_sort_2(nums.copy()))

def decreasing_insertion_sort_(arr):

    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]<key:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr


nums = [23,0,-2,43,10,-5,46]

print(decreasing_insertion_sort_(nums.copy()))


