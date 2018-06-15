# !/usr/bin/python
# -*- coding=utf-8 -*-
from numpy import *


def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return dataMat


def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


def ranCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    # 构建簇质心
    for j in range(n):
        minJ = min(dataSet[:, j])
        rangeJ = float(max(dataSet[:, j]) - minJ)
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
    return centroids


if __name__ == "__main__":
    datMat = mat(loadDataSet('testSet.txt'))
    print min(datMat[:, 0])
    print min(datMat[:, 1])
    print max(datMat[:, 0])
    print max(datMat[:, 1])
    print ranCent(datMat, 2)
    print distEclud(datMat[0], datMat[1])
