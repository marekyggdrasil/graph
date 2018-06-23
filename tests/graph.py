from unittest import TestCase
from paramunittest import parametrized

from tools.tools import parseFile, listDirectory, parseFile
from os import listdir
from os.path import isfile, join

edges = listDirectory('./edges')
vertices = listDirectory('./vertices')

files = []
for edge in edges :
    files.append({'filename': edge, 'component': 'edge', 'directory': 'edges'})
for vertex in vertices :
    files.append({'filename': vertex, 'component': 'vertex', 'directory': 'vertices'})

files = tuple(files)

@parametrized(*files)
class GraphTestParsingEdges(TestCase):
    def testComplete(self) :
        path = self.directory + '/' + self.filename
        try:
            parsed = parseFile(path)
        except Exception as error :
            self.fail('failed to parse '+ self.directory +'/' + self.filename + ': ' + str(error))
    def setParameters(self, filename, component, directory):
        self.filename = filename
        self.type = component
        self.directory = directory
