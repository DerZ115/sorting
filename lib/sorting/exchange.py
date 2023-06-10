from collections.abc import MutableSequence

from .base import Sort


# noinspection DuplicatedCode
class BubbleSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        while True:
            is_sorted = True
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    is_sorted = False
            if is_sorted:
                break

        self.last_results = arr
        return arr


class OptBubbleSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        n = len(arr) - 1
        while n > 0:
            last_swap = 0
            for i in range(n):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    last_swap = i
            n = last_swap

        self.last_results = arr
        return arr


# noinspection DuplicatedCode
class CocktailSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        while True:
            is_sorted = True
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    is_sorted = False
            if is_sorted:
                break

            is_sorted = True
            for i in range(len(arr) - 1, 0, -1):
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
                    is_sorted = False
            if is_sorted:
                break

        self.last_results = arr
        return arr


class OptCocktailSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        start = 0
        end = len(arr) - 1
        while start < end:
            new_start = end
            new_end = start
            for i in range(start, end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    new_end = i
            end = new_end

            for i in range(end, start, -1):
                if arr[i - 1] > arr[i]:
                    arr[i - 1], arr[i] = arr[i], arr[i - 1]
                    new_start = i
            start = new_start

        self.last_results = arr
        return arr


class OddEvenSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        while True:
            is_sorted = True
            for i in range(1, len(arr) - 1, 2):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    is_sorted = False

            for i in range(0, len(arr) - 1, 2):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    is_sorted = False

            if is_sorted:
                break

        self.last_results = arr
        return arr


class GnomeSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        i = 0
        while i < len(arr):
            if i == 0 or arr[i] >= arr[i - 1]:
                i += 1
            else:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                i -= 1

        self.last_results = arr
        return arr


class OptGnomeSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        for i in range(1, len(arr)):
            j = i
            while j > 0 and arr[j] < arr[j - 1]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1

        self.last_results = arr
        return arr


class BinaryGnomeSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                low = 0
                high = i
                while low < high:
                    j = (low + high) // 2
                    if arr[i] < arr[j]:
                        high = j
                    else:
                        low = j + 1

                for j in range(i, low, -1):
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]

        self.last_results = arr
        return arr


class ExchangeSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

        self.last_results = arr
        return arr


class CombSort(Sort):
    def __init__(self, k: float = 1.3, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.k = k

    def sort(self, arr: MutableSequence) -> MutableSequence:
        gap = len(arr)
        is_sorted = False
        while not is_sorted:
            gap = int(gap / self.k)
            if gap <= 1:
                gap = 1
                is_sorted = True

            for i in range(len(arr) - gap):
                if arr[i] > arr[i + gap]:
                    arr[i], arr[i + gap] = arr[i + gap], arr[i]
                    is_sorted = False
        return arr


class CircleSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def _inner_circle(self, arr: MutableSequence, i0: int, j0: int) -> int:
        s = 0
        i = i0
        j = j0

        if i0 == j0:
            return 0

        while i < j:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                s += 1
            i += 1
            j -= 1

        if i - j == 1:  # To include middle item in odd-length lists
            i -= 1
            j += 1

        s += self._inner_circle(arr, i0=i0, j0=i)
        s += self._inner_circle(arr, i0=j, j0=j0)

        return s

    def sort(self, arr: MutableSequence) -> MutableSequence:
        while self._inner_circle(arr, 0, len(arr) - 1):
            pass

        self.last_results = arr
        return arr
