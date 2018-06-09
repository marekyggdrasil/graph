from tools.tools import *
from tools.output import *

print 'temporarily, as demonstration, it can only derive equation vert3 from vert1'
print ''

edges = ['transition1', 'transition2']
vertices = ['vert1', 'vert2', 'vert3']

parsedv = {}
for v in vertices :
    root = parseFile('vertices/' + v + '.xml')
    parsedv[v] = parseVertex(root)

e1 = parseInferenceRuleEdge(parseFile('edges/transition1.xml'))
e2 = parseSubstitutionEdge(parseFile('edges/transition2.xml'))

displayVertex(parsedv['vert1'])

displayInference(e1)

displayVertex(parsedv['vert2'])

displaySubstitution(e2)

displayVertex(parsedv['vert3'])

print '#\n'
