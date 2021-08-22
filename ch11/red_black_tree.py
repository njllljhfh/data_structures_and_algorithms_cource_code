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

from ch11.binary_search_tree import TreeMap


class RedBlackTreeMap(TreeMap):
    """Sorted map implementation using a red-black tree."""

    # -------------------------- nested _Node class --------------------------
    class _Node(TreeMap._Node):
        """Node class for red-black tree maintains bit that denotes color."""
        __slots__ = '_red'  # add additional data member to the Node class

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._red = True  # new node red by default

    # ------------------------- positional-based utility methods -------------------------
    # we consider a nonexistent child to be trivially black
    def _set_red(self, p):
        p._node._red = True

    def _set_black(self, p):
        p._node._red = False

    def _set_color(self, p, make_red):
        p._node._red = make_red

    def _is_red(self, p):
        return p is not None and p._node._red

    def _is_red_leaf(self, p):
        return self._is_red(p) and self.is_leaf(p)

    def _get_red_child(self, p):
        """Return a red child of p (or None if no such child)."""
        for child in (self.left(p), self.right(p)):
            if self._is_red(child):
                return child
        return None

    # ------------------------- support for insertions -------------------------
    def _rebalance_insert(self, p):
        self._resolve_red(p)  # new node is always red

    def _resolve_red(self, p):
        if self.is_root(p):
            # 红黑树的根节点是黑色的
            self._set_black(p)  # make root black
        else:
            parent = self.parent(p)  # parent 即是 y
            # 解决双红色问题
            if self._is_red(parent):  # double red problem
                uncle = self.sibling(parent)
                if not self._is_red(uncle):  # Case 1: misshapen 4-node
                    middle = self._restructure(p)  # do trinode restructuring
                    self._set_black(middle)  # and then fix colors
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                else:  # Case 2: overfull 5-node
                    grand = self.parent(parent)  # grand 即是 z
                    self._set_red(grand)  # grandparent becomes red
                    self._set_black(self.left(grand))  # its children become black
                    self._set_black(self.right(grand))
                    self._resolve_red(grand)  # recur at red grandparent

    # ------------------------- support for deletions -------------------------
    def _rebalance_delete(self, p):
        """p 是被删除节点的父节点"""
        if len(self) == 1:
            self._set_black(self.root())  # special case: ensure that root is black
        elif p is not None:
            n = self.num_children(p)
            # 需要结合书中P-307页 图11-6来理解
            if n == 1:  # deficit exists unless child is a red leaf
                c = next(self.children(p))  # c是y，p是z
                if not self._is_red_leaf(c):  # 如果c是红色的叶子节点，那么被删除的节点也是红色叶子节点
                    # 被删除的节点是节点p的黑色叶子节点
                    self._fix_deficit(p, c)
            elif n == 2:  # removed black node with red child
                # 书中P-338页，最上边描述的情况。另见P-340 图11-41 b) 右侧的描述。
                if self._is_red_leaf(self.left(p)):
                    self._set_black(self.left(p))
                else:
                    self._set_black(self.right(p))

    def _fix_deficit(self, z, y):
        """Resolve black deficit at z, where y is the root of z's heavier subtree."""
        if not self._is_red(y):  # y is black; will apply Case 1 or 2
            x = self._get_red_child(y)
            if x is not None:  # Case 1: y is black and has red child x; do "transfer". (对应（2，4）树)
                # 书中P-338页，情况1
                old_color = self._is_red(z)  # 重组前，z的颜色
                middle = self._restructure(x)
                self._set_color(middle, old_color)  # middle gets old color of z
                self._set_black(self.left(middle))  # children become black
                self._set_black(self.right(middle))
            else:  # Case 2: y is black, but no red children; recolor as "fusion". (对应（2，4）树)
                self._set_red(y)
                if self._is_red(z):
                    # 书中P-338页，情况2中的第一种情况（z节点原先是红色的）
                    self._set_black(z)  # this resolves the problem
                elif not self.is_root(z):  # 如果z是整个树的根节点，那就不需再向上传递了，因为在删除节点并进行了一系列的结构调整后，整个树的黑色深度减少了1
                    # 书中P-338页，情况2中的第二种情况（z节点原先是黑色的）
                    self._fix_deficit(self.parent(z), self.sibling(z))  # recur upward
        else:  # Case 3: y is red; rotate misaligned 3-node and repeat
            self._rotate(y)
            self._set_black(y)
            self._set_red(z)
            # 在执行一次 情况1 或者 情况2中的第一种情况(因为下面的代执行之前，z节点是红色的)
            if z == self.right(y):
                self._fix_deficit(z, self.left(z))
            else:
                self._fix_deficit(z, self.right(z))
