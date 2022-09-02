# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from exceptions import Empty


class ArrayDeque:
    """Deque implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty deque."""
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size

    def is_empty(self):
        """Return True if the deque is empty."""
        return self._size == 0

    def first(self):
        """
        Return (but do not remove) the element at the front of the deque.
        Raise Empty exception if the deque is empty.
        """
        return self._data[self.front]

    def last(self):
        """
        Return (but do not remove) the element at the end of the deque.
        Raise Empty exception if the deque is empty.
        """
        return self._data[self.end]

    def delete_first(self):
        """
        Remove and return the first element of the deque.
        Raise Empty exception if the deque is empty.
        """
        answer = self._data[self.front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # 当队列所存储的元素降低到数组总存储能力的1/4时，将数组的容量减少一半。
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def delete_last(self):
        """
        Remove and return the last element of the deque.
        Raise Empty exception if the deque is empty.
        """
        answer = self._data[self.end]
        self._data[self.end] = None  # help garbage collection
        self._size -= 1
        # 当队列所存储的元素降低到数组总存储能力的1/4时，将数组的容量减少一半。
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def add_last(self, e):
        """Add an element to the back of deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def add_first(self, e):
        """Add an element to the front of deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        self._front = (self._front - 1 + len(self._data)) % len(self._data)
        self._data[self._front] = e
        self._size += 1

    def _resize(self, cap):  # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        old = self._data  # keep track of existing list
        self._data = [None] * cap  # allocate list with new capacity
        walk = self._front
        for k in range(self._size):  # only consider existing elements
            self._data[k] = old[walk]  # intentionally shift indices
            walk = (1 + walk) % len(old)  # use old size as modulus
        self._front = 0  # front has been realigned

    @property
    def front(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._front

    @property
    def end(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return (self._front + self._size - 1) % len(self._data)

    def show_data(self):
        print(f"{self._data}")


def show_deque_info(deque: ArrayDeque):
    try:
        print(f"len(deque) = {len(deque)}")
        print(f'front_index = {deque.front}')
        print(f'end_index = {deque.end}')
        print(f'deque.first() = {deque.first()}')
        print(f'deque.last() = {deque.last()}')
    except Empty as e:
        print(f'[ERROR]: {e}')


def example():
    """测试例题6-4的操作（P-156）。"""
    q = ArrayDeque()
    q.show_data()
    print('- ' * 20)

    q.add_last(55)
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.add_last(44)
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.add_first(1)
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.add_first(2)
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.add_first(3)
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.add_first(4)
    q.add_first(5)
    q.add_first(6)
    q.add_first(7)
    q.add_first(8)
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.add_first(9)
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.add_last(10)
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.delete_first()
    q.delete_first()
    q.delete_first()
    q.delete_first()
    q.delete_first()
    q.delete_first()
    q.delete_first()
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.delete_first()
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.delete_last()
    q.delete_last()
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.delete_last()
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.delete_last()
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)


def _shrink_underlying_array():
    # 测试缩减底层数组
    q = ArrayDeque()
    q.show_data()
    print('- ' * 20)

    q.add_last(1)
    q.add_last(2)
    q.add_first(3)
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.delete_first()
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)

    q.delete_last()
    q.show_data()
    show_deque_info(q)
    print('- ' * 20)


if __name__ == '__main__':
    example()

    # 测试缩减底层数组
    # _shrink_underlying_array()
