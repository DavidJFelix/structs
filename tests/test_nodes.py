﻿#!/usr/bin/env python3
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
    These tests are interdependent and any test failure that this test does not
    account as less important could possibly indicate flawed test results for
    other passed (or failed) tests in this case. The tests that this case runs
    are for the functioning of the "data" attribute of the Node, as this is all
    that Node has; Since all other types of Nodes inherit from this Node, all
    other test cases should inherit this test case directly or through a parent.
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
        on a functioning set data method to return correct test results.
        """

        # Check initialized data for test_obj_empty
        self.assertIsNone(self.test_obj_empty._data,
                          '_data should be initialized as None',
                         )
        self.assertEqual(self.test_obj_empty.data,
                         self.test_obj_empty._data,
                         'getter for data should return same value as _data',
                        )

        # Check initialized data for test_obj_full
        self.assertEqual(self.test_obj_full._data,
                         1,
                         '_data should be initialized as 1',
                        )
        self.assertEqual(self.test_obj_full.data,
                         self.test_obj_full._data,
                        'getter for data should return same value as _data',
                        )

        # Change the values of data to check that get retrives the new values
        # Tests below here are dependent on a working set function for data
        self.test_obj_empty.data = 2
        self.test_obj_full.data = 2

        # Check data of test_obj_empty again
        self.assertEqual(self.test_obj_empty._data,
                         2,
                         '_data was set to 2 and should now return 2',
                        )
        self.assertEqual(self.test_obj_empty.data,
                         self.test_obj_empty._data,
                         'getter for data should return same value as _data',
                        )

        # Check data of test_obj_full again
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
        return false passes if test_data_get has failed before it.
        """

        # Properly set data test
        self.test_obj_empty.data = 2
        self.test_obj_full.data = 2

        # Tests below here are dependent on a working get function for data
        # Check data of test_obj_empty for new values
        self.assertEqual(self.test_obj_empty._data,
                         2,
                         '_data should have been set to 2',
                        )
        self.assertEqual(self.test_obj_empty.data,
                         2,
                         'data should return a 2 after being set to 2',
                        )

        # Check data of test_obj_full for new values
        self.assertEqual(self.test_obj_full._data,
                         2,
                         '_data should have been set to 2',
                        )
        self.assertEqual(self.test_obj_full.data,
                         2,
                         'data should return a 2 after being set to 2',
                        )

    def test_data_set_inprop(self):
        """Test the behavior for setting _data, which is considered incorrect.
        This tests the way that data is handled when an inpropper attempt is
        made to change it. The expected behavior is to set the value of data,
        in this case with no property protections. User beware.
        """

        # Improperly set data
        self.test_obj_empty._data = 2
        self.test_obj_full._data = 2

        # Tests below here are dependent on a working get function for data
        # Check data of test_obj_empty for no change
        self.assertIsNone(self.test_obj_empty._data,
                          '_data should still have been set to 2',
                         )
        self.assertEqual(self.test_obj_empty.data,
                         self.test_obj_empty._data,
                         'data should return a 2 after being set to 2',
                        )

        # Check data of test_obj_full for no change
        self.assertEqual(self.test_obj_full._data,
                         1,
                         '_data should still have been set to 2',
                        )
        self.assertEqual(self.test_obj_full.data,
                         self.test_obj_full._data,
                         'data should return a 2 after being set to 2',
                        )

    def test_data_delete(self):
        """Test delete techniques for data.
        This tests that when data is deleted, the expected action, setting data
        to None, occurs. data and _data should still be usable if 'del data' is
        declared.
        """

        self.test_obj_empty.data = 2
        # Tests below here are dependent on a working set function for data
        # Properly delete data for test
        del self.test_obj_empty.data
        del self.test_obj_full.data

        # Check data of test_obj_empty for None
        self.assertIsNone(self.test_obj_empty._data,
                          '_data should have been set to None by the delete',
                         )
        self.assertEqual(self.test_obj_empty.data,
                         self.test_obj_empty._data,
                         'data should return None just as _data did'
                        )

        # Check data of test_obj_full for None
        self.assertIsNone(self.test_obj_full._data,
                          '_data should have been set to None by the delte',
                         )
        self.assertEqual(self.test_obj_full.data,
                         self.test_obj_full._data,
                         'data should return None just as _data did'
                        )

    def test_data_delete_inprop(self):
        """Test boundary cases for deleting _data.
        This tests ways for expected results when somebody declares 'del _data'.
        Expected behavior is that _data and data will become unusable. This
        action normally would be protected against, but there may be boundary
        cases where deleting _data like this is necessary. Protection for users
        has been added by making data a property to begin with, messing around
        with underscore variables should be enough of a warning.
        """

        # Delete data improperly via _data
        del self.test_obj_empty._data
        del self.test_obj_full._data

        # Test that _data gets deleted for real
        with self.assertRaises(AttributeError):
            self.test_obj_empty._data

        with self.assertRaises(AttributeError):
            self.test_obj_empty.data

        with self.assertRaises(AttributeError):
            self.test_obj_full._data

        with self.assertRaises(AttributeError):
            self.test_obj_full.data

        # Test that a set still works
        self.test_obj_empty.data = 2
        self.test_obj_full.data = 2
        self.asserEqual(self.test_obj_empty.data,
                        2,
                        'data should now be 2',
                        )
        self.asserEqual(self.test_obj_full.data,
                        2,
                        'data should now be 2',
                        )
        
    def test_are_nodes(self):
        """Test for the are_nodes() static method.
        This tests that the are_nodes() function is correctly identifying lists
        that are entirely composed of nodes
        """

        # Create a few lists of different compositions to test with
        node_list = [self.test_obj_empty, self.test_obj_full]
        mixed_list = [self.test_obj_empty, 1]
        int_list = [1, 2]

        # Test both existing nodes' are_nodes() using a list of entirely nodes
        self.assertTrue(self.test_obj_empty.are_nodes(node_list),
                        'A list of nodes passed to are_nodes() should ' + \
                        'return True',
                       )
        self.assertTrue(self.test_obj_full.are_nodes(node_list),
                        'A list of nodes passed to are_nodes() should ' + \
                        'return True',
                       )

        # Test both existing nodes' are_nodes() using a mixed list
        self.assertFalse(self.test_obj_empty.are_nodes(mixed_list),
                         'A mixed list of nodes and non-nodes passed to ' + \
                         'are_nodes() should return False',
                        )
        self.assertFalse(self.test_obj_full.are_nodes(mixed_list),
                         'A mixed list of nodes and non-nodes passed to ' + \
                         'are_nodes() should return False',
                        )

        # Test both existing nodes' are_nodes() using a list of entirely ints
        self.assertFalse(self.test_obj_empty.are_nodes(int_list),
                         'A list of ints passed to are_nodes() should ' + \
                         'return False',
                        }
        self.assertFalse(self.test_obj_full.are_nodes(int_list),
                         'A list of ints passed to are_nodes() should ' + \
                         'return False',
                        }

    def tearDown(self):
        """The unittest tearDown function for this test case.
        This function will clean up between each test of the case to ensure
        encapsulated tests. Most inheriting test cases should leave this
        unchanged, or at the very least call super() on it.
        """
        del self.test_obj_empty
        del self.test_obj_full

