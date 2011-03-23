#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# binary_trees.py
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

import nodes

class BinaryTree(nodes.BiBinaryNode):
    """A tree data structure in which each node has at most two child nodes"""

    def insert(self):
        pass

    def __iter__(self):
        """Recursively iterate in-order"""
        try:
            for each in self.left:
                yield each

        except(TypeError):
            pass

        yield self.data
        try:
            for each in self.right:
                yield each

        except(TypeError):
            pass

    def iter_in_order(self):
        """Recursively iterate in-order.
    Operates identically to __iter__(), but exists for calling consistancy"""
        return self.__iter__()

    def iter_pre_order(self):
        """Recursively iterate pre-order"""
        yield self.data
        try:
            for each in self.left:
                yield each

        except(TypeError):
            pass

        try:
            for each in self.right:
                yield each

        except(TypeError):
            pass
            
    def iter_post_order(self):
        """Recursively iterate post-order"""
        try:
            for each in self.left:
                yield each

        except(TypeError):
            pass

        try:
            for each in self.right:
                yield each

        except(TypeError):
            pass

        yield self.data
    
class AATree(RedBlackTree):
    """A variation of the red-black tree in which red nodes can only be added to
a right subchild"""
    pass

class AVLTree(BinarySearchTree):
    """A self-balancing binary search tree"""
    pass

class BinarySearchTree(BinaryTree):
    """An ordered or sorted binary tree"""
    pass

class CartesianTree(): #needs lookup
    """"""
    pass

class RandomizedBinarySearchTree(): #may be similar to treap
    pass

class RedBlackTree(BinarySearchTree):
    """A self-balancing binary search tree."""
    pass

class Rope(): #needs lookup, more informations
    pass

class ScapegoatTree(): #needs more information
    pass

class SelfBalancingBinarySearchTree(): #a group of trees, consisting of aa, avl, r/b. scape, splay, treap
    pass

class SplayTree(): #may not have a place in python implementation
    pass

class TTree(): #may not have a place in python implementation
    pass

class TangoTree(): #needs more information
    pass

class ThreadedBinaryTree(): #possible in python, need more info
    pass

class TopTree():
    pass

class Treap():
    pass

class VanEmdeBoasTree():
    pass

class WeightBalancedTree():
    pass
