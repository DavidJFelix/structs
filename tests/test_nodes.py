#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# structs/tests/test_nodes.py
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

import unittest
from structs import nodes

class NodeTestCase(unittest.TestCase):
    """A test case for the Node class.
    This test case tests different elements of Node for expected behaviors.
    These tests are interdependant, and any test failure that this test does not
    account as less important could possibly indicate flawed test results for
    other passed (or failed) tests in this case.
    """

    def setUp(self):
        self.test_obj_empty = nodes.Node()
        self.test_obj_full = nodes.Node(1)

    def test_data_get(self):
        """Test get techniques for data explicitly. Implicitly test __init__.
        This test will check that _data is properly by __init__ and that the
        data get method correctly returns the value stored in data. This test
        also checks that set values on can be gotten properly. This portion of
        the test overlaps part of test_data_set's test. Half of this test relies
        on a functioning set data method to return correct test results."""

        self.assertIsNone(self.test_obj_empty._data,
                          '_data should be initialized as None',
                         )
        self.assertEqual(self.test_obj_empty.data,
                         self.test_obj_empty._data,
                         'getter for data should return same value as _data',
                        )
        self.assertEqual(self.test_obj_full._data,
                         1,
                         '_data should be initialized as 1',
                        )
        self.assertEqual(self.test_obj_full.data,
                         self.test_obj_full._data,
                        'getter for data should return same value as _data',
                        )
        self.test_obj_empty.data = 2
        self.test_obj_full.data = 2
        self.assertEqual(self.test_obj_empty._data,
                         2,
                         '_data was set to 2 and should now return 2',
                        )
        self.assertEqual(self.test_obj_empty.data,
                         self.test_obj_empty._data,
                         'getter for data should return same value as _data',
                        )
        self.assertEqual(self.test_obj_full.data,
                         2,
                         '_data was set to 2 and should now return 2',
                        )
        self.assertEqual(self.test_obj_full.data,
                         self.test_obj_full._data,
                         'getter for data should return same value as _data',
                        )

    def test_data_set(self):
        """Test set techniques for data explicitly.
        This test will check that _data is properly set by invoking data's set
        method. This test relies on a properly functioning get method, and may
        return false passes if test_data_get has failed before it."""

        # Properly set data test
        self.test_obj_empty.data = 2
        self.test_obj_full.data = 2
        self.assertEqual(self.test_obj_empty._data,
                         2,
                         '_data should have been set to 2',
                        )
        self.assertEqual(self.test_obj_empty.data,
                         2,
                         'data should return a 2 after being set to 2',
                        )
        self.assertEqual(self.test_obj_full._data,
                         2,
                         '_data should have been set to 2',
                        )
        self.assertEqual(self.test_obj_full.data,
                         2,
                         'data should return a 2 after being set to 2',
                        )

    def test_data_set_fail(self):
        """Test that set for data fails when done improperly."""

        # Improperly set data test
        with self.assertRaises(AttributeError):
            self.test_obj_empty._data = 2

        with self.assertRaises(AttributeError):
            self.test_obj_full._data = 2

        self.assertIsNone(self.test_obj_empty._data,
                          '_data should not have been set to 2',
                         )
        self.assertEqual(self.test_obj_empty.data,
                         self.test_obj_empty._data,
                         'data should not return a 2 after not being set to 2',
                        )
        self.assertEqual(self.test_obj_full._data,
                         1,
                         '_data should have not been set to 2',
                        )
        self.assertEqual(self.test_obj_full.data,
                         self.test_obj_full._data,
                         'data should not return a 2 after not being set to 2',
                        )

    def tearDown(self):
        del self.test_obj

class LinkedNodeTestCase(NodeTestCase):
    """A test case for the LinkedNode class.
    """

    def setUp(self):
        self.test_obj_empty = nodes.LinkedNode()
        self.test_obj_full = nodes.LinkedNode(1)

    def test_right(self):
        # Ensure that _right is initialized as None
        self.assertIsNone(self.test_obj._right,
                    'data should be initialized as None')

        # Ensure that get for right works initially
        self.assertIsNone(self.test_obj.right,
                    'getter for data should return None now')

        # Ensure that set for right works for LinkedNode
        self.test_obj.right = self.linked_node
        self.assertEqual(self.test_obj._right,
                    self.linked_node,
                    '_right should be set when setting right')
        self.assertEqual(self.test_obj.right,
                    self.linked_node,
                    'right should return value set above')

        # Ensure that set for right works for other Nodes
        self.test_obj.right = self.node
        self.assertEqual(self.test_obj._right,
                    self.node,
                    '_right should be set when setting right')
        self.assertEqual(self.test_obj.right,
                    self.node,
                    'right should return value set above')

        # Ensure that set does NOT work for non-Node types
        self.assertRaisesself.test_obj.right = 1

def get_test_suite():
    """A function which generates a test suite for the nodes.py file.
    """
    nodes_test_suite = unittest.TestSuite()
    test_loader = nodes_test_suite.TestLoader()
    test_loader.loadTestsFromTestCase(NodeTestCase)
    test_loader.loadTestsFromTestCase(LinkedNodeTestCase)
    return nodes_test_suite

def run_test():
    nodes_test_suite = get_test_suite()
    tester = unittest.TextTestRunner(verbosity = 2)
    tester.run(nodes_test_suite)

if __name__ == '__main__':
    run_test()
