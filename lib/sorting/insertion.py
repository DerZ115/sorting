from .base import Sort
from math import ceil
from collections.abc import MutableSequence


class InsertionSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        for i in range(1, len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                else:
                    break

        return arr
    

class BinaryInsertionSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        for i in range(1, len(arr)):
            lo, hi = 0, i
            num = arr[i]

            while lo < hi:
                mid = (lo + hi) // 2
                if num < arr[mid]:
                    hi = mid
                else:
                    lo = mid + 1

            for j in range(i-1, lo-1, -1):
                arr[j+1] = arr[j]

            arr[lo] = num

        return arr


class ShellSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
    
    def _make_gaps(self, max_gap: int) -> list:
        gaps = [1]
        while True:
            gap = gaps[-1] * 2.25 + 1
            if gap > max_gap:
                break
            gaps.append(gap)
        return [ceil(gap) for gap in gaps[::-1]]
    
    def sort(self, arr: MutableSequence) -> MutableSequence:
        gaps = self._make_gaps(len(arr))

        for gap in gaps:
            for i in range(gap, len(arr)):
                val = arr[i]
                j = i

                while j >= gap and arr[j - gap] > val:
                    arr[j] = arr[j - gap]
                    j -= gap
                
                arr[j] = val

        return arr


class PatienceSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def _binary_search(self, piles, value):
        lo, hi = 0, len(piles)

        while lo < hi:
            mid = (lo + hi) // 2
            if value < piles[mid][-1]:
                hi = mid
            else:
                    lo = mid + 1
        
        return lo
    
    def _sift_down(self, heap, pos=0):
        root, end = pos, len(heap)

        while (child := 2 * root + 1) < end:
            if child + 1 < end and heap[child][0] > heap[child + 1][0]:
                child += 1
            
            if heap[root][0] > heap[child][0]:
                heap[root], heap[child] = heap[child], heap[root]
                root = child
            else:
                break

    def sort(self, arr: MutableSequence) -> MutableSequence:
        piles = []

        for i in range(len(arr)):
            val = arr[i]
            if len(piles) == 0:
                piles.append([val])
                continue
            
            p = self._binary_search(piles, val)
            if p == len(piles):
                piles.append([val])
            else:
                piles[p].append(val)

        queue = []

        for i, pile in enumerate(piles):
            if pile:
                val = pile.pop()
                queue.append((val, i))
        
        result = []

        while queue:
            val, i = queue[0]
            result.append(val)

            if piles[i]:
                new_val = piles[i].pop()
                queue[0] = (new_val, i)
            else:
                queue[0], queue[-1] = queue[-1], queue[0]
                queue.pop()

            self._sift_down(queue)

        return result      


class TreeSort(Sort):
    pass
