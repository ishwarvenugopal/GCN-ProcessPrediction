#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 07:45:19 2020

@author: jessica
"""

import pickle


with open('helpdesk.pkl', 'rb') as f:
    data = pickle.load(f)
    
print(data)    