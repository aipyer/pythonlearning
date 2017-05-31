"""
找出整个目录树中最大的Python源代码文件
"""

import os, sys, pprint
trace = Falseif
if sys.platform.startswith('linux'):
  dirname = './'
else:
  dirname = r'C:\Python31\Lib'

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
  if trace:print(thisDir)
  for filename in filesHere:
    if filename.endswith('.py'):
      if trace:print('...', filename)
      fullname = os.path.join(thisDir, filename)
      fullsize = os.path.getsize(fullname)
      allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])