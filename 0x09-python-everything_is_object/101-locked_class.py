#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
dynamically created an instance
"""


class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']

