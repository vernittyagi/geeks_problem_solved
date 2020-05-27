def rearrange(arr,n):
    for i in range(0,n-1,2):
        if arr[i+1]<arr[i]:
            arr[i+1],arr[i]=arr[i],arr[i+1]
    # if length is odd 
    if(n&1):
        for i in range(n-1,0,-2):
            if arr[i]>arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
            
def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    
# Driver code 
if __name__ == '__main__':
    arr = [3,2,6,1,5,9,4,8,7]
    n = len(arr)
    printList(arr)
    print()
    rearrange(arr,n)
    printList(arr)
