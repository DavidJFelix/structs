#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#
# nodes.py
#
# Copyright (C) 2011  David J Felix
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more
# details.
#
# You should have received a copy of the GNU Affero General Public License along
# with this program. If not, see <http://www.gnu.org/licenses/>.

class Node(object):
    """A container class which is used for creating complex data structures."""

    def __init__(self, data = None):
        self._data = data

    @property
    def data(self):
        """The data property stores what is contained in the node"""
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @data.deleter
    def data(self):
        del self._data
        self._data = None

# New node types should be added here and should probably inherit Node
class LinkedNode(Node):
    """A container class with one child"""

    def __init__(self, data = None, next = None):
        super(Node, self).__init__(self, data)
        self._next = next

    @property
    def next(self):
        """The next property stores the node that is linked"""
        return self._next

    @next.setter
    def next(self, value):
        self._data = value

    @next.deleter
    def next(self):
        del self._next
        self._next = None

class BiLinkedNode(LinkedNode):
    """A bidirectional container class with one child"""

    def __init__(self, data, next, prev):
        super(LinkedNode, self).__init__(self, data, next)
        self._prev = prev

    @property
    def prev(self):
        """"""
        return self._prev

    @prev.setter
    def prev(self, value):
        self._prev = value

    @prev.deleter
    def prev(self):
        del self._prev
        self._prev = None

class BinaryNode(Node):
    """A container class with two children"""

    def __init__(self, data, left = None, right = None):
        super(Node, self).__init__(self, data):
        self._left = left
        self._right = right

    @property
    def left(self):
        """"""
        return self._left

    @left.setter
    def left(self, value):
        """"""
        self._left = value

    @left.deleter
    def left(self):
        del self._left
        self._left = None

    @property
    def right(self):
        """"""
        return self._right

    @right.setter
    def right(self, value):
        self._right = value

    @right.deleter
    def right(self):
        del self._right
        self._right = None

class BiBinaryNode(BinaryNode):
    """A bidirectional container class with two children"""

    def __init__(self, data, left = None, right = None, parent = None):
        super(BinaryNode, self).__init__(self, data, left, right)
        self._parent = parent

`   @property
    def parent(self):
        """"""
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @parent.deleter
    def parent(self):
        del self._parent
        self._parent = None

class MultiNode(Node):
    """A container class with any number of children"""

    def __init__(self, data, children = set()):
        super(Node, self).__init__(self, data)
        self._children = children

    @property
    def children(self):
        """"""
        return self._children

    @children.setter
    def children(self, value):
        self._children = value

    @children.deleter
    def children(self):
        del self._children
        self._children = set()

class BiMultiNode(MultiNode):
    """A container class with any number of unordered children and parents"""

    def __init__(self, data, children = set(), parents = set()):
        super(MultiNode, self).__init__(self, data, children)
        self._parents = parents

    @property
    def parents(self):
        """"""
        return self._parents

    @parents.setter
    def parents(self, value):
        self._parents = value

    @parents.deleter
    def parents(self)
        del self._parents
        self._parents = set()

class OrderedMultiNode(MulitNode):
    """A container class with any number of ordered children"""

    def __init__(self, data, children = [])
        super(MultiNode, self).__init__(self, data, children)

    @children.deleter
    def children(self):
        del self._children
        self._children = []

class BiOrderedMultiNode(BiMultiNode):
    """A bidirectional container class with any number of ordered children"""

    def __init__(self, data, children = [], parents = []):
        super(BiMultiNode, self).__init__(self, data, children, parents)

    @parents.deleter
    def parents(self):
        del self._parents
        self._parents = []