class LinkedNodeTestCase(NodeTestCase):
    """A test case for the LinkedNode class.
    These tests are interdependent and any test failure that this test does not
    account as less important could possibly indicate flawed test results for
    other passed (or failed) tests in this case. This test case inherits
    NodeTestCase to test the functionality of data, but adds to the case by
    testing the functionality of "right".
    """

    def setUp(self):
        self.test_obj_empty = nodes.LinkedNode()
        self.test_obj_full = nodes.LinkedNode(1, self.test_obj_empty)

    def test_right_get(self):
        """Test get techniques for right explicitly. Implicitly test __init__.
        This test will check that _right is properly by __init__ and that the
        right get method correctly returns the value stored in right. This test
        also checks that set values on can be gotten properly. This portion of
        the test overlaps part of test_right_set's test. Half of this test
        relies on a functioning set right method to return correct test results.
        """

        # Check initialized right of test_obj_empty
        self.assertIsNone(self.test_obj_empty._right,
                          '_right should be initialized as None',
                         )
        self.assertEqual(self.test_obj_empty.right,
                         self.test_obj_empty._right,
                         'getter for right should return same value as _right',
                        )

        # Check initialized right of test_obj_full
        self.assertEqual(self.test_obj_full._right,
                         self.test_obj_empty,
                         '_right should be initialized as test_obj_full',
                        )
        self.assertEqual(self.test_obj_full.right,
                         self.test_obj_full._right,
                        'getter for right should return same value as _right',
                        )

        # Tests below here are dependent on a working set and delete function
        # for right
        # Change the values to of right check that get retrieves the new values
        self.test_obj_empty.right = self.test_obj_full
        del self.test_obj_full.right

        # Check right of test_obj_empty again
        self.assertEqual(self.test_obj_empty._right,
                         self.test_obj_full,
                         '_right was set to test_obj_full and should now ' + \
                         'return test_obj_full',
                        )
        self.assertEqual(self.test_obj_empty.right,
                         self.test_obj_empty._right,
                         'getter for right should return same value as _right',
                        )

        # Check right of test_obj_full again
        self.assertNone(self.test_obj_full.right,
                         '_right was deleted and should now return None',
                        )
        self.assertEqual(self.test_obj_full.right,
                         self.test_obj_full._right,
                         'getter for right should return same value as _right',
                        )

    def test_right_set(self):
        """Test set techniques for right explicitly.
        This test will check that _right is properly set by invoking right's set
        method. This test relies on a properly functioning get method, and may
        return false passes if test_right_get has failed before it.
        """

        # Properly set right
        self.test_obj_empty.right = self.test_obj_full
        self.test_obj_full.right = self.test_obj_empty

        # Check that right was set for test_obj_empty
        self.assertEqual(self.test_obj_empty._right,
                         self.test_obj_full,
                         '_right should have been set to test_obj_full',
                        )
        self.assertEqual(self.test_obj_empty.right,
                         self.test_obj_full,
                         'right should return test_obj_full after being set',
                        )

        # Check that right was set for test_ob_full
        self.assertEqual(self.test_obj_full._right,
                         self.test_obj_empty,
                         '_right should have been set to test_obj_empty',
                        )
        self.assertEqual(self.test_obj_full.right,
                         self.test_obj_empty,
                         'right should return test_obj_empty after being set',
                        )

    def test_right_set_inprop(self):
        """Test the behavior of setting _right, which is considered incorrect.
        This tests the way that right is handled when an inpropper attempt is
        made to change it.
        """

        # Improperly set right test
        self.test_obj_empty._right = self.test_obj_full
        self.test_obj_full._right = self.test_obj_empty

        self.assertIsNone(self.test_obj_empty._right,
                          '_right should not have been set to 2',
                         )
        self.assertEqual(self.test_obj_empty.right,
                         self.test_obj_empty._right,
                         'right should not return a 2 after not being set to 2',
                        )
        self.assertEqual(self.test_obj_full._right,
                         1,
                         '_right should have not been set to 2',
                        )
        self.assertEqual(self.test_obj_full.right,
                         self.test_obj_full._right,
                         'right should not return a 2 after not being set to 2',
                        )

