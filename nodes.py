#!/usr/bin/env python3
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
    """A container class which is used for creating complex data structures.
    Node is not inteded for any specific purpose but to be inherited when
    creating more complex classes.

    Attributes:
        _data:
            where data is stored. Code and users should not interact with the
            stored data this way, but should instead interact with the 'data'
            propery.

    Properties:
        data:
            how code interacts with the _data attribute."""

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

class LinkedNode(Node):
    """A container class with one child.
    LinkedNode inherits Node and is the simplest container with an intended
    purpose. LinkedNode has one child and can used to create unidirectional
    chained containers, such as simple lists, queues or stacks.

    Attributes:
        _next:
            where the next node is stored"""

    def __init__(self, data = None, next = None):
        super(LinkedNode, self).__init__(data)
        self._next = next

    @property
    def next(self):
        """The next property stores the next node that is linked"""
        return self._next

    @next.setter
    def next(self, value):
        if isinstance(value, Node):
            self._data = value

        else:
            raise TypeError('next cannot be assigned to a non-Node-inherited type')

    @next.deleter
    def next(self):
        del self._next
        self._next = None

class BiLinkedNode(LinkedNode):
    """A bidirectional container class with one child"""

    def __init__(self, data = None, next = None, prev = None):
        super(BiLinkedNode, self).__init__(data, next)
        self._prev = prev

    @property
    def prev(self):
        """The prev property stores the previous node that is linked"""
        return self._prev

    @prev.setter
    def prev(self, value):
        if isinstance(value, Node):
            self._prev = value

        else:
            raise TypeError('prev cannot be assigned to a non-Node-inherited type')

    @prev.deleter
    def prev(self):
        self._prev = None

class BinaryNode(Node):
    """A container class with two children"""

    def __init__(self, data = None, left = None, right = None):
        super(BinaryNode, self).__init__(data)
        self._left = left
        self._right = right

    @property
    def left(self):
        """The left property stores the left child node that is linked"""
        return self._left

    @left.setter
    def left(self, value):
        if isinstance(value, Node):
            self._left = value

        else:
            raise TypeError('left cannot be assigned to a non-Node-inherited type')

    @left.deleter
    def left(self):
        self._left = None

    @property
    def right(self):
        """The right property stores the right child node that is linked"""
        return self._right

    @right.setter
    def right(self, value):
        if isinstance(value, Node):
            self._right = value

        else:
            raise TypeError('right cannot be assigned to a non-Node-inherited type')

    @right.deleter
    def right(self):
        self._right = None

class BiBinaryNode(BinaryNode):
    """A bidirectional container class with two children"""

    def __init__(self, data = None, left = None, right = None, parent = None):
        super(BiBinaryNode, self).__init__(data, left, right)
        self._parent = parent

    @property
    def parent(self):
        """The parent property stores the parent node that is linked"""
        return self._parent

    @parent.setter
    def parent(self, value):
        if isinstance(value, Node):
            self._parent = value

        else:
            raise TypeError('parent cannot be assigned to a non-Node-inherited type')

    @parent.deleter
    def parent(self):
        self._parent = None

class MultiNode(Node):
    """A container class with any number of children"""

    def __init__(self, data = None, children = set()):
        super(MultiNode, self).__init__(data)
        self._children = children

    @property
    def children(self):
        """The children property stores a set of linked children"""
        return self._children

    @children.setter
    def children(self, value):
        self._children = value

    @children.deleter
    def children(self):
        self._children = set()

class BiMultiNode(MultiNode):
    """A container class with any number of unordered children and parents"""

    def __init__(self, data = None, children = set(), parents = set()):
        super(BiMultiNode, self).__init__(data, children)
        self._parents = parents

    @property
    def parents(self):
        """The parents property stores a set of linked parents"""
        return self._parents

    @parents.setter
    def parents(self, value):
        self._parents = value

    @parents.deleter
    def parents(self):
        self._parents = set()

class OrderedMultiNode(Node):
    """A container class with any number of ordered children"""

    def __init__(self, data = None, children = []):
        super(OrderedMultiNode, self).__init__(data)
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
        self._children = []

class BiOrderedMultiNode(OrderedMultiNode):
    """A bidirectional container class with any number of ordered children"""

    def __init__(self, data = None, children = [], parents = []):
        super(BiOrderedMultiNode, self).__init__(data, children)
        self._parent = parents

    @property
    def parents(self):
        """"""
        return self._parents

    @parents.setter
    def parents(self, value):
        self._parents = value

    @parents.deleter
    def parents(self):
        self._parents = []
