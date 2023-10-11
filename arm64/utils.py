"""
utils.py

General functions to analyse simulation data
"""
import json
import pickle
import numpy as np
from pylab import *
from itertools import product

from pprint import pprint
from netpyne import specs

def readBatchData(dataFolder, batchLabel, loadAll=False, saveAll=True, vars=None, maxCombs=None, listCombs=None):
    if loadAll:
        filename =
