import matplotlib.pyplot as plt
from benchmark import (
                        benchmark_creating_AVL,
                        benchmark_creating_BST,
                        benchmark_searching_AVL,
                        benchmark_searching_BST,
                        removing_AVL_benchmark,
                        removing_BST_benchmark,
                        numbers,
                        sorted_numbers,
                        s_benchmark_creating_AVL,
                        s_benchmark_creating_BST,
                        s_benchmark_searching_AVL,
                        s_benchmark_searching_BST,
                        s_creating_AVL,
                        s_creating_BST,
                        s_removing_AVL_benchmark,
                        s_removing_BST_benchmark,
                        s_searching_AVL,
                        s_searching_BST
                        )

times = [i*1000 for i in range(11)]


def plot_create():
    plt.cla()
    result_BST = benchmark_creating_BST(numbers)
    result_AVL = benchmark_creating_AVL(numbers)
    plt.plot(times, result_BST)
    plt.plot(times, result_AVL)
    plt.xlabel("quantity of numbers")
    plt.ylabel("time of creation")
    plt.title("Time of creation")
    plt.legend(["BST", "AVL"], loc = "upper right")
    plt.show()
    return plt

def plot_search():
    plt.cla()
    result_BST = benchmark_searching_BST()
    result_AVL = benchmark_searching_AVL()
    plt.plot(times, result_BST)
    plt.plot(times, result_AVL)
    plt.xlabel("quantity of numbers searched")
    plt.ylabel("time of searching")
    plt.title("Time of searching")
    plt.legend(["BST", "AVL"], loc = "upper right")
    plt.show()
    return plt

def plot_remove():
    plt.cla()
    result_BST = removing_BST_benchmark()
    result_AVL = removing_AVL_benchmark()
    plt.plot(times, result_BST)
    plt.plot(times, result_AVL)
    plt.xlabel("quantity of numbers removed")
    plt.ylabel("time of removing")
    plt.title("Time of removing")
    plt.legend(["BST", "AVL"], loc = "upper right")
    plt.show()
    return plt

def s_plot_create():
    plt.cla()
    result_BST = s_benchmark_creating_BST(sorted_numbers)
    result_AVL = s_benchmark_creating_AVL(sorted_numbers)
    plt.plot(times, result_BST)
    plt.plot(times, result_AVL)
    plt.xlabel("quantity of numbers")
    plt.ylabel("time of creation")
    plt.title("Time of creation")
    plt.legend(["BST", "AVL"], loc = "upper right")
    plt.show()
    return plt

def s_plot_search():
    plt.cla()
    result_BST = s_benchmark_searching_BST()
    result_AVL = s_benchmark_searching_AVL()
    plt.plot(times, result_BST)
    plt.plot(times, result_AVL)
    plt.xlabel("quantity of numbers searched")
    plt.ylabel("time of searching")
    plt.title("Time of searching")
    plt.legend(["BST", "AVL"], loc = "upper right")
    plt.show()
    return plt

def s_plot_remove():
    plt.cla()
    result_BST = s_removing_BST_benchmark()
    result_AVL = s_removing_AVL_benchmark()
    plt.plot(times, result_BST)
    plt.plot(times, result_AVL)
    plt.xlabel("quantity of numbers removed")
    plt.ylabel("time of removing")
    plt.title("Time of removing")
    plt.legend(["BST", "AVL"], loc = "upper right")
    plt.show()
    return plt

if __name__ == "__main__":
    plot_create().savefig('creating.png')
    plot_search().savefig('searching.png')
    plot_remove().savefig('removing.png')
    s_plot_create().savefig('sorted_creating.png')
    s_plot_search().savefig('sorted_searching.png')
    s_plot_remove().savefig('sorted_removing.png')
