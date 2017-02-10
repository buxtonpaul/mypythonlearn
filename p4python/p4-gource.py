#! /usr/bin/python

# p4-gource.py - perforce to gource change log converter
# Copyright (C) 2010 Maxim Yegorushkin <maxim.yegorushkin@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# usage:
# $ head=`p4 changes -m 1 | awk '{ print $2 }'`
# $ for ((i = 1; i <= $head; ++i)); do p4 describe -s $i >> p4.log; done
# $ ./p4-gource.py -p //depot/trunk -o trunk.gource p4.log
# $ gource --highlight-all-users trunk.gource

from __future__ import print_function
import os, sys, re, time, optparse

usage = "usage: %s [options] FILE" % sys.argv[0]
parser = optparse.OptionParser(usage=usage)
parser.add_option("-o", "--out-file", dest="out", help="output filename, defaults to FILE.gource")
parser.add_option("-p", "--path-filter", dest="filter", default="//", help="include only paths starting with FILTER")
(options, args) = parser.parse_args()
if 1 != len(args):
    parser.error("one FILE argument required")
input = args[0]
if not options.out:
    options.out = input + ".gource"
output = options.out

p4_entry = re.compile("^Change \d+ by (?P<author>[a-zA-Z0-9_\.]+)@\S+ on (?P<timestamp>\S+ \S+)\s*$")
p4_affected_files = re.compile("^Affected files ...\s*$")
p4_file = re.compile("^... (?P<file>%s[^#]+)#\d+ (?P<action>\w+)\s*$" % options.filter)

p4_action_to_gource = {
      "add" : "A"
    , "edit" : "M"
    , "integrate" : "M"
    , "branch" : "A"
    , "delete" : "D"
    , "purge" : "D"
}

def p4_to_gource(p4_log, gource_log):
    author = None
    timestamp = None
    files = False
    for line in p4_log:
        entry = p4_entry.match(line)
        if entry:
            author = entry.group("author")
            timestamp = int(time.mktime(time.strptime(entry.group("timestamp"), "%Y/%m/%d %H:%M:%S")))
            files = False
            continue
        if not files:
            if p4_affected_files.match(line):
                files = True
        else:
            file = p4_file.match(line)
            if file:
                print("%d|%s|%s|%s|" % (
                          timestamp
                        , author
                        , p4_action_to_gource[file.group("action")]
                        , file.group("file")
                      ), file=gource_log)

p4_to_gource(open(input, "r"), open(output, "w"))