class BinaryNodeTestCase(LinkedNodeTestCase):
    """A test case for the BinaryNode class.
    These tests are interdependent and any test failure that this test does not
    account as less important could possibly indicate flawed test results for
    other passed (or failed) tests in this case. This test case inherits
    LinkedNodeTestCase to test the functionality of data and right, but adds to
    the case by testing the functionality of "left".
    """

    def setUp(self):
        self.test_obj_empty = nodes.BinaryNode()
        self.test_obj_full = nodes.BinaryNode(1)

    def test_left_get(self):
        """Test get techniques for left explicitly. Implicitly test __init__.
        This test will check that _left is properly by __init__ and that the
        left get method correctly returns the value stored in left. This test
        also checks that set values on can be gotten properly. This portion of
        the test overlaps part of test_left_set's test. Half of this test
        relies on a functioning set left method to return correct test results.
        """

        self.assertIsNone(self.test_obj_empty._left,
                          '_left should be initialized as None',
                         )
        self.assertEqual(self.test_obj_empty.left,
                         self.test_obj_empty._left,
                         'getter for left should return same value as _left',
                        )
        self.assertEqual(self.test_obj_full._left,
                         1,
                         '_left should be initialized as 1',
                        )
        self.assertEqual(self.test_obj_full.left,
                         self.test_obj_full._left,
                        'getter for left should return same value as _left',
                        )
        self.test_obj_empty.left = 2
        self.test_obj_full.left = 2
        self.assertEqual(self.test_obj_empty._left,
                         2,
                         '_left was set to 2 and should now return 2',
                        )
        self.assertEqual(self.test_obj_empty.left,
                         self.test_obj_empty._left,
                         'getter for left should return same value as _left',
                        )
        self.assertEqual(self.test_obj_full.left,
                         2,
                         '_left was set to 2 and should now return 2',
                        )
        self.assertEqual(self.test_obj_full.left,
                         self.test_obj_full._left,
                         'getter for left should return same value as _left',
                        )

    def test_left_set(self):
        """Test set techniques for left explicitly.
        This test will check that _left is properly set by invoking left's set
        method. This test relies on a properly functioning get method, and may
        return false passes if test_left_get has failed before it.
        """

        # Properly set left test
        self.test_obj_empty.left = 2
        self.test_obj_full.left = 2
        self.assertEqual(self.test_obj_empty._left,
                         2,
                         '_left should have been set to 2',
                        )
        self.assertEqual(self.test_obj_empty.left,
                         2,
                         'left should return a 2 after being set to 2',
                        )
        self.assertEqual(self.test_obj_full._left,
                         2,
                         '_left should have been set to 2',
                        )
        self.assertEqual(self.test_obj_full.left,
                         2,
                         'left should return a 2 after being set to 2',
                        )

    def test_left_set_fail(self):
        """Test that set for left fails when done improperly.
        This tests the way that left is handled when an inpropper attempt is
        made to change it.
        """

        # Improperly set left test
        with self.assertRaises(AttributeError):
            self.test_obj_empty._left = 2

        with self.assertRaises(AttributeError):
            self.test_obj_full._left = 2

        self.assertIsNone(self.test_obj_empty._left,
                          '_left should not have been set to 2',
                         )
        self.assertEqual(self.test_obj_empty.left,
                         self.test_obj_empty._left,
                         'left should not return a 2 after not being set to 2',
                        )
        self.assertEqual(self.test_obj_full._left,
                         1,
                         '_left should have not been set to 2',
                        )
        self.assertEqual(self.test_obj_full.left,
                         self.test_obj_full._left,
                         'left should not return a 2 after not being set to 2',
                        )

