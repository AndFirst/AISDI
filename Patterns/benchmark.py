import KMP_algorithm as KMP
import KR_algorithm as KR
import N_algorithm as N
from timeit import timeit
import matplotlib.pyplot as plt

def read_from_file(path: str)->str:
    with open(path, encoding="utf-8") as file:
        words = file.read()
    return words


def search_N(patterns, text, quantity):
    for pattern in patterns[:quantity]:
        N.find(pattern, text)

def search_KR(patterns, text, quantity):
    for pattern in patterns[:quantity]:
        KR.find(pattern, text)

def search_KMP(patterns, text, quantity):
    for pattern in patterns[:quantity]:
        KMP.find(pattern, text)

def benchmark_N(patterns, text):
    results = []
    quantity = 0
    for i in range(11):
        searching_time = timeit(lambda: search_N(patterns, text, quantity), number=1)
        results.append(searching_time)
        quantity += 50
    return results

def benchmark_KR(patterns, text):
    results = []
    quantity = 0
    for i in range(11):
        searching_time = timeit(lambda: search_KR(patterns, text, quantity), number=1)
        results.append(searching_time)
        quantity += 50
    return results

def benchmark_KMP(patterns, text):
    results = []
    quantity = 0
    for i in range(11):
        searching_time = timeit(lambda: search_KMP(patterns, text, quantity), number=1)
        results.append(searching_time)
        quantity += 50
    return results

def plotter(patterns, text):
    times = [i * 50 for i in range(11)]
    plt.cla()
    search_N = benchmark_N(patterns, text)
    search_KR = benchmark_KR(patterns, text)
    search_KMP = benchmark_KMP(patterns, text)

    plt.plot(times, search_N)
    plt.plot(times, search_KR)
    plt.plot(times, search_KMP)
    plt.xlabel("quantity of words")
    plt.ylabel("time of searching")
    plt.title("Time of searching")
    plt.legend(["N_algorithm", "KR_algorithm", "KMP_algorithm"], loc="upper right")
    plt.show()
    plt.savefig("plots.png")
    return plt



if __name__ == "__main__":
    text = read_from_file("pan-tadeusz.txt")
    patterns = text.split()
    plotter(patterns, text)