#!/usr/bin/env python
# encoding: utf-8

'''
The objective is to see how schools form clusters, according to various characteristics, such as demographics, test scores, ayp, grad rate, etc, and locale

Author: Ken Graham

Copyright (c) 2011, Ken Graham
All rights reserved.
'''

from Pycluster import *
import school_clusters as SC
import csv
import string

filename = 'high-priority.csv'

def main():

    schooldata = csv.reader(open(filename),delimiter=',')
#    locales = csv.reader(open('tn_locale_codes.csv'), delimiter=",")
    
    schools = []
    for row in schooldata:
        schools.append(SC.School(row))
    
#    locale_code = {}
#    for row in locales:
#        locale_code[row[1]] = row[0]
            
    school_data = SC.build_data_array(schools)
#    (clusterid, error, nfound) = kcluster(school_data,nclusters=3,npass=3,dist='b')
    (clusterid, error, nfound) = kcluster(school_data,nclusters=5,npass=10,dist='b')
    print clusterid, nfound
                
if __name__ == '__main__':

    main()
