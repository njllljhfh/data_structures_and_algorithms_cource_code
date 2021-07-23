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

def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    for k in range(1, len(A)):  # from 1 to n-1
        cur = A[k]  # current element to be inserted
        j = k  # find correct index j for current
        while j > 0 and A[j - 1] > cur:  # element A[j-1] must be after current
            A[j] = A[j - 1]
            j -= 1
        A[j] = cur  # cur is now in the right place


def insertion_sort_njl(a, desc=False):
    """Sort list of comparable elements into nondecreasing order."""
    if desc:
        for k in range(1, len(a)):  # from 1 to n-1
            cur = a[k]  # current element to be inserted
            j = k  # find correct index j for current
            while j > 0 and a[j - 1] < cur:  # element A[j-1] must be after current
                a[j] = a[j - 1]
                j -= 1
            a[j] = cur  # cur is now in the right place
    else:
        for k in range(1, len(a)):  # from 1 to n-1
            cur = a[k]  # current element to be inserted
            j = k  # find correct index j for current
            while j > 0 and a[j - 1] > cur:  # element A[j-1] must be after current
                a[j] = a[j - 1]
                j -= 1
            a[j] = cur  # cur is now in the right place


# Has been read by dragon.(2021-07-12)
if __name__ == '__main__':
    a = [3, 1, 2, 5, 4, 10, 6, 8, 7, 9]
    # a = ["a", "c", "d", "b", "e"]
    insertion_sort_njl(a)
    print(a)
    insertion_sort_njl(a, desc=True)
    print(a)
