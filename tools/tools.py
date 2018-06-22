from ContentMathML import mml2sympy

from lxml import etree
from sympy import Symbol, simplify, sympify, simplify

from os import listdir
from os.path import isfile, join

def listDirectory(path) :
    return [f for f in listdir(path) if isfile(join(path, f))]

def parseFile(path) :
    with open(path, 'r') as file :
        xml = file.read()
        return etree.XML(xml)

def parseVertex(root) :
    res = {}
    for child in root :
        res[child.tag] = mml2sympy(child[0][0])
    return res

def mapKeyValue(root) :
    res = {}
    for child in root :
        key = None
        value = None
        for child2 in child :
            if child2.tag == 'from' : key = child2.text
            if child2.tag == 'to' : value = child2.text
        res[key] = value
    return res

def applyOperation(expr, operation) :
    return simplify(operation.subs(Symbol('eq'), expr))

def remapSymbols(expr, mapping) :
    for key in mapping.keys() :
        expr = expr.subs(Symbol(key), Symbol(mapping[key]))
    return simplify(expr)

def applySubstitution(expr, substitution, subside, mapping) :
    # remap symbols in substituted expression according to the mapping
    lhs = remapSymbols(sympify(substitution['lhs']), mapping)
    rhs = remapSymbols(sympify(substitution['rhs']), mapping)
    # substitute according to the side
    if subside == 'lhs' : return simplify(expr.subs(lhs, rhs))
    return simplify(expr.subs(rhs, lhs))

def testEquivalency(expr1, expr2) :
    return simplify(expr1 - expr2) == 0

def parseInferenceRuleEdge(root) :
    source = None
    target = None
    operation = None
    for child in root :
        if child.tag == 'source' :
            source = parseVertex(parseFile('vertices/' + child.text + '.xml'))
        if child.tag == 'target' :
            target = parseVertex(parseFile('vertices/' + child.text + '.xml'))
        if child.tag == 'apply' :
            operation = mml2sympy(child[0][0])
    return source, target, operation

def parseSubstitutionEdge(root) :
    source = None
    target = None
    substitution = None
    mapping = None
    subside = None
    for child in root :
        if child.tag == 'source' :
            source = parseVertex(parseFile('vertices/' + child.text + '.xml'))
        if child.tag == 'target' :
            target = parseVertex(parseFile('vertices/' + child.text + '.xml'))
        if child.tag == 'substitution' :
            subroot = child
            subfile = subroot.attrib['of']
            subside = subroot.attrib['side']
            subvertex = parseFile('vertices/' + subfile + '.xml')
            substitution = parseVertex(subvertex)
            for subchild in subroot :
                if subchild.tag == 'map' :
                    mapping = mapKeyValue(subchild)
    return source, target, substitution, subside, mapping
