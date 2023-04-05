import typing
from abc import ABC, abstractmethod
from typing import List

from typing_extensions import Protocol

C = typing.TypeVar("C", bound="Comparable")


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: C, other: C) -> bool:
        pass

    @abstractmethod
    def __gt__(self: C, other: C) -> bool:
        pass


class AbstractHeap(ABC):
    def __init__(self, num_children: int) -> None:
        pass

    def __len__(self) -> int:
        return len(self.get_raw_data())

    @abstractmethod
    def peek(self) -> C:
        """Get the topmost element without changing the heap."""

    @abstractmethod
    def push(self, value: C):
        """Add an element to the heap."""

    @abstractmethod
    def pop(self) -> C:
        """Remove the topmost element from the heap and return it."""

    @abstractmethod
    def get_raw_data(self) -> List[C]:
        """Get the underlying data storage."""

class Heap(AbstractHeap):
    def __init__(self, k:int):
        if k < 2:
            raise ValueError("Heap must be at least binary.")
        self._k = k
        self._values = []

    def peek(self):
        return self._values[0]

    def get_raw_data(self):
        return self._values

    def push(self, number):
        index = len(self._values)
        self._values.append(number)
        parent = (index - 1) // self._k
        while index > 0 and self._values[parent] < number:
            self._values[index] = self._values[parent]
            index = parent
            parent = (index - 1) // self._k
        self._values[index] = number

    def fall(self, index, value):
        min_child_index = index * self._k + 1
        max_child_index = min((index + 1) * self._k + 1, len(self._values))
        children = self._values[min_child_index : max_child_index]
        if not children or max(children) < value:
            self._values[index] = value
            return
        max_child = index * self._k + children.index(max(children)) + 1
        self._values[index] = self._values[max_child]
        return self.fall(max_child, value)

    def pop(self):
        value = self._values[0]
        if self.__len__() == 1:
            self._values = []
        else:
            self._values[0] = self._values[-1]
            self.fall(0, self._values.pop())
        return value

    def check(self):
        for index, val in enumerate(self._values):
            if self._values[(index - 1) // self._k] < self._values[index]:
                if index != 0:
                    return False
        return True

    def __str__(self):
        result = ""
        level = 0
        els = 0
        while els < len(self._values):
            row = self._k ** level
            els += row
            st = "   #" + str(level) + ": ";
            for i in range(els - row, els):
                if i < len(self._values):
                    st += str(self._values[i]) + ", "
                else:
                    st += "_, "
            st = st[:-2]
            result += (st + '\n')
            level += 1
        return result


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    heap = Heap(3)
    for elem in list:
        heap.push(elem)
    list = []
    while heap.get_raw_data():
        print(heap.__str__())
        list.append(heap.pop())
    print(list)
