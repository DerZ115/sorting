from collections.abc import MutableSequence

from .base import Sort


def _merge(array_from: MutableSequence,
           array_to: MutableSequence,
           i_start: int, i_mid: int, i_end: int) -> None:

    i = i_start
    j = i_mid

    for ix in range(i_start, i_end):
        if i < i_mid and (j >= i_end or array_from[i] <= array_from[j]):
            array_to[ix] = array_from[i]
            i += 1
        else:
            array_to[ix] = array_from[j]
            j += 1


class TopDownMergeSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        aux_arr = arr[:]
        self._split(aux_arr, arr, 0, len(arr))
        return arr

    def _split(self,
               array_from: MutableSequence,
               array_to: MutableSequence,
               i_start: int, i_end: int) -> None:
        if i_end - i_start <= 1:
            return

        i_mid = (i_end + i_start) // 2
        self._split(array_to, array_from, i_start, i_mid)
        self._split(array_to, array_from, i_mid, i_end)

        _merge(array_from, array_to, i_start, i_mid, i_end)


class BottomUpMergeSort(Sort):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        aux_arr = arr[:]
        run_width = 1
        n = len(arr)

        while run_width < n:
            for i in range(0, n, 2 * run_width):
                _merge(arr, aux_arr, i, min(i+run_width, n), min(i+2*run_width, n))

            run_width *= 2
            if run_width >= n:
                return aux_arr

            for i in range(0, n, 2*run_width):
                _merge(aux_arr, arr, i, min(i+run_width, n), min(i+2*run_width, n))

            run_width *= 2

        return arr
