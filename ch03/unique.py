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


"""
元素唯一性问题：给出一个有n个元素的序列S，求该集合内的所有元素是否彼此不同。
"""


def unique1(S):
    """
    Return True if there are no duplicate elements in sequence S.
    时间复杂度: O(n^2)
    """
    for j in range(len(S)):
        for k in range(j + 1, len(S)):
            if S[j] == S[k]:
                return False  # found duplicate pair
    return True  # if we reach this, elements were unique


def unique2(S):
    """
    Return True if there are no duplicate elements in sequence S.
    时间复杂度：O(nlog(n))
    """
    # Dragon: sorted(S) 的是最坏时间复杂度是 O(nlog(n))
    temp = sorted(S)  # create a sorted copy of S
    for j in range(1, len(temp)):  # O(n)
        if S[j - 1] == S[j]:
            return False  # found duplicate pair
    return True  # if we reach this, elements were unique
