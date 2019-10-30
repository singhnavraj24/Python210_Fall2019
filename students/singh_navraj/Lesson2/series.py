#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:28:33 2019

@author: navraj
"""

def fib(n):
    
        if n==0:
            return 0
        elif n==1:
            return 1
        return fib(n-2) + fib(n-1)
        
if __name__ == "__main__":
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13