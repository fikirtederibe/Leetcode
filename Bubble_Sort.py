n = int(input())
arr = [int(i) for i in input().strip().split(' ')]
numSwaps=0
for d in range(len(arr)):
    for k in range(1,len(arr)-d):
        if arr[k-1] > arr[k]:
            arr[k-1], arr[k] = arr[k], arr[k-1]
            numSwaps+=1
print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(arr[0]))
print("Last Element: " + str(arr[-1]))

