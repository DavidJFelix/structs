#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# structs/nodes.py
#
# Copyright (c) 2011 David J Felix
#
# Contributors:
#                    [Add your name here]
#
# Licensed under the Apache License, Version 2.0 (the "License");  you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at:
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#
# Alternatively, the contents of this file may be used under the terms of 
# the LGPLv3+ (the  "Lesser GNU General Public License version 3 or later"),
# the GPLv3+ (the "GNU General Public License version 3 or later"),
# the AGPLv3+ (the "Affero GNU General Public License version 3 or later"),
# the MPLv1.1+ (the "Mozilla Public License version 1.1 or later"), in which
# case the provisions of LGPLv3+, GPLv3+, AGPLv3+, or MPLv1.1+ are respectively
# applicable instead of those above. If you wish to allow use of your version of
# this file only under the terms of the LGPLv3+, GPLv3+, AGPLv3+ or MPLv1.1 and
# not to allow others to use your version of this file under the Apache License,
# Version 2.0 or another of the above licenses, indicate your decision by
# deleting the provisions above and replace them with the notice and other
# provisions required by the LGPLv3+, GPLv3+, AGPLv3+, or MPLv1.1+ respectively.
# If you do not delete the provisions above, or modify this notice a recipient
# may use your version of this file under either the Apache License, Version 
# 2.0, the LGPLv3+, the GPLv3+, the AGPLv3+ or the MPLv1.1+. A full copy of the
# oldest allowable version of these licenses is available in the "licenses"
# directory, which is located in the root directory of this project.


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

    node_err = 'linked nodes must be a Node-inherited type'
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
    def are_nodes(iterable):
        for each in iterable:
            if not isinstance(each, Node):
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

        _next:
            where the next node is stored. Code and users should not interact
            with the stored next this way, but should instead interact with the 
            'next' propery.

    Properties:
        data:
            how code and users interact with the _data attribute.

        next:
            how code and users interact with the _next attribute.
    """

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
            self._next = value

        else:
            raise TypeError(self.node_err)

    @next.deleter
    def next(self):
        self._next = None

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

        _next:
            where the next node is stored. Code and users should not interact
            with the stored next this way, but should instead interact with the 
            'next' propery.

        _prev:
            where the previous node is stored. Code and users should not
            interact with the stored previous this way, but should instead
            interact with the 'prev' property.

    Properties:
        data:
            how code and users interact with the _data attribute.

        next:
            how code and users interact with the _next attribute.

        prev:
            how code and users interact with the _prev attribute.
    """

    def __init__(self, data = None, next = None, prev = None):
        super(BinaryNode, self).__init__(data, next)
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
            raise TypeError(self.node_err)

    @prev.deleter
    def prev(self):
        self._prev = None

class BiBinaryNode(BinaryNode):
    """A bidirectional container class with two children.
    BiBinaryNode has two children and one parent and can be used to create
    bidirectional binary trees.

    Attributes:
        _data:
            where data is stored. Code and users should not interact with the
            stored data this way, but should instead interact with the 'data'
            propery.

        _next:
            where the next node is stored. Code and users should not interact
            with the stored next this way, but should instead interact with the 
            'next' propery.

        _prev:
            where the previous node is stored. Code and users should not
            interact with the stored previous this way, but should instead
            interact with the 'prev' property.


        _parent:
            where the parent node is stored. Code and users should not interact
            with the stored parent this way, but should instead interact with
            the 'parent' property.

    Properties:
        data:
            how code and users interact with the _data attribute.

        next:
            how code and users interact with the _next attribute.

        prev:
            how code and users interact with the _prev attribute.

        parent:
            how code and users interact with the _parent attribute.
    """

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
        super(MultiNode, self).__init__(data)
        if isinstance(children, set):
            self._children = children

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
        super(BiMultiNode, self).__init__(data, children)
        if isinstance(parents, set):
            self._parents = parents

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
        super(OrderedMultiNode, self).__init__(data)
        if isinstance(children, list):
            self._children = children

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
        super(BiOrderedMultiNode, self).__init__(data, children)
        if isinstance(parents, list):
            self._parents = parents

        else:
            raise TypeError(self.list_err)

    @property
    def parents(self):
        """The parents property stores an ordered list of linked parents"""
        return self._parents

    @parents.setter
    def parents(self, value):
        if isinstance(value, list):
            if self.are_nodes(value)
                self._parents = value

            else:
                raise TypeError(self.node_err)

        else:
            raise TypeError(self.list_err)

    @parents.deleter
    def parents(self):
        self._parents = []
