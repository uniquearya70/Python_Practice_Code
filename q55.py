#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 02:11:20 2018

@author: arpitansh
"""

'''
Write a program which accepts a sequence of words separated by whitespace as input 
to print the words composed of digits only.

Example:
If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

In case of input data being supplied to the question, it should be assumed to be
 a console input.

Hints:

Use re.findall() to find all substring using regex.
'''
import re
s = input()
print (re.findall("\d+",s))