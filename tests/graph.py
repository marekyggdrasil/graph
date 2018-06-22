import unittest

from tools.tools import parseFile, listDirectory, parseFile
from os import listdir
from os.path import isfile, join

edges = listDirectory('./edges')
vertices = listDirectory('./vertices')

for edge in edges :
    class GraphTest(unittest.TestCase):
        def testComplete(self) :
            path = 'edges/' + edge
            try:
                parsed = parseFile(path)
            except Exception as error :
                self.fail('failed to parse edges/' + edge + ': ' + str(error))
