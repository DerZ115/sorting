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


class QuickSortDualPivot(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        self._partition(arr, 0, len(arr) - 1)

        self.last_results = arr
        return arr

    def _partition(self, arr: MutableSequence, left: int, right: int):
        if right > left:
            if arr[left] > arr[right]:
                arr[left], arr[right] = arr[right], arr[left]
            p, q = arr[left], arr[right]

            l, r = left + 1, right - 1
            k = l

            while k <= r:
                if arr[k] < p:
                    arr[l], arr[k] = arr[k], arr[l]
                    l += 1

                elif arr[k] >= q:
                    while arr[r] > q and k < r:
                        r -= 1
                    arr[k], arr[r] = arr[r], arr[k]
                    r -= 1

                    if arr[k] < p:
                        arr[l], arr[k] = arr[k], arr[l]
                        l += 1

                k += 1

            l -= 1
            r += 1

            arr[left], arr[l] = arr[l], arr[left]
            arr[right], arr[r] = arr[r], arr[right]

            self._partition(arr, left, l - 1)
            self._partition(arr, l + 1, r - 1)
            self._partition(arr, r + 1, right)


class QuickSortStable(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        self._partition(arr, 0, len(arr) - 1)

        self.last_results = arr
        return arr

    def _partition(self, arr: MutableSequence, lo: int, hi: int) -> None:
        if lo >= hi:
            return

        mid = (hi + lo) // 2
        piv = arr[mid]
        left, right = [], []

        for i in range(lo, hi + 1):
            if arr[i] < piv or (arr[i] == piv and i < mid):
                left.append(arr[i])
            elif arr[i] > piv or (arr[i] == piv and i > mid):
                right.append(arr[i])

        piv_new = lo + len(left)
        arr[piv_new] = piv
        arr[lo:piv_new] = left
        arr[piv_new+1:hi+1] = right

        del left, right

        self._partition(arr, lo, piv_new - 1)
        self._partition(arr, piv_new + 1, hi)
