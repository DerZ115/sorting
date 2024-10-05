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
    # Precomputed Leonardo numbers up to 2^64
    leonardo_nums = [1, 1, 3, 5, 9, 15, 25, 41, 67, 109, 177, 287, 465, 753, 
                     1219, 1973, 3193, 5167, 8361, 13529, 21891, 35421, 57313, 
                     92735, 150049, 242785, 392835, 635621, 1028457, 1664079, 
                     2692537, 4356617, 7049155, 11405773, 18454929, 29860703, 
                     48315633, 78176337, 126491971, 204668309, 331160281, 
                     535828591, 866988873, 1402817465, 2269806339, 3672623805, 
                     5942430145, 9615053951, 15557484097, 25172538049, 
                     40730022147, 65902560197, 106632582345, 172535142543, 
                     279167724889, 451702867433, 730870592323, 1182573459757, 
                     1913444052081, 3096017511839, 5009461563921, 8105479075761, 
                     13114940639683, 21220419715445, 34335360355129, 
                     55555780070575, 89891140425705, 145446920496281, 
                     235338060921987, 380784981418269, 616123042340257, 
                     996908023758527, 1613031066098785, 2609939089857313, 
                     4222970155956099, 6832909245813413, 11055879401769513, 
                     17888788647582927, 28944668049352441, 46833456696935369, 
                     75778124746287811, 122611581443223181, 198389706189510993, 
                     321001287632734175, 519390993822245169, 840392281454979345, 
                     1359783275277224515, 2200175556732203861, 
                     3559958832009428377, 5760134388741632239, 
                     9320093220751060617, 15080227609492692857, 
                     24400320830243753475]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _sift_down(self, arr, root, shift):
        root_val = arr[root]
        while shift > 1:
            child_r = root - 1
            child_l = root - 1 - self.leonardo_nums[shift - 2]

            if arr[child_r] > arr[child_l]:
                largest_child = child_r
                shift -= 2
            else:
                largest_child = child_l
                shift -= 1

            if root_val >= arr[largest_child]:
                break
            else:
                arr[root] = arr[largest_child]
                root = largest_child

        arr[root] = root_val

    def _trickle_down(self, arr, root, shape, shift):
        while True:  
            if root == self.leonardo_nums[shift] - 1: # First heap --> Done
                break
            
            i_to_compare = root

            if shift > 1:
                child_r = root - 1
                child_l = root - 1 - self.leonardo_nums[shift - 2]
                largest_child = max(child_r, child_l, key=lambda x: arr[x])

                if arr[largest_child] > arr[i_to_compare]:
                    i_to_compare = largest_child

            prior_root = root - self.leonardo_nums[shift]

            if arr[prior_root] <= arr[i_to_compare]:
                break

            arr[root], arr[prior_root] = arr[prior_root], arr[root]
            root = prior_root

            while True:
                shape >>= 1
                shift += 1
                if shape & 1 == 1:
                    break

        self._sift_down(arr, root, shift)

    def _build_heap(self, arr, start, end):
        shape = 1
        shift = 1

        for root in range(start+1, end+1):
            # Insert the next element into the heap
            if shape & 3 == 3:
                # Combine the two smallest heaps
                shape = (shape >> 2) + 1
                shift += 2
            elif shift == 1:
                # Add a new l0 heap
                shape = (shape << 1) + 1
                shift = 0
            else:
                # Add a new l1 heap
                shape = (shape << (shift - 1)) + 1
                shift = 1

            # Check if the current heap is in its final position
            is_final = False
            if shift == 0:
                if root == end:
                    is_final = True
            elif shift == 1:
                if root == end or (root == end - 1 and shape & 2 != 1):
                    is_final = True
            elif end - root < self.leonardo_nums[shift - 1] + 1:
                is_final = True

            if is_final:
                self._trickle_down(arr, root, shape, shift)
            else:
                self._sift_down(arr, root, shift)

        return shape, shift
    
    def _remove_last(self, arr, root, shape, shift):
        if shift <= 1:
            while True:
                shape >>= 1
                shift += 1
                if shape == 0 or shape & 1 == 1:
                    return shape, shift
        
        removed_tree_order = shift
        shape &= ~1
        shape <<= 2
        shape |= 3
        shift -= 2

        child_r = root - 1
        child_l = root - 1 - self.leonardo_nums[removed_tree_order - 2]

        self._trickle_down(arr, child_l, shape >> 1, shift + 1)
        self._trickle_down(arr, child_r, shape, shift)

        return shape, shift

    def sort(self, arr):
        if len(arr) < 2:
            return arr
        
        start = 0
        end = len(arr) - 1

        shape, shift = self._build_heap(arr, start, end)

        for i in range(end, start, -1):
            shape, shift = self._remove_last(arr, i, shape, shift)

        return arr


class PoplarSort(Sort):
    pass


class TournamentSort(Sort):
    pass