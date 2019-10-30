#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 14:53:43 2019

@author: navraj
"""





def print_grid(i,n):
    count=0
    plus='+'
    minus='-'
    down='|'
    space=" "
    while count<i:
        
        print((plus+(minus)*n)*i+plus)
        counter=1
        
        while counter<=n:
            print((down+(space)*n)*i+down)
            counter+=1
        count+=1
    
        
    print((plus+(minus)*n)*i+plus)
    
    if __name__ == '__main__':
        print_grid(i,n)
    
    
        
    
