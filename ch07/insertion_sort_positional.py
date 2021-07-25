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
from ch07.positional_list import PositionalList


def insertion_sort(L):
    """Sort PositionalList of comparable elements into nondecreasing order."""
    if len(L) > 1:  # otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)  # next item to be placed
            value = pivot.element()
            if value > marker.element():  # pivot is already sorted
                marker = pivot  # pivot becomes new marker
            else:  # must relocate pivot
                walk = marker  # find leftmost item greater than value
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)  # reinsert value before walk


if __name__ == '__main__':
    pl = PositionalList()
    elements = [15, 22, 25, 29, 36, 23, 53, 11, 42]
    for e in elements:
        pl.add_last(e)
    print(f"排序前：{pl}")

    insertion_sort(pl)
    print(f"排序后：{pl}")
