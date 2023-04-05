import random
import KMP_algorithm as KMP
import KR_algorithm as KR
import N_algorithm as N

def empty_test():
    print("===EMPTY===")

    print("BOTH EMPTY:")
    pattern = ""
    text = ""

    assert (N.find(pattern, text) == [])
    assert (KR.find(pattern, text) == [])
    assert (KMP.find(pattern, text) == [])

    print(f"Naive: {N.find(pattern, text)}, KR: {KR.find(pattern, text)}, KMP: {KMP.find(pattern, text)}")

    print("PATTERN_EMPTY:")
    pattern = ""
    text = "ABBAB"

    assert (N.find(pattern, text) == [])
    assert (KR.find(pattern, text) == [])
    assert (KMP.find(pattern, text) == [])

    print(f"Naive: {N.find(pattern, text)}, KR: {KR.find(pattern, text)}, KMP: {KMP.find(pattern, text)}")

    print("TEXT_EMPTY:")
    pattern = "ABA"
    text = ""

    assert (N.find(pattern, text) == [])
    assert (KR.find(pattern, text) == [])
    assert (KMP.find(pattern, text) == [])

    print(f"Naive: {N.find(pattern, text)}, KR: {KR.find(pattern, text)}, KMP: {KMP.find(pattern, text)}")
    print()

def equal_test():
    print("===EQUAL===")
    pattern = "ABABB"
    text = "ABABB"

    assert (N.find(pattern, text) == [0])
    assert (KR.find(pattern, text) == [0])
    assert (KMP.find(pattern, text) == [0])

    print(f"Naive: {N.find(pattern, text)}, KR: {KR.find(pattern, text)}, KMP: {KMP.find(pattern, text)}")
    print()

def longer_test():
    print("===PATTERN LONGER===")
    pattern = "ABABBB"
    text = "ABABB"

    assert (N.find(pattern, text) == [])
    assert (KR.find(pattern, text) == [])
    assert (KMP.find(pattern, text) == [])

    print(f"Naive: {N.find(pattern, text)}, KR: {KR.find(pattern, text)}, KMP: {KMP.find(pattern, text)}")

    print()

def not_containing_test():
    print("===NOT CONTAINS===")
    pattern = "AAA"
    text = "ABABAB"

    assert (N.find(pattern, text) == [])
    assert (KR.find(pattern, text) == [])
    assert (KMP.find(pattern, text) == [])

    print(f"Naive: {N.find(pattern, text)}, KR: {KR.find(pattern, text)}, KMP: {KMP.find(pattern, text)}")
    print()

def naive_test():
    print("===NAIVE===")

    pattern = "ABA"
    text = "AABABAAAB"
    assert (N.find(pattern, text) == [1, 3])
    print(f"Naive: {N.find(pattern, text)}")

    pattern = "AA"
    text = "AABABAAAB"
    assert (N.find(pattern, text) == [0, 5, 6])
    print(f"Naive: {N.find(pattern, text)}")
    print()

def random_test():
    print("===RANDOM===")
    alphabet = ["A", "B"]
    pattern_len = random.randint(2, 6)
    text_len = random.randint(7, 150)
    for i in range(5):
        pattern = generate_string(alphabet, pattern_len)
        text = generate_string(alphabet, text_len)
        assert(N.find(pattern, text) == KR.find(pattern, text)) # ==KMP.find(pattern, text)
        print(f"Naive: {N.find(pattern, text)}, KR: {KR.find(pattern, text)}, KMP: {KMP.find(pattern, text)}")
    print()


def generate_string(alphabet, length):
    string = ""
    for i in range(length):
        string += random.choice(alphabet)
    return string


if __name__ == "__main__":
    empty_test()
    equal_test()
    longer_test()
    not_containing_test()
    naive_test()
    random_test()