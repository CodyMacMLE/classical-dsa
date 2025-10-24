
class Sort:
    @staticmethod
    def BubbleSort(arr):
        length = len(arr)

        if length <= 1:
            return arr

        for i in range(0, length - 1):
            for j in range(0, length - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j] = arr[j] ^ arr[j+1]
                    arr[j+1] = arr[j] ^ arr[j+1]
                    arr[j] = arr[j] ^ arr[j+1]

        return arr

    @staticmethod
    def InsertionSort(arr):
        length = len(arr)

        if length <= 1:
            return arr

        for i in range(1, length):
            current = arr.pop(i)
            for j in range(i, -1, -1):
                if j == 0 or current > arr[j-1]:
                    arr.insert(j, current)
                    break


        return arr

    @staticmethod
    def SelectionSort(arr):
        length = len(arr)

        if length <= 1:
            return arr

        i = 0
        while i < length:
            lowest = i
            for j in range(i, length - 1):
                if arr[j + 1] < arr[lowest]:
                    lowest = j + 1

            if lowest is not i:
                arr[i] = arr[i] ^ arr[lowest]
                arr[lowest] = arr[i] ^ arr[lowest]
                arr[i] = arr[i] ^ arr[lowest]

            i += 1
        return arr