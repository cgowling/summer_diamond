#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 09:37:18 2017

@author: jdn93577
"""
from collections import OrderedDict

test = {"one":1, "two":2,"three":3}
#test["first"] = {"one":1, "two":2,"three":3}
#test["second"]= {"A":1, "B":2,"C":3}
print(test)
ordered = OrderedDict(test)
print(ordered)


for key in ordered:
  print(key)
  print(ordered[key])