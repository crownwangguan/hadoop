#!/usr/bin/python

import sys

salesValue = 0
salesCount = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    thisItem, thisSale = data_mapped

    salesValue += float(thisSale)
    salesCount += 1

print salesValue, "\t", salesCount