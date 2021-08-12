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

from ch10.sorted_table_map import SortedTableMap


class CostPerformanceDatabase:
    """Maintain a database of maximal (cost,performance) pairs."""

    def __init__(self):
        """Create an empty database."""
        # 最大值集
        self._M = SortedTableMap()  # or a more efficient sorted map

    def best(self, c):
        """Return (cost,performance) pair with largest cost not exceeding c.

        Return None if there is no such pair.
        """
        return self._M.find_le(c)

    def add(self, c, p):
        """Add new entry with cost c and performance p."""
        # 时间复杂度: O(n)

        # determine if (c,p) is dominated by an existing pair
        # 查找价格小于等于c的（价格, 性能）对
        other = self._M.find_le(c)  # other is at least as cheap as c
        if other is not None and other[1] >= p:  # if its performance is as good,
            return  # (c,p) is dominated, so ignore
        self._M[c] = p  # else, add (c,p) to database
        # and now remove any pairs that are dominated by (c,p)
        other = self._M.find_gt(c)  # other more expensive than c
        while other is not None and other[1] <= p:
            del self._M[other[0]]  # other[0] 是映射中的键（在此应用中，即价格；见书中10.3.2节，p-286）
            other = self._M.find_gt(c)


if __name__ == '__main__':
    print((99, 110) <= (99, 100))
