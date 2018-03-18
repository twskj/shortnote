arr = [29, 5, 19, 20, 27, 30, 10, 24, 19, 17]
print(arr)


def heapsort(arr):

    # fix = fix1 # min heap
    fix = fix2  # max heap
    # build heap
    for i in xrange(len(arr),-1,-1):
        fix(arr, len(arr), i)
    print arr
    # arr.append(55) <-- insert new value
    # fix(arr,len(arr),0) <-- recompile the heap
    # print(arr)

    # construct sorted values
    heap_size = len(arr)
    for i in range(heap_size - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        fix(arr, heap_size, 0)
    print arr

# min_heapify


def fix1(arr, size, index):

    minIdx = index
    offset = index * 2
    left = offset + 1
    right = offset + 2

    if left < size and arr[left] < arr[minIdx]:
        minIdx = left
    if right < size and arr[right] < arr[minIdx]:
        minIdx = right

    if minIdx != index:
        arr[minIdx], arr[index] = arr[index], arr[minIdx]
        fix1(arr, size, minIdx)

# max_heapify


def fix2(arr, size, index):
    maxIdx = index
    offset = index * 2
    left = offset + 1
    right = offset + 2

    if left < size and arr[left] > arr[maxIdx]:
        maxIdx = left
    if right < size and arr[right] > arr[maxIdx]:
        maxIdx = right

    if maxIdx != index:
        arr[maxIdx], arr[index] = arr[index], arr[maxIdx]
        fix2(arr, size, maxIdx)


heapsort(arr)
