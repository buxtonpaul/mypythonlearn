# -*- coding: utf-8 -*-
"""
Given an input file containing perforce changelists, sorts them chronologically and creates an outputfile of the files changed for use byt the p4-gource script
"""
import re
import os
import  optparse
import sys



usage = "usage: %s [options] FILE" % sys.argv[0]
parser = optparse.OptionParser(usage=usage)
parser.add_option("-o", "--out-file", dest="out", help="output filename, defaults to FILE.gource")
(options, args) = parser.parse_args()
if 1 != len(args):
    parser.error("one FILE argument required")
input = args[0]
if not options.out:
    options.out = input + "_diff.log"
output = options.out


p4_entry = re.compile("^Change (?P<changelist>\d+).*")

changeslists=[]

file= open(input)
for line in file:
    print line
    change=p4_entry.match(line)
    if change:
        print change.group("changelist")
        changeslists.append(int(change.group("changelist")))

print changeslists

changeslists.sort()

outfile=output
print changeslists
for change in changeslists:
    execstring="p4 describe -s {} >>{}".format(change,outfile)    
    os.system(execstring)
    #print(execstring)