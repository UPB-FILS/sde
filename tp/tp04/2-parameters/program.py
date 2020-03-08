import os
import sys

print ("Command line arguments:")
for index, arg in enumerate(sys.argv):
    print ("  argv[{}]: {}".format(index, arg))
