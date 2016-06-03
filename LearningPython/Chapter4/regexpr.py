"""
DOCString goes here
"""
import re

TARGET = 'Hello python world'
MATCH = re.match('Hello[ \t]*(.*)world', TARGET)
print MATCH.group(1)

TARGET2 = '/home/user/paulbuxton'
RES2 = re.split('[/:]', TARGET2)
FOLDER = RES2[-1]  # last item in the list (indexing -1)
PATH = '/'.join(RES2[:-1])  # everything upto the last item in the list
# example using the template substitution to print variables
print '%(folder)s is the folder %(path)s is the path' % vars()
