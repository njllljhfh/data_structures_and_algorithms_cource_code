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

from ch10.map_base import MapBase


# 10.3.1 排序检索表(p-282)
class SortedTableMap(MapBase):
    """Map implementation using a sorted table."""

    # ----------------------------- nonpublic behaviors -----------------------------
    def _find_index(self, k, low, high):
        """Return index of the leftmost item with key greater than or equal to k.

        Return high + 1 if no such item qualifies.

        That is, j will be returned such that:
           all items of slice table[low:j] have key < k
           all items of slice table[j:high+1] have key >= k
        """
        # 此处用的算法是"二分查找"，并通过递归来实现。
        # 时间复杂度: O(log n)
        if high < low:
            return high + 1  # no element qualifies
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid  # found exact match
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)  # Note: may return mid
            else:
                return self._find_index(k, mid + 1, high)  # answer is right of mid

    # ----------------------------- public behaviors -----------------------------
    def __init__(self):
        """Create an empty map."""
        self._table = []

    def __len__(self):
        """Return number of items in the map.
        """
        # 时间复杂度: O(1)
        return len(self._table)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        # 时间复杂度: O(1)
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        # 最坏时间复杂度: O(n)
        # 最优时间复杂度: O(log n), 在此情况下 k 存在。
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v  # reassign value
        else:
            self._table.insert(j, self._Item(k, v))  # adds new item

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        # 最坏时间复杂度: O(n)
        # 最优时间复杂度: O(log n), 在此情况下 k 存在。
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j)  # delete item

    def __iter__(self):
        """Generate keys of the map ordered from minimum to maximum."""
        # 时间复杂度: O(n)
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """Generate keys of the map ordered from maximum to minimum."""
        # 时间复杂度: O(n)
        for item in reversed(self._table):
            yield item._key

        # dragon:逆序遍历
        # for i in range(len(self._table)-1, -1, -1):
        #     yield self._table[i]._key

    def find_min(self):
        """Return (key,value) pair with minimum key (or None if empty)."""
        # 时间复杂度: O(1)
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        """Return (key,value) pair with maximum key (or None if empty)."""
        # 时间复杂度: O(1)
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_le(self, k):
        """Return (key,value) pair with greatest key less than or equal to k.

        Return None if there does not exist such a key.
        """
        # 时间复杂度: O(log n)
        j = self._find_index(k, 0, len(self._table) - 1)  # j's key >= k
        if j < len(self._table) and self._table[j]._key == k:
            return (self._table[j]._key, self._table[j]._value)  # exact match
        elif j > 0:
            return (self._table[j - 1]._key, self._table[j - 1]._value)  # Note use of j-1
        else:
            return None

    def find_ge(self, k):
        """Return (key,value) pair with least key greater than or equal to k.

        Return None if there does not exist such a key.
        """
        # 时间复杂度: O(log n)
        j = self._find_index(k, 0, len(self._table) - 1)  # j's key >= k
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_lt(self, k):
        """Return (key,value) pair with greatest key strictly less than k.

        Return None if there does not exist such a key.
        """
        # 时间复杂度: O(log n)
        j = self._find_index(k, 0, len(self._table) - 1)  # j's key >= k
        if j > 0:
            return (self._table[j - 1]._key, self._table[j - 1]._value)  # Note use of j-1
        else:
            return None

    def find_gt(self, k):
        """Return (key,value) pair with least key strictly greater than k.

        Return None if there does not exist such a key.
        """
        # 时间复杂度: O(log n)
        j = self._find_index(k, 0, len(self._table) - 1)  # j's key >= k
        if j < len(self._table) and self._table[j]._key == k:
            j += 1  # advanced past match
        if j < len(self._table):  # 上一步的if中，j+=1后，j可能大于 self._table 表的最大索引.
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_range(self, start, stop):
        """Iterate all (key,value) pairs such that start <= key < stop.

        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maximum key of map.
        """
        # 时间复杂度: O(s + log n), s是区间范围内元素的个数。
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)  # find first result
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1


if __name__ == '__main__':
    a = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
    print(f"len(a) = {len(a)}")
    print("- " * 30)

    my_map = SortedTableMap()
    for i in a:
        my_map[i] = i

    print(f"19 in my_map: {19 in my_map}")
    print(f"21 in my_map: {21 in my_map}")
    print("- " * 30)

    # print(my_map[38])
    # print("- " * 30)

    # my_map[100] = 100
    # print("- " * 30)

    print(f"正序遍历key:")
    i = 0
    for k in my_map:
        if i < len(my_map) - 1:
            print(k, end=' ')
        else:
            print(k)
        i += 1
    print("- " * 30)

    print(f"逆序遍历key:")
    i = 0
    for k in reversed(my_map):
        if i < len(my_map) - 1:
            print(k, end=' ')
        else:
            print(k)
        i += 1
    print("- " * 30)
