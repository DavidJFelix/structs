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

class Node:
    """
    """
    def __abs__(self):
        return abs(self.content)

    def __add__(self, other):
        return self.content + other

    def __and__(self, other):
        return self.content & other

    def __bool__(self):
        return bool(self.content)

    def __call__(self, *args):
        return self.content(*args)

    def __complex__(self):
        return complex(self.content)

    def __contains__(self, item):
        return item in self.content

#    def __del__(self):
#        pass
#
#    def __delete__(self, insance):
#        pass
#
#    def __delattr__(self, name):
#        pass
#
#    def __delitem__(self, key):
#        pass
#
#    def __dir__(self):
#        pass
#

    def __divmod__(self, other):
        return divmod(self.content, other)

#    def __enter__(self):
#        pass
#
    def __eq__(self, other):
        return self.content == other

#    def __exit__(self):
#        pass
#
    def __floordiv__(self, other):
        return self.content // other

    def __float__(self):
        return float(self.content)

    def __format__(self):
        return format(self.content)

    def __ge__(self, other):
        return self.content >= other

#    def __get__(self, insance, owner):
#        pass
#
#    def __getattr__(self, name):
#        pass
#
#    def __getattribute(self, name):
#        pass
#
    def __getitem__(self, key):
        return self.content[key]

    def __gt__(self, other):
        return self.content > other

    def __hash__(self):
        return hash(self.content)

    def __le__(self, other):
        return self.content <= other

    def __len__(self):
        return len(self.content)

    def __lshift__(self, other):
        return self.content << other

    def __lt__(self, other):
        return self.content < other

    def __iadd__(self, other):
        self.content += other
        return self.content

    def __iand__(self, other):
        self.content &= other
        return self.content

    def __ifloordiv__(self, other):
        self.content //= other
        return self.content

    def __ilshift__(self, other):
        self.content <<= other
        return self.content

    def __imod__(self, other):
        self.content %= other
        return self.content

    def __imul__(self, other):
        self.content *= other
        return self.content

    def __index__(self):
        return self.content.__index__()

    def __init__(self, content, parent = None):
        self.content = content
        self.parent = parent
        self.children = []

    def __int__(self):
        return int(self.content)

    def __invert__(self):
        return ~self.content

    def __ior__(self, other):
        self.content |= other
        return self.content

#    def __instancecheck__(self, instance):
#        pass
#
    def __ipow__(self, other, *modulo):
        self.content = pow(self.content, other, *modulo)
        return self.content

    def __irshift__(self, other):
        self.content >>= other
        return self.content

    def __isub__(self, other):
        self.content -= other
        return self.content

#    def __iter__(self):
#        pass
#
    def __itruediv__(self, other):
        self.content /= other
        return self.content

    def __ixor__(self, other):
        self.content ^= other
        return self.content

    def __mod__(self, other):
        return self.content % other

    def __mul__(self, other):
        return self.content * other

    def __ne__(self, other):
        return self.content != other

    def __neg__(self):
        return -self.content

#    def __new__(cls[, ...]):
#        pass
#
    def __or__(self, other):
        return self.content | other

    def __pos__(self):
        return +self.content

    def __pow__(self,other, *modulo):
        return pow(self.content, other, *modulo)

    def __radd__(self, other):
        return other + self.content

    def __rand__(self, other):
        return other & self.content

    def __rdivmod__(self, other):
        return divmod(other, self.content)

    def __repr__(self):
        return repr(self.content)

    def __reversed__(self):
        return reversed(self.content)

    def __rfloordiv__(self, other):
        return other // self.content

    def __rlshift__(self, other):
        return other << self.content

    def __rmod__(self, other):
        return other % self.content

    def __rmul__(self, other):
        return other * self.content

    def __ror__(self, other):
        return other | self.content

    def __round__(self, *n):
        return round(self.content, *n)

    def __rpow__(self, other):
        return other ** self.content

    def __rrshift__(self, other):
        return other >> self.content

    def __rshift__(self, other):
        return self.content >>  other

    def __rsub__(self, other):
        return other - self.content

    def __rtruediv__(self, other):
        return other / self.content

    def __rxor__(self, other):
        return other ^ self.content

#    def __set__(self, instance, value):
#        pass
#
#    def __setattr(self, name, value):
#        pass
#
#    def __setitem__(self, key):
#        pass
#
#    def __slots__(self):
#        pass
#
    def __str__(self):
        return str(self.content)

    def __sub__(self, other):
        return self.content - other

#    def __subclasscheck__(self, subclass):
#        pass
#
    def __truediv__(self, other):
        return self.content / other

    def __xor__(self, other):
        return self.content ^ other

# New node types should be added here and should probably inherit Node


        

