import gc
import random
import itertools
from time import process_time_ns
from collections.abc import Callable, Sequence, MutableSequence


class Sort(object):
    def __init__(self, it: int = 1000,
                 repeats: int = 1,
                 max_time: int | None = None,
                 random_state=None) -> None:
        self.it = it
        self.repeats = repeats
        self.max_time = max_time
        self.random_state = random_state
        self.last_results = None
        self.last_runtimes = None

    def sort(self, arr: MutableSequence) -> MutableSequence:
        return arr

    def timed_sort(self,
                   array: Sequence,
                   *args, **kwargs) -> list:
        gc.disable()
        results = []
        runtimes = []

        random.seed(self.random_state)
        for i in range(self.repeats):
            shuffled_array = random.sample(array, k=len(array))
            runtimes_tmp, results_tmp = self.timed_iter(func=self.sort,
                                                        array=shuffled_array,
                                                        *args,
                                                        **kwargs)
            runtimes.append(runtimes_tmp)
            results.extend(results_tmp)

        gc.enable()
        self.last_results = results
        self._check_sorting()
        self.last_runtimes = [min(runtimes_tmp) for runtimes_tmp in runtimes]

        return self.last_runtimes

    def timed_iter(self,
                   func: Callable,
                   array: MutableSequence,
                   *args, **kwargs) -> tuple[list, list]:
        total_time = 0
        runtimes_it = []
        results_it = []
        for _ in itertools.repeat(None, self.it):
            if hasattr(array, "copy"):
                arr = array.copy()
            else:
                arr = array
            start = process_time_ns()
            result = func(arr, *args, **kwargs)
            runtime = process_time_ns() - start
            runtimes_it.append(runtime)
            results_it.append(result)
            total_time += runtime

            if self.max_time is not None and total_time >= self.max_time:
                break

        return runtimes_it, results_it

    def _check_sorting(self) -> None:
        """Returns True if all the elements are equal to each other"""
        sorted_array = list(range(len(self.last_results[0])))
        is_sorted = all([result == sorted_array for result in self.last_results])
        if not is_sorted:
            print(set(tuple(x) for x in self.last_results))
            raise ValueError("Sorting failed in at least one iteration")
