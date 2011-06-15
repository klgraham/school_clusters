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
    
    def __init__(self,name,demographics):
        self.name = name

        # demographics holds racial and ethnic %s as a dictionary
        # {white, black, latino, asian, pacific islander, native am, FRPL}
        self.demographics = demographics
#        self.test_scores = test_scores
#        self.ayp = ayp # school performance variables (numeric)

        data = self.demographics.values()
        self.data = tuple(data)

    def print_school(self):
        print self.name,self.data

#        if (self.demographics != None):
#            for r in self.demographics:
#                print ', %s: %f' % (r, self.demographics[r]),
#            print ''

#        if (self.test_scores != None):
#            for r in self.test_scores:
#                print ', %s: %f' % (r, self.test_scores),
#            print ''

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
#    race = {
#        'white': .75,
#        'black': .10,
#        'latino': .10,
#        'asian': .02,
#        'pac_isle': .02,
#        'native': .01,
#        'frpl': .67
#    }

    def race():
      d = {
            'white': random(),
            'black': random(),
            'latino': random(),
            'asian': random(),
            'pac_isle': random(),
            'native': random(),
            'frpl': random()
      }
      return d

    schools = []
    for i in range(30):
        schools.append(School(name,race()))

#    s = School(name,race)
#    s.print_school()

#    s1 = School(name+name,race)
#    s1.print_school()
    
#    schools = [s,s1,s,s1]
    data = build_data_array(schools)
    (clusterid, error, nfound) = kcluster(data,nclusters=3,npass=3,dist='b')
    print clusterid, nfound

