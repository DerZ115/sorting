import gc
import random
import itertools
from time import perf_counter_ns
from func_timeout import func_timeout, FunctionTimedOut
from collections.abc import Callable, Sequence, MutableSequence


class Sort:
    def __init__(self, it: int = 10,
                 repeats: int = 5,
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
        self._check_sorting(array)
        self.last_runtimes = []
        for runtimes_tmp in runtimes:
            if all([runtime is None for runtime in runtimes_tmp]):
                self.last_runtimes.append(None)
            else:
                self.last_runtimes.append(min([runtime for runtime in runtimes_tmp if runtime is not None]))

        return self.last_runtimes

    def timed_iter(self,
                   func: Callable,
                   array: MutableSequence,
                   *args, **kwargs) -> tuple[list, list]:
        runtimes_it = []
        results_it = []
        for _ in itertools.repeat(None, self.it):
            if hasattr(array, "copy"):
                arr = array.copy()
            else:
                arr = array
            try:
                result, runtime = func_timeout(self.max_time,
                                               self.measure_sort_time,
                                               args=(func, arr, *args),
                                               kwargs=kwargs)
            except FunctionTimedOut:
                print(f"Sorter {self.__class__.__name__} timed out")
                result = None
                runtime = None
            runtimes_it.append(runtime)
            results_it.append(result)

        return runtimes_it, results_it

    def _check_sorting(self, array) -> None:
        sorted_array = list(range(len(array)))
        is_sorted = all([result == sorted_array or result is None for result in self.last_results])
        if not is_sorted:
            print(set(tuple(x) for x in self.last_results))
            raise ValueError("Sorting failed in at least one iteration")

    @staticmethod
    def measure_sort_time(func: Callable, array: MutableSequence, *args, **kwargs) -> tuple[Sequence, int]:
        start = perf_counter_ns()
        result = func(array, *args, **kwargs)
        end = perf_counter_ns()
        return result, end - start
