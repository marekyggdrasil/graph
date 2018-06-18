import unittest

from tools.tools import *
from os import listdir
from os.path import isfile, join

edges = [f for f in listdir('./edges') if isfile(join('./edges', f))]
vertices = [f for f in listdir('./vertices') if isfile(join('./vertices', f))]

inference_apply = []
inference_substitute = []

for edge_filename in edges :
    root = parseFile('edges/' + edge_filename)
    inference_type = root.attrib['type']
    # perform test of inference rule
    if inference_type == 'apply' :
        source, target, operation = parseInferenceRuleEdge(root)
        test_info = source, target, operation, edge_filename
        inference_apply.append(test_info)
    # perform test of substitution
    if inference_type == 'substitution' :
        source, target, substitution, subside, mapping = parseSubstitutionEdge(root)
        test_info = source, target, substitution, subside, mapping, edge_filename
        inference_substitute.append(test_info)

def testParsingFile(self, fullpath) :
    try:
        parseFile(fullpath)
    except :
        self.fail('failed to parse file ' + fullpath)

class GraphTest(unittest.TestCase):
    def testParsing(self) :
        for edge_filename in edges :
            fullpath = 'edges/' + edge_filename
            testParsingFile(self, fullpath)
        for edge_filename in vertices :
            fullpath = 'vertices/' + edge_filename
            testParsingFile(self, fullpath)
    def testApply(self) :
        for test_info in inference_apply :
            source, target, operation, edge_filename = test_info
            # LHS of source is equal to LHS of target after applying inference rule operation?
            LHS = testEquivalency(sympify(target['lhs']), applyOperation(sympify(source['lhs']), sympify(operation)))
            self.assertTrue(LHS, 'LHS is incorrect after applying rule in edges/' + edge_filename)
            # RHS of source is equal to RHS of target after applying inference rule operation?
            RHS = testEquivalency(sympify(target['rhs']), applyOperation(sympify(source['rhs']), sympify(operation)))
            self.assertTrue(RHS, 'RHS is incorrect after applying rule in edges/' + edge_filename)
    def testSubstitute(self) :
        for test_info in inference_substitute :
            source, target, substitution, subside, mapping, edge_filename = test_info
            # LHS of source is equal to LHS of target?
            LHS = testEquivalency(applySubstitution(sympify(source['lhs']), substitution, subside, mapping), sympify(target['lhs']))
            self.assertTrue(LHS, 'LHS is incorrect after applying rule in edges/' + edge_filename)
            # RHS of source is equal to RHS of target?
            RHS = testEquivalency(applySubstitution(sympify(source['rhs']), substitution, subside, mapping), sympify(target['rhs']))
            self.assertTrue(RHS, 'RHS is incorrect after applying rule in edges/' + edge_filename)
