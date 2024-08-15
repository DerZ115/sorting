import pandas as pd
import numpy as np
from pathlib import Path

from lib.sorting.exchange import (BinaryGnomeSort, BubbleSort, CircleSort,
                                  CocktailSort, CombSort, ExchangeSort,
                                  GnomeSort, OddEvenSort, OptBubbleSort,
                                  OptCocktailSort, OptGnomeSort)
from lib.sorting.selection import (SelectionSort, DoubleSelectionSort,
                                   CycleSort, HeapSortMax, HeapSortMin,
                                   HeapSortMinFlipped, WeakHeapSort, TernaryHeapSort)
from lib.sorting.insertion import (InsertionSort)
from lib.sorting.quick import (QuickSortLL, QuickSortLR, QuickSortDualPivot,
                               QuickSortStable)
from lib.sorting.merge import (TopDownMergeSort,
                               BottomUpMergeSort)
from lib.sorting.impractical import (BogoSort)

sort_args = {'it': 10, 'repeats': 5, 'random_state': 141, "max_time": 1}

exchange_sorts = [BubbleSort(**sort_args),
                  OptBubbleSort(**sort_args),
                  CocktailSort(**sort_args),
                  OptCocktailSort(**sort_args),
                  OddEvenSort(**sort_args),
                  GnomeSort(**sort_args),
                  OptGnomeSort(**sort_args),
                  BinaryGnomeSort(**sort_args),
                  ExchangeSort(**sort_args),
                  CombSort(**sort_args),
                  CircleSort(**sort_args)]

selection_sorts = [SelectionSort(**sort_args),
                   DoubleSelectionSort(**sort_args),
                   CycleSort(**sort_args),
                   HeapSortMax(**sort_args),
                   HeapSortMin(**sort_args),
                   HeapSortMinFlipped(**sort_args),
                   WeakHeapSort(**sort_args),
                   TernaryHeapSort(**sort_args)]

insertion_sorts = [InsertionSort(**sort_args)]

quick_sorts = [QuickSortLL(**sort_args),
               QuickSortLR(**sort_args),
               QuickSortDualPivot(**sort_args),
               QuickSortStable(**sort_args)]

merge_sorts = [TopDownMergeSort(**sort_args),
               BottomUpMergeSort(**sort_args)]

impractical_sorts = [BogoSort(**sort_args)]

all_sorts = {
    # 'Exchange Sorts': exchange_sorts,
    'Selection Sorts': selection_sorts,
    # 'Insertion Sorts': insertion_sorts,
    # 'Quick Sorts': quick_sorts,
    # 'Merge Sorts': merge_sorts,
    # 'Impractical Sorts': impractical_sorts
}

array_lens = [2**x for x in range(11)]  # 1 - 1024

result_path = Path("./results")
result_path.mkdir(exist_ok=True)

for name, category in all_sorts.items():
    print(name)
    ctg_path = result_path / name
    ctg_path.mkdir(exist_ok=True)

    for sorter in category:
        print(sorter.__class__.__name__)

        results = np.zeros((len(array_lens), sort_args["repeats"]))
        timed_out = False

        for i, n in enumerate(array_lens):
            arr = list(range(n))
            if timed_out:
                results[i, :] = None
                continue

            result = sorter.timed_sort(arr)
            if all([r is None for r in result]):
                timed_out = True

            results[i, :] = result

        print(results)
        pd.DataFrame(results, index=array_lens).to_csv(
            ctg_path / f"{sorter.__class__.__name__}.csv",
            header=False
        )
