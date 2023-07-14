#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# counter: library for check_csv

dictall = {}  # dictionary for count all the keywords
dict = {}     # dictionary for count primary keyword


def addkey(key):
    # add a keyword as a primary category
    if (key not in dict):
        dict[key] = 1
    else:
        dict[key] += 1


def addallkeys(key):
    # add a keyword into dictall
    if (key not in dictall):
        dictall[key] = 1
    else:
        dictall[key] += 1


def printkeys():
    total = 0
    sdict = sorted(dict.items())   # sort dict
    for key, num in list(sdict):
        print("%s %s" % (key, num))
        total = total + num
    print("Total primary categories: %s" % total)
    print("---")

    tall = 0
    sdictall = sorted(dictall.items())  # sort dict
    for key, num in list(sdictall):
        print("%s %s" % (key, num))
        tall = tall + num
    print("Total categories used: %s" % tall)       
