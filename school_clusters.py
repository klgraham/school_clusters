#!/usr/bin/env python
# encoding: utf-8

# description of a school and its characteristics

"""
school_clusters.py

Created by Ken Graham on 15 June 2011
Copyright (c) 2011, Ken Graham.
All rights reserved.
"""

import numpy
from Pycluster import *
from random import random

class School(object):
    
    def __init__(self,data):
	self.name = data[2]
        self.data = tuple(data[4:-4])

    def print_school(self):
        print self.name,self.data

    def get_data(self):
        return self.data

def build_data_array(schools):
    d = []
    for s in schools:
          d.append(s.get_data())
    return numpy.array(d)

# k-means clustering algorithm
# optional parameters
# distance measure possibilities, dist = :
# 'a' = abs value of correlation
# 'b' = manhattan
# 'c' = correlation
# 'k' = kendall's tau
# 'e' = euclidean
# kcluster (data, nclusters=2, mask=None, weight=None, transpose=0, npass=1, method=’a’, dist=’e’, initialid=None)

if __name__ == '__main__':
    name = 'Central High'

    def race():
        d = ['asdfa','adfa',name,'adsf',1000*random(),random(),random(),random(),random(),random(),random(),random()]

        return d

    schools = []
    for i in range(10):
        schools.append(School(race()))

    data = build_data_array(schools)
    (clusterid, error, nfound) = kcluster(data,nclusters=3,npass=3,dist='b')
    print clusterid, nfound
   
