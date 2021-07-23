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


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10  # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None  # help garbage collection
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        # 当队列所存储的元素降低到数组总存储能力的1/4时，将数组的容量减少一半。
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
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

    def front(self):
        if self.is_empty():
            raise Empty("队列中没有数据。")
        return self._front

    def show_data(self):
        print(f"{self._data}")


def _example_6_4():
    """测试例题6-4的操作（P-156）。"""
    q = ArrayQueue()
    q.enqueue(5)
    q.show_data()

    q.enqueue(3)
    q.show_data()

    print(f"len(q)={len(q)}")

    q.dequeue()
    q.show_data()

    print(f"q.is_empty()={q.is_empty()}")

    q.dequeue()
    q.show_data()

    print(f"q.is_empty()={q.is_empty()}")

    try:
        q.dequeue()
    except Exception as e:
        print(f"error: {e}")

    q.enqueue(7)
    q.show_data()

    q.enqueue(9)
    q.show_data()

    print(f"q.first()={q.first()}")

    q.enqueue(4)
    q.show_data()

    print(f"len(q)={len(q)}")

    q.dequeue()
    q.show_data()


def _shrink_underlying_array():
    # 测试缩减底层数组
    q = ArrayQueue()
    q.show_data()

    q.enqueue(1)
    q.enqueue(2)
    q.show_data()

    q.dequeue()
    q.show_data()


if __name__ == '__main__':
    # 测试例题6-4的操作（P-156）。
    # _example_6_4()

    # 测试缩减底层数组
    _shrink_underlying_array()
