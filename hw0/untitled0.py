#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 17:04:40 2020

@author: jtwong
"""


def looper():

    n = int(1e6)
    a = [0]*n
    while True:
        for k in range(n):
            a[k] = 0
        for k in range(n):
            a[k] = k**3
