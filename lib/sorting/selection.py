from .base import Sort
from collections.abc import MutableSequence


class SelectionSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        for i in range(len(arr) - 1):
            min_val = arr[i]
            min_idx = i
            for j in range(i + 1, len(arr)):
                if arr[j] < min_val:
                    min_val = arr[j]
                    min_idx = j
            if i != min_idx:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]

        self.last_results = arr
        return arr
