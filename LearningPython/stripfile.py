
"""
File stripper
"""




def stripfile(filename):
    """
    Sample to demonstrate fileio with list comprehensions
    strips lines starting with # and empty lines
    note that compound if statement uses & rather than &&
    """
    stripped = [line.rstrip() for line in open(filename) if (line[0] != '#') \
        & (line[0] != '\n')]
    for line in stripped:
        print line

stripfile('/home/paulbuxton/history.txt')
