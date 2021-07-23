# -*- coding:utf-8 -*-

from ch08.tree import Tree


class LinkedGeneralTree(Tree):
    """Linked representation of a general tree."""

    # -------------------------- nested _Node class --------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a node."""
        __slots__ = '_element', '_parent', '_children'  # streamline memory usage

        def __init__(self, element, parent=None, children=None):
            self._element = element
            self._parent = parent  # <type: _Node>
            # self._left = left
            # self._right = right
            self._children = children  # [_Node, _Node, ...]

    # -------------------------- nested Position class --------------------------
    class Position(Tree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

    # ------------------------------- utility methods -------------------------------
    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    # -------------------------- general tree constructor --------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None  # <type: _Node>
        self._size = 0

    # -------------------------- public accessors --------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    # def left(self, p):
    #     """Return the Position of p's left child (or None if no left child)."""
    #     node = self._validate(p)
    #     return self._make_position(node._left)
    #
    # def right(self, p):
    #     """Return the Position of p's right child (or None if no right child)."""
    #     node = self._validate(p)
    #     return self._make_position(node._right)

    def children(self, p):
        """Generate an list of Positions representing p's children."""
        node = self._validate(p)
        if node._children:
            for child_node in node._children:
                yield self._make_position(child_node)
        # return node._children  # might be None.

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        if node._children is None:
            count = 0
        else:
            count = len(node._children)
        return count

    # -------------------------- nonpublic mutators --------------------------
    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_children(self, p, e):
        """Create a new child for Position p, storing element e.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid.
        """
        node = self._validate(p)
        self._size += 1
        child_node = self._Node(e, node)
        if node._children is None:
            node._children = [child_node]
        else:
            node._children.append(child_node)
        return self._make_position(child_node)

    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) > 1:
            raise ValueError('Position has more then one children.')

        child = node._children[0]
        if node is self._root:
            self._root = child
            child._parent = None
        else:
            parent = node._parent
            child._parent = parent
            # parent._children.remove(node)
            # parent._children.append(child)

            index = parent._children.index(node)
            parent._children.pop(index)
            parent._children.insert(index, child)
        self._size -= 1
        node._parent = node  # convention for deprecated node
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2, respectively, as the left and right subtrees of the external Position p.

        As a side effect, set t1 and t2 to empty.
        Raise TypeError if trees t1 and t2 do not match type of this tree.
        Raise ValueError if Position p is invalid or not external.
        """
        pass


if __name__ == '__main__':
    linked_t = LinkedGeneralTree()
    p_root = linked_t._add_root("root")
    print(f"p_root.element() = {p_root.element()}")
    print(linked_t.root().element())
    print(f"linked_t.children(p_root) = {linked_t.children(p_root)}")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    p_1_child_a = linked_t._add_children(p_root, "1_child_a")
    print(f"p_1_child_a.element() = {p_1_child_a.element()}")
    print(f"[p_child.element() for p_child in linked_t.children(p_root)] = "
          f"{[p_child.element() for p_child in linked_t.children(p_root)]}")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")


    for p_child in linked_t.children(p_root):
        print(f"{p_child.element()} -- {linked_t.children(p_child)}")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    print(linked_t.depth(p_root))
    print(linked_t.height(p_root))
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    for p_child in linked_t.children(p_root):
        print(f"depth={linked_t.depth(p_child)}, height={linked_t.height(p_child)}")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    p_1_child_b = linked_t._add_children(p_root, "1_child_b")
    p_1_child_c = linked_t._add_children(p_root, "1_child_c")
    p_1_child_d = linked_t._add_children(p_root, "1_child_d")
    p_2_child_a = linked_t._add_children(p_1_child_a, "2_child_a")
    p_3_child_a = linked_t._add_children(p_2_child_a, "3_child_a")
    p_3_child_b = linked_t._add_children(p_2_child_a, "3_child_b")
    p_3_child_c = linked_t._add_children(p_2_child_a, "3_child_c")
    element_ls = list()
    for position in linked_t.positions():
        element_ls.append(position.element())
    print(f"element_ls = {element_ls}")
    print(f"element_count = {len(element_ls)}")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")

    element_ls = list()
    delete_element = linked_t._delete(p_1_child_a)
    # delete_element = linked_t._delete(p_root)
    print(f"delete_element = {delete_element}")
    # root_children = [p_child.element() for p_child in linked_t.children(p_root)]
    # print(f"root_children={root_children}")
    # p_1_child_a_children = [p_child.element() for p_child in linked_t.children(p_1_child_a)]
    # print(f"p_1_child_a_children={p_1_child_a_children}")
    # p_2_child_a_children = [p_child.element() for p_child in linked_t.children(p_2_child_a)]
    # print(f"p_2_child_a_children={p_2_child_a_children}")
    for position in linked_t.positions():
        element_ls.append(position.element())
    print(f"element_ls = {element_ls}")
    print(f"element_count = {len(element_ls)}")
    print(len(linked_t))
    p_root = linked_t.root()
    print(f"p_root.element() = {p_root.element()}")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
