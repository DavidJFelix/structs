#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# structs/nodes.py
#
# Copyright (c) 2011 David J Felix
#
# MIT/X11 License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
            how code and users interact with the _data attribute.
    """

    node_err = 'linked nodes must be a ' + str(self.__class__)
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
        self._data = None

    @staticmethod
    def are_nodes(iterable):    #needs testing
        for each in iterable:
            if not isinstance(each, self.__class__):
                return False

        return True

class LinkedNode(Node):
    """A container class with one child.
    LinkedNode inherits Node and is the simplest container with an intended
    purpose. LinkedNode has one child and can used to create unidirectional
    chained containers, such as simple lists, queues or stacks.

    Attributes:
        _data:
            where data is stored. Code and users should not interact with the
            stored data this way, but should instead interact with the 'data'
            propery.

        _right:
            where the right node is stored. Code and users should not interact
            with the stored right this way, but should instead interact with the
            'right' propery.

    Properties:
        data:
            how code and users interact with the _data attribute.

        right:
            how code and users interact with the _right attribute.
    """

    def __init__(self, data = None, right = None):
        super().__init__(data)
        if right and isinstance(right, self.__class__):
            self._right = right

        else:
            raise TypeError(self.node_err)

    @property
    def right(self):
        """The right property stores the right node that is linked"""
        return self._right

    @right.setter
    def right(self, value):
        if isinstance(value, Node):
            self._right = value

        else:
            raise TypeError(self.node_err)

    @right.deleter
    def right(self):
        self._right = None

class BinaryNode(LinkedNode):
    """A bidirectional container class with one child.
    BiLinkedNode has two children and can be used to create bidirectional
    chained containers, such as doubly-linked lists or to create unidirectional
    binary trees.

    Attributes:
        _data:
            where data is stored. Code and users should not interact with the
            stored data this way, but should instead interact with the 'data'
            propery.

        _right:
            where the right node is stored. Code and users should not interact
            with the stored right this way, but should instead interact with the 
            'right' propery.

        _left:
            where the left node is stored. Code and users should not interact
            with the stored left this way, but should instead interact with the
            'left' property.

    Properties:
        data:
            how code and users interact with the _data attribute.

        right:
            how code and users interact with the _right attribute.

        left:
            how code and users interact with the _left attribute.
    """

    def __init__(self, data = None, right = None, left = None):
        super().__init__(data, right)
        if left and isinstance(right, self.__class__):
            self._left = left

        else:
            raise TypeError(self.node_err)

    @property
    def left(self):
        """The left property stores the left node that is linked"""
        return self._left

    @left.setter
    def left(self, value):
        if isinstance(value, self.__class__):
            self._left = value

        else:
            raise TypeError(self.node_err)

    @left.deleter
    def left(self):
        self._left = None

class BiBinaryNode(BinaryNode):
    """A bidirectional container class with two children.
    BiBinaryNode has two children and one parent and can be used to create
    bidirectional binary trees.

    Attributes:
        _data:
            where data is stored. Code and users should not interact with the
            stored data this way, but should instead interact with the 'data'
            propery.

        _right:
            where the right node is stored. Code and users should not interact
            with the stored right this way, but should instead interact with the 
            'right' propery.

        _left:
            where the left node is stored. Code and users should not interact
            with the stored left this way, but should instead interact with the
            'left' property.


        _parent:
            where the parent node is stored. Code and users should not interact
            with the stored parent this way, but should instead interact with
            the 'parent' property.

    Properties:
        data:
            how code and users interact with the _data attribute.

        right:
            how code and users interact with the _right attribute.

        left:
            how code and users interact with the _left attribute.

        parent:
            how code and users interact with the _parent attribute.
    """

    def __init__(self, data = None, right = None, left = None, parent = None):
        super().__init__(data, left, right)
        if parent and isinstance(parent, self.__class__):
            self._parent = parent

        else:
            raise TypeError(self.node_err)

    @property
    def parent(self):
        """The parent property stores the parent node that is linked"""
        return self._parent

    @parent.setter
    def parent(self, value):
        if isinstance(value, Node):
            self._parent = value

        else:
            raise TypeError(self.node_err)

    @parent.deleter
    def parent(self):
        self._parent = None

class MultiNode(Node):
    """A container class with any number of children.
    Multinode has a set containing its children and can be used to create
    unidirectional trees or graphs, where child order does not matter.

    Attributes:
        _data:
            where data is stored. Code and users should not interact with the
            stored data this way, but should instead interact with the 'data'
            propery.

        _children:
            where the children set of nodes is stored. Code and users should not
            interact with the stored children this way, but should instead
            interact with the 'children' property.

    Properties:
        data:
            how code and users interact with the _data attribute.

        children:
            how code and users interact with the _children attribute.
    """

    set_err = 'must be of type "set"'
    def __init__(self, data = None, children = set()):
        super().__init__(data)
        if isinstance(children, set):
            if self.are_nodes(children):
                self._children = children

            else:
                raise TypeError(self.set_err)
        else:
            raise TypeError(self.set_err)

    @property
    def children(self):
        """The children property stores a set of linked children"""
        return self._children

    @children.setter
    def children(self, value):
        if isinstance(value, set):
            if self.are_nodes(value):
                self._children = value

            else:
                raise TypeError(self.node_err)

        else:
            raise TypeError(self.set_err)

    @children.deleter
    def children(self):
        self._children = set()

class BiMultiNode(MultiNode):
    """A container class with any number of unordered children and parents.
    BiMultiNode has a set containing its children and a set containing its
    parents and can be used to create bidirectional trees or graphs where child
    order and parent order do not matter.

    Attributes:
        _data:
            where data is stored. Code and users should not interact with the
            stored data this way, but should instead interact with the 'data'
            propery.

        _children:
            where the children set of nodes is stored. Code and users should not
            interact with the stored children this way, but should instead
            interact with the 'children' property.

        _parents:
            where the parents set of nodes is stored. Code and users should not
            interact with the stored parents this way, but should instead
            interact with the 'parents' property.

    Properties:
        data:
            how code and users interact with the _data attribute.

        children:
            how code and users interact with the _children attribute.

        parents:
            how code and users interact with the _parents attribute.
    """

    def __init__(self, data = None, children = set(), parents = set()):
        super().__init__(data, children)
        if isinstance(parents, set):
            if self.are_nodes(parents):
                self._parents = parents

            else:
                raise TypeError(self.node_err)

        else:
            raise TypeError(self.set_err)

    @property
    def parents(self):
        """The parents property stores a set of linked parents"""
        return self._parents

    @parents.setter
    def parents(self, value):
        if isinstance(value, set):
            if self.are_nodes(value):
                self._parents = value

            else:
                raise TypeError(self.node_err)
        else:
            raise TypeError(self.set_err)

    @parents.deleter
    def parents(self):
        self._parents = set()

class OrderedMultiNode(Node):
    """A container class with any number of ordered children.
    OrderedMultiNode has a list containing its children and can be used to
    create unidirectional trees or graphs where order of children matters.

    Attributes:
        _data:
            where data is stored. Code and users should not interact with the
            stored data this way, but should instead interact with the 'data'
            propery.

        _children:
            where the children list of nodes is stored. Code and users should
            not interact with the stored children this way, but should instead
            interact with the 'children' property.

    Properties:
        data:
            how code and users interact with the _data attribute.

        children:
            how code and users interact with the _children attribute.
    """

    list_err = 'must be of type "list"'
    def __init__(self, data = None, children = []):
        super().__init__(data)
        if isinstance(children, list):
            if self.are_nodes(children):
                self._children = children

            else:
                raise TypeError(self.node_err)

        else:
            raise TypeError(self.list_err)

    @property
    def children(self):
        """The children property stores an ordered list of linked children"""
        return self._children

    @children.setter
    def children(self, value):
        if isinstance(value, list):
            if self.are_nodes(value)
                self._children = value

            else:
                raise TypeError(self.node_err)

        else:
            raise TypeError(self.list_err)

    @children.deleter
    def children(self):
        self._children = []

class BiOrderedMultiNode(OrderedMultiNode):
    """A bidirectional container class with any number of ordered children.
    BiOrderedMultiNode has a list containing its children and a list containing
    its parents and can be used to create bidirectional trees or graphs where
    child order and parent order matter.

    Attributes:
        _data:
            where data is stored. Code and users should not interact with the
            stored data this way, but should instead interact with the 'data'
            propery.

        _children:
            where the children list of nodes is stored. Code and users should 
            not interact with the stored children this way, but should instead
            interact with the 'children' property.

        _parents:
            where the parents list of nodes is stored. Code and users should not
            interact with the stored parents this way, but should instead
            interact with the 'parents' property.

    Properties:
        data:
            how code and users interact with the _data attribute.

        children:
            how code and users interact with the _children attribute.

        parents:
            how code and users interact with the _parents attribute.
    """

    def __init__(self, data = None, children = [], parents = []):
        super().__init__(data, children)
        if isinstance(parents, list):
            if self.are_nodes(parents):
                self._parents = parents

            else:
                raise TypeError(self.node_err)

        else:
            raise TypeError(self.list_err)

    @property
    def parents(self):
        """The parents property stores an ordered list of linked parents"""
        return self._parents

    @parents.setter
    def parents(self, value):
        if isinstance(value, list):
            if self.are_nodes(value):
                self._parents = value

            else:
                raise TypeError(self.node_err)

        else:
            raise TypeError(self.list_err)

    @parents.deleter
    def parents(self):
        self._parents = []

if __name__ == '__main__':
    from structs.tests import test_nodes
    test_nodes.run_test()
