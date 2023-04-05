from Sorting.Sources.bubble_sort import bubble_sort
from Sorting.Sources.merge_sort import merge_sort
from Sorting.Sources.quick_sort import quick_sort
from Sorting.Sources.selection_sort import selection_sort


import matplotlib.pyplot as plt
from aisdi.Trees.Sources.benchmark import (
                        read_from_file,
                        benchmark
                        )

words = read_from_file('pan-tadeusz.txt')
times = [i*1000 for i in range(11)]


def plot_functions(words, *args):
    plt.cla()
    for function in args:
        result = benchmark(function, words)
        plt.plot(times, result)
    plt.legend([function.__name__ for function in args])
    return plt

if __name__ == "__main__":
    plot_functions(words, quick_sort).savefig('Plots/quick_sort.png')
    plot_functions(words, merge_sort).savefig('Plots/merge_sort.png')
    plot_functions(words, bubble_sort).savefig('Plots/bubble_sort.png')
    plot_functions(words, selection_sort).savefig('Plots/selection_sort.png')
    plot_functions(words, quick_sort, merge_sort, bubble_sort, selection_sort).savefig('Plots/all_functions.png')

