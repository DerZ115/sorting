from .base import Sort
from collections.abc import MutableSequence


class CountingSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        k = max(arr)
        length = len(arr)
        count = [0] * (k + 1)
        output = [None] * length

        for i in range(len(arr)):
            count[arr[i]] += 1
        
        for i in range(1, k+1):
            count[i] += count[i-1]

        for i in range(length-1, -1, -1):
            val = arr[i]
            count[val] -= 1

            output[count[val]] = val

        return output
    

class PigeonholeSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        min_val, max_val = min(arr), max(arr)

        k = max_val - min_val

        holes = [list() for _ in range(k+1)]

        for val in arr:
            i = val - min_val
            holes[i].append(val)

        output = []

        for hole in holes:
            output.extend(hole)

        return output

