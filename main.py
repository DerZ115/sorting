from lib.sorting.exchange import (BinaryGnomeSort, BubbleSort, CircleSort,
                                  CocktailSort, CombSort, ExchangeSort,
                                  GnomeSort, OddEvenSort, OptBubbleSort,
                                  OptCocktailSort, OptGnomeSort)
from lib.sorting.selection import (SelectionSort)
from lib.sorting.insertion import (InsertionSort)
from lib.sorting.quick import (QuickSortLL, QuickSortLR)
from lib.sorting.merge import (TopDownMergeSort,
                               BottomUpMergeSort)
from lib.sorting.impractical import (BogoSort)

array = list(range(16))

sort_args = {'it': 10, 'repeats': 5, 'random_state': 141}

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

selection_sorts = [SelectionSort(**sort_args)]

insertion_sorts = [InsertionSort(**sort_args)]

quick_sorts = [QuickSortLL(**sort_args),
               QuickSortLR(**sort_args)]

merge_sorts = [TopDownMergeSort(**sort_args),
               BottomUpMergeSort(**sort_args)]

impractical_sorts = [BogoSort(**sort_args)]

all_sorts = {
    'Exchange Sorts': exchange_sorts,
    'Selection Sorts': selection_sorts,
    'Insertion Sorts': insertion_sorts,
    'Quick Sorts': quick_sorts,
    'Merge Sorts': merge_sorts,
    # 'Impractical Sorts': impractical_sorts
}

for name, category in all_sorts.items():
    print(name)
    for sorter in category:
        print(sorter.__class__.__name__)
        result = sorter.timed_sort(array)
        print(result)
