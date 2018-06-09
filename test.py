from tools.tools import *

from lxml import etree
from os import listdir
from os.path import isfile, join

path = 'edges'
edges = [f for f in listdir(path) if isfile(join(path, f))]

for edge_filename in edges :
    print '* parsing edge ' + edge_filename + '...',
    root = parseFile('edges/' + edge_filename)
    print ' OK'
    inference_type = root.attrib['type']
    # perform test of inference rule
    if inference_type == 'apply' :
        source, target, operation = parseInferenceRuleEdge(root)
        # LHS of source is equal to LHS of target after applying inference rule operation?
        print '  LHS after inference rule...',
        assert testEquivalency(sympify(target['lhs']), applyOperation(sympify(source['lhs']), sympify(operation)))
        print ' OK'
        # RHS of source is equal to RHS of target after applying inference rule operation?
        print '  RHS after inference rule...',
        assert testEquivalency(sympify(target['rhs']), applyOperation(sympify(source['rhs']), sympify(operation)))
        print ' OK'
    # perform test of substitution
    if inference_type == 'substitution' :
        source, target, substitution, subside, mapping = parseSubstitutionEdge(root)
        # LHS of source is equal to LHS of target?
        print '  LHS after inference rule...',
        assert testEquivalency(applySubstitution(sympify(source['lhs']), substitution, subside, mapping), sympify(target['lhs']))
        print ' OK'
        # RHS of source is equal to RHS of target?
        print '  RHS after inference rule...',
        assert testEquivalency(applySubstitution(sympify(source['rhs']), substitution, subside, mapping), sympify(target['rhs']))
        print ' OK'