class BiBinaryNodeTestCase(BinaryNodeTestCase):
    """A test case for the BiBinaryNode class.
    These tests are interdependent and any test failure that this test does not
    account as less important could possibly indicate flawed test results for
    other passed (or failed) tests in this case. This test case inherits
    BinaryNodeTestCase to test the functionality of data, right and left, but
    adds to the case by testing the functionality of "parent".
    """

    def setUp(self):
        self.test_obj_empty = nodes.BiBinaryNode()
        self.test_obj_full = nodes.BiBinaryNode(1)

    def test_parent_get(self):
        """Test get techniques for parent explicitly. Implicitly test __init__.
        This test will check that _parent is properly by __init__ and that the
        parent get method correctly returns the value stored in parent. This
        test also checks that set values on can be gotten properly. This portion
        of the test overlaps part of test_parent_set's test. Half of this test
        relies on a functioning set parent method to return correct test
        results.
        """

        self.assertIsNone(self.test_obj_empty._parent,
                          '_parent should be initialized as None',
                         )
        self.assertEqual(self.test_obj_empty.parent,
                         self.test_obj_empty._parent,
                         'getter for parent should return same value as ' + \
                         '_parent',
                        )
        self.assertEqual(self.test_obj_full._parent,
                         1,
                         '_parent should be initialized as 1',
                        )
        self.assertEqual(self.test_obj_full.parent,
                         self.test_obj_full._parent,
                        'getter for parent should return same value as ' + \
                        '_parent',
                        )
        self.test_obj_empty.parent = 2
        self.test_obj_full.parent = 2
        self.assertEqual(self.test_obj_empty._parent,
                         2,
                         '_parent was set to 2 and should now return 2',
                        )
        self.assertEqual(self.test_obj_empty.parent,
                         self.test_obj_empty._parent,
                         'getter for parent should return same value as ' + \
                         '_parent',
                        )
        self.assertEqual(self.test_obj_full.parent,
                         2,
                         '_parent was set to 2 and should now return 2',
                        )
        self.assertEqual(self.test_obj_full.parent,
                         self.test_obj_full._parent,
                         'getter for parent should return same value as ' + \
                         '_parent',
                        )

    def test_parent_set(self):
        """Test set techniques for parent explicitly.
        This test will check that _parent is properly set by invoking parent's
        set method. This test relies on a properly functioning get method, and
        may return false passes if test_parent_get has failed before it.
        """

        # Properly set parent test
        self.test_obj_empty.parent = 2
        self.test_obj_full.parent = 2
        self.assertEqual(self.test_obj_empty._parent,
                         2,
                         '_parent should have been set to 2',
                        )
        self.assertEqual(self.test_obj_empty.parent,
                         2,
                         'parent should return a 2 after being set to 2',
                        )
        self.assertEqual(self.test_obj_full._parent,
                         2,
                         '_parent should have been set to 2',
                        )
        self.assertEqual(self.test_obj_full.parent,
                         2,
                         'parent should return a 2 after being set to 2',
                        )

    def test_parent_set_fail(self):
        """Test that set for parent fails when done improperly.
        This tests the way that parent is handled when an inpropper attempt is
        made to change it.
        """

        # Improperly set parent test
        with self.assertRaises(AttributeError):
            self.test_obj_empty._parent = 2

        with self.assertRaises(AttributeError):
            self.test_obj_full._parent = 2

        self.assertIsNone(self.test_obj_empty._parent,
                          '_parent should not have been set to 2',
                         )
        self.assertEqual(self.test_obj_empty.parent,
                         self.test_obj_empty._parent,
                         'parent should not return a 2 after not being set ' + \
                         'to 2',
                        )
        self.assertEqual(self.test_obj_full._parent,
                         1,
                         '_parent should have not been set to 2',
                        )
        self.assertEqual(self.test_obj_full.parent,
                         self.test_obj_full._parent,
                         'parent should not return a 2 after not being set ' + \
                         'to 2',
                        )

