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


class DoubleSelectionSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        left = 0
        right = len(arr) - 1

        while left <= right:
            lo = left
            hi = right
            for i in range(left, right + 1):
                if arr[i] < arr[lo]:
                    lo = i
                if arr[i] > arr[hi]:
                    hi = i

            if hi == left:
                hi = lo

            arr[left], arr[lo] = arr[lo], arr[left]
            arr[right], arr[hi] = arr[hi], arr[right]

            left += 1
            right -= 1

        self.last_results = arr
        return arr


class CycleSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        for start in range(len(arr) - 1):
            item = arr[start]

            new_pos = start
            for i in range(start + 1, len(arr)):
                if arr[i] < item:
                    new_pos += 1

            if new_pos == start:
                continue

            while item == arr[new_pos]:
                new_pos += 1

            arr[new_pos], item = item, arr[new_pos]

            while new_pos != start:
                new_pos = start
                for i in range(start + 1, len(arr)):
                    if arr[i] < item:
                        new_pos += 1
                while item == arr[new_pos]:
                    new_pos += 1

                arr[new_pos], item = item, arr[new_pos]

        return arr


class HeapSortMax(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        end = len(arr)
        start = end // 2

        while end > 1:
            if start > 0:
                start -= 1
            else:
                end -= 1
                arr[0], arr[end] = arr[end], arr[0]

            root = start

            while (child := 2 * root + 1) < end:
                if child + 1 < end and arr[child] < arr[child + 1]:
                    child += 1

                if arr[root] < arr[child]:
                    arr[root], arr[child] = arr[child], arr[root]
                    root = child

                else:
                    break

        return arr


class HeapSortMin(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        end = len(arr)
        start = end // 2

        while end > 1:
            if start > 0:
                start -= 1
            else:
                end -= 1
                arr[0], arr[end] = arr[end], arr[0]

            root = start

            while (child := 2 * root + 1) < end:
                if child + 1 < end and arr[child] > arr[child + 1]:
                    child += 1

                if arr[root] > arr[child]:
                    arr[root], arr[child] = arr[child], arr[root]
                    root = child

                else:
                    break

        arr.reverse()

        return arr


class HeapSortMinFlipped(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        length = len(arr)
        end = 0
        start = (length - 1) // 2

        while end < length - 1:
            if start < length - 1:
                start += 1
            else:
                arr[-1], arr[end] = arr[end], arr[-1]
                end += 1

            root = start

            while (child := length - 2 * (length - root)) >= end:
                if child - 1 >= end and arr[child] > arr[child - 1]:
                    child -= 1

                if arr[root] > arr[child]:
                    arr[root], arr[child] = arr[child], arr[root]
                    root = child

                else:
                    break

        return arr


class WeakHeapSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        if len(arr) <= 1:
            return arr

        reverse = [False] * len(arr)

        for child in range(len(arr)-1, 0, -1):
            root = child

            while root & 1 == reverse[root >> 1]:
                root >>= 1
            ancestor = root >> 1

            if arr[ancestor] < arr[child]:
                reverse[child] = not reverse[child]
                arr[ancestor], arr[child] = arr[child], arr[ancestor]

        for i in range(len(arr)-1, 1, -1):
            arr[0], arr[i] = arr[i], arr[0]

            x = 1
            while (y := 2 * x + reverse[x]) < i:
                x = y

            while x > 0:
                if arr[0] < arr[x]:
                    reverse[x] = not reverse[x]
                    arr[0], arr[x] = arr[x], arr[0]
                x >>= 1

        arr[0], arr[1] = arr[1], arr[0]

        return arr


class TernaryHeapSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        end = len(arr)
        start = end // 3 + 1

        while end > 1:
            if start > 0:
                start -= 1
            else:
                end -= 1
                arr[0], arr[end] = arr[end], arr[0]

            root = start

            while (left := 3 * root + 1) < end:
                middle = 3 * root + 2
                right = 3 * root + 3

                child = left
                if middle < end and arr[child] < arr[middle]:
                    child = middle
                if right < end and arr[child] < arr[right]:
                    child = right

                if arr[root] < arr[child]:
                    arr[root], arr[child] = arr[child], arr[root]
                    root = child

                else:
                    break

        return arr


class SmoothSort(Sort):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._leonardo_nums = None

    def _make_leonardo_nums(self, length):
        self._leonardo_nums = [1, 1]
        while self._leonardo_nums[-1] < length:
            self._leonardo_nums.append(self._leonardo_nums[-2] + self._leonardo_nums[-1] + 1)



    def _sift_down(self, arr, root, shift):
        root_val = arr[root]
        while shift > 1:
            child_r = root - 1
            child_l = root - 1 - self._leonardo_nums[shift - 2]

            if root_val >= arr[child_r] and root_val >= arr[child_l]:
                break
            elif arr[child_r] < arr[child_l]:
                arr[root] = arr[child_l]
                root = child_l
                shift -= 1
            else:
                arr[root] = arr[child_r]
                root = child_r
                shift -= 2

        arr[root] = root_val

    def sort(self, arr):
        if len(arr) < 2:
            return arr

        self._make_leonardo_nums(len(arr))

        shape = 1
        shift = 1

        start = 0
        end = len(arr) - 1
        root = start

        while root < end:
            if shape & 3 == 3:
                self._sift_down(arr, root, shift)







