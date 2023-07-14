#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# check techarea strings in csv file for the nomination
# usage: check_techarea -c -f csv-filename

import csv
from counter import addallkeys, addkey, printkeys

TechArea_categories = [
    "automotive",
    "base operating system",
    "block chain",
    "cloud computing",
    "common packages",
    "configuration management",
    "deep learning",
    "desktop",
    "embedded",
    "enterprise computing",
    "hardware development",
    "mobile",
    "networking",
    "security",
    "software development",
    "storage",
    "web"
]


def check_format(nominated, type, comments):
    # check the nomination format. this can be ommitted by -f
    message = ""
    if (nominated != "OIN"):
        message = "Wrong nominator: %s " % nominated
    if (type != "CLEANUP"):
        message += "Wrong nomination type: %s " % type
    if (comments != "Update TechArea"):
        message += "Wrong comments: %s " % comments
    if (message != ""):
        message = message + "\n"
    return message


def check_duplicate(string):
    # check string contains dupulicated words
    return len(string) != len(set(string))


def check_techarea(techarea):
    # check contains of TechArea strings,
    # return '' if no error, return error message if anything wrong

    talist = str(techarea).split(',')
    message = ''
    if (len(talist) > 0):
        addkey(talist[0])   # add primary keyword
    else:
        print("*** No techarea string: %s", techarea)
    for s in talist:
        if not(s in TechArea_categories):    # check techarea string
            message = message + "Category string error: '%s'\n" % (s)
        else:
            addallkeys(s)  # add all the keywords
    if (check_duplicate(talist)):
        message = message + "duplicated category string: %s\n" % techarea
    return message


def main(csvfile, format_check, techarea_check):
    # main processing
    with open(csvfile, 'r') as csvf:
        reader = csv.DictReader(csvf)
        linecount = 1
        error_count = 0
        for row in reader:
            name = row['Package Name']
            if not name:
                continue  # ignore if no name
            linecount += 1
            #print("Name: ", name)
            if (format_check):  # should check format
                formatmsg = check_format(
                    row['Nominated By...'], row['Nomination type'],
                    row['Nominator comments'])
                if (formatmsg != ''):
                    error_count += 1
                    print(name, ": ", formatmsg, end="")
            ta = row['TechArea']
            msg = check_techarea(ta)
            if (msg != ''):
                print(name, ": ",  msg, end="")
                error_count += 1

        if (error_count == 0):
            print("No error for TechArea in %s lines." %
                  linecount)
            printkeys()   # print keywords
        else:
            print("%s errors for TechArea in %s lines" %
                  (error_count, linecount))


def parsearg():
    # command [-f] [-c] csvfilename
    #  -f : check format of nomination
    #  -c : check spelling of techarea, always on
    import argparse
    parser = argparse.ArgumentParser(prog='check_techarea')
    parser.add_argument("csvfile", help="csv filename")
    parser.add_argument("-f", "--check_format", action='store_true')
    parser.add_argument("-c", "--check_techarea", action='store_true')
    args = parser.parse_args()
    return args


if __name__ == "__main__":

    args = parsearg()
    main(args.csvfile, args.check_format, args.check_techarea)
    exit(0)
