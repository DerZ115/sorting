from .base import Sort
from collections.abc import MutableSequence
from random import shuffle


class BogoSort(Sort):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def sort(self, arr: MutableSequence) -> MutableSequence:
        while True:
            if all(a <= b for a, b in zip(arr[:-1], arr[1:])):
                break
            else:
                shuffle(arr)

        self.last_results = arr
        return arr
