from .base import Sort
from collections.abc import MutableSequence


class QuickSortLL(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        self._partition(arr, 0, len(arr)-1)

        self.last_results = arr
        return arr

    def _partition(self, arr: MutableSequence, lo, hi) -> None:
        if lo >= hi:
            return

        piv = arr[hi]
        i = lo

        for j in range(lo, hi):
            if arr[j] <= piv:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[hi], arr[i] = arr[i], arr[hi]

        self._partition(arr, lo, i - 1)
        self._partition(arr, i + 1, hi)


class QuickSortLR(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        self._partition(arr, 0, len(arr) - 1)

        self.last_results = arr
        return arr

    def _partition(self, arr: MutableSequence, lo: int, hi: int) -> None:
        if lo >= hi:
            return

        piv = arr[(hi + lo) // 2]
        i = lo
        j = hi

        while True:
            while arr[i] < piv:
                i += 1

            while arr[j] > piv:
                j -= 1

            if i >= j:
                self._partition(arr, lo, j - 1)
                self._partition(arr, j + 1, hi)
                return

            arr[i], arr[j] = arr[j], arr[i]