class TrinaryNodeTestCase(BiBinaryNodeTestCase):
    """A test case for the TrinaryNode class.
    This test should be identical to the BiBinaryNodeTestCase because
    TrinaryNode is an alias for BiBinaryNode. This test case just ensures that
    the alias is functioning correctly."""

    def setUp(self):
        self.test_obj_empty = nodes.TrinaryNode()
        self.test_obj_full = nodes.TrinaryNode(1)

class MultiNodeTestCase(NodeTestCase):
    """A test case fot the MultiNode class.
    These tests are interdependent and any test failure that this test does not
    account as less important could possibly indicate flawed test results for
    other passed (or faild) tests in this case. This test case inherits
    NodeTestCase to test the functionality of data, but adds to the case by
    testing the functionality of "children".
    """

    def setUp(self):
        self.test_obj_empty = nodes.MultiNode()
        self.test_obj_full = nodes.MultiNode(1)

    def test_children_get(self):
        pass

    def test_children_set(self):
        pass

    def test_children_set_fail(self):
        pass

class BiMultiNodeTestCase(MultiNodeTestCase):
    """
    """

    def setUp(self):
        self.test_obj_empty = nodes.BiMultiNode()
        self.test_obj_full = nodes.BiMultiNode(1)

class OrderedMultiNodeTestCase(NodeTestCase):
    """
    """

    def setUp(self):
        self.test_obj_empty = nodes.OrderedMultiNode()
        self.test_obj_full = nodes.OrderedMultiNode(1)

class BiOrderedMultiNodeTestCase(OrderedMultiNodeTestCase):
    """
    """

    def setUp(self):
        self.test_obj_empty = nodes.BiOrderedMultiNode()
        self.test_obj_full = nodes.BiOrderedMultiNode(1)

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
