def merge(arr , p ,q, r):
    arr1 = arr[p:q]
    arr2 = arr[q:r]

    i,j,k=0,0,p
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            i= i+1
        else:
            arr[k]=arr2[j]
            j=j+1
        k=k+1
    while i<len(arr1):
        arr[k]= arr1[i]
        i+=1
        k=k+1
    while j<len(arr1):
        arr[k]= arr2[j]
        j+=1
        k=k+1

    return arr

def merge_sort(arr,p,r):
    if r - p <= 1:
        return arr

    q =(p+r)//2

    merge_sort(arr,p,q)
    merge_sort(arr,q,r)

    return merge(arr,p,q,r)

arry = [10,8,3,2,1,6,-1,0,11,0]
p=0
r = len(arry)
print("sorted array after merge sort :",merge_sort(arry,p,r))