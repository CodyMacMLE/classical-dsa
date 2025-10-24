### Time Complexity

#### 1) Bubble Sort
```python
@staticmethod
def BubbleSort(arr):                    
    length = len(arr)                           # 1 assign, 1 func call

    if length <= 1:                             # 1 comparison                                          Not Worst Case
        return arr                              # 1 return                                              Not Worst Case

    for i in range(0, length - 1):              # 1 func call, n loops
        for j in range(0, length - i - 1):      # n(1 func call, n - 1 loops)
            if arr[j] > arr[j+1]:               # n^2 - n(1 comparison, 2 indexes, 1 addition)
                arr[j] = arr[j] ^ arr[j+1]      # n^2 - n(1 assign, 2 indexes, 1 addition, 1 bitwise)
                arr[j+1] = arr[j] ^ arr[j+1]    # n^2 - n(1 assign, 2 indexes, 2 additions, 1 bitwise)
                arr[j] = arr[j] ^ arr[j+1]      # n^2 - n(1 assign, 2 indexes, 1 addition, 1 bitwise)

    return arr                                  # 1 return
```
$ T(n) = 1 + 1 + 1 + n + n(1 + n - 1) + 4(n^2 - n) + 5(n^2 - n) + 6(n^2 - n) + 5(n^2 - n) + 1$ <br>
$ T(n) = 4 + n + n + n^2 - n + 4n^2 - 4n + 5n^2 - 5n + 6n^2 - 6n + 5n^2 - 5n$ <br>
$ T(n) = 4 - 19n + 21n^2$

$ O(n^2) $

#### 2) Insertion Sort
```python
@staticmethod
def InsertionSort(arr):
    length = len(arr)                           # 1 assign, 1 func call          

    if length <= 1:                             # 1 comparison                                          Not Worst Case
        return arr                              # 1 return                                              Not Worst Case

    for i in range(1, length):                  # n loops, 1 func call
        current = arr.pop(i)                    # n(1 assign, 1 func call)
        for j in range(i, -1, -1):              # n(n-1 loops, 1 func call)
            if j is 0 or current > arr[j-1]:    # (n^2-n)(2 comparisons, 1 or, 1 subtraction)
                arr.insert(j, current)          # (n^2-n)(1 func call)
                break                           # (n^2-n)(1 func call)


    return arr                                  # 1 return
```
$ T(n) = 1 + 1 + 1 + n + 2n + n^2 - n + n + 4(n^2-n) + (n^2-n) + (n^2-n) + 1$ <br>
$ T(n) = 4 - 3n + 7n^2$ <br>

$ O(n^2) $

#### 3) Selection Sort
```python
@staticmethod
def SelectionSort(arr):
    length = len(arr)                               # 1 assign, 1 func call 

    if length <= 1:                                 # 1 comparison                                          Not Worst Case
        return arr                                  # 1 return                                              Not Worst Case

    i = 0                                           # 1 assignment
    while i < length:                               # n loops
        lowest = i                                  # 1 assignment for n loops
        for j in range(i, length - 1):              # 1 func call, 1 subtraction, n loops for n loops
            if arr[j + 1] < arr[lowest]:            # n^2(2 index, 1 comparison)
                lowest = j + 1                      # n^2(1 assignment, 1 addition)

        if lowest is not i:                         # 1 comparison n loops
            arr[i] = arr[i] ^ arr[lowest]           # 1 assignment, 2 indexes, 1 bitwise xor n loops
            arr[lowest] = arr[i] ^ arr[lowest]      # 1 assignment, 2 indexes, 1 bitwise xor n loops
            arr[i] = arr[i] ^ arr[lowest]           # 1 assignment, 2 indexes, 1 bitwise xor n loops

        i += 1                                      # 1 addition, 1 assignment n loops
    return arr                                      # 1 return
```
$ T(n) = 2 + 1 + n + n + 2n + n^2 + 3n^2 + 2n^2 + n + 4n + 4n +4n + 2n + 1$ <br>
$ T(n) = 4 + 19n + 6n^2$ <br>

$ O(n^2) $