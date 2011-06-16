#!/usr/bin/env python
# encoding: utf-8

'''
This file lets you cluster a list of schools accordining to their data.
Any school-level data can be used. Demographics, test scores, grad rates, 
NCLB/AYP performance, etc.

Author: Ken Graham

Copyright (c) 2011, Ken Graham
All rights reserved.
'''

from Pycluster import kcluster
import school_clusters as SC
import csv

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
