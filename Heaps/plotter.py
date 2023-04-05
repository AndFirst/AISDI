import matplotlib.pyplot as plt
from benchmark import (
                        benchmark_creating_2ary_heap,
                        benchmark_creating_3ary_heap,
                        benchmark_creating_4ary_heap,
                        numbers,
                        benchmark_removing_root_2ary_heap,
                        benchmark_removing_root_3ary_heap,
                        benchmark_removing_root_4ary_heap
                        )

times = [i*1000 for i in range(11)]


def plot_create_heap():
    plt.cla()
    creating_2ary = benchmark_creating_2ary_heap(numbers)
    creating_3ary = benchmark_creating_3ary_heap(numbers)
    creating_4ary = benchmark_creating_4ary_heap(numbers)

    plt.plot(times, creating_2ary)
    plt.plot(times, creating_3ary)
    plt.plot(times, creating_4ary)
    plt.xlabel("quantity of numbers")
    plt.ylabel("time of creation")
    plt.title("Time of creation")
    plt.legend(["2-ary heap", "3-ary heap", "4-ary heap"], loc = "upper right")
    plt.show()
    return plt

def plot_remove_roots():
    plt.cla()
    removing_2ary = benchmark_removing_root_2ary_heap()
    removing_3ary = benchmark_removing_root_3ary_heap()
    removing_4ary = benchmark_removing_root_4ary_heap()

    plt.plot(times, removing_2ary)
    plt.plot(times, removing_3ary)
    plt.plot(times, removing_4ary)
    plt.xlabel("quantity of roots removed")
    plt.ylabel("time of removing")
    plt.title("Time of removing roots")
    plt.legend(["2-ary heap", "3-ary heap", "4-ary heap"], loc = "upper right")
    plt.show()
    return plt


if __name__ == "__main__":
    plot_create_heap().savefig('creating.png')
    plot_remove_roots().savefig('removing.png')
    