#!/usr/bin/env python

from pyspark import SparkContext

def main():
    sc = SparkContext(appName='SparkWordCount')

    input_file = sc.textFile('/user/guan/test.txt')
    counts = input_file.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

    counts.saveAsTextFile('/user/guan/test_output')

    sc.stop()

if __name__ == '__main__':
    main()
