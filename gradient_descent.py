#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:52:52 2017

@author: abhishek
"""

import os
os.chdir('/home/abhishek/Desktop/andrewng')

import numpy
import pandas as pd
import pickle
import logging
import io



originaldata = pd.read_csv(io.open('ashina.csv'), 'r')