import re

target='Hello python world'
match=re.match('Hello[ \t]*(.*)world',target)
print match.group(1)

target2='/home/user/paulbuxton'
res2=re.split('[/:]',target2)
folder=res2[-1] # last item in the list (indexing -1)
path='/'.join(res2[:-1]) # everything upto the last item in the list
print '%(folder)s is the folder %(path)s is the path' % vars()
