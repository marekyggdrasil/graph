from sympy import sympify

def strs(a) :
    return str(sympify(a))

def displayVertex(v) :
    print strs(v['lhs']) + ' = ' + strs(v['rhs']) + '\n'

def displayInference(e) :
    _, _, o = e
    print 'apply ' + strs(o) + ' to both sides of equation\n'

def displaySubstitution(e) :
    _, _, s, subside, mapping = e
    print 'substitute with ' + subside + ' of ' + strs(s['lhs']) + ' = ' + strs(s['rhs']) + ', map values as ' + str(mapping) + '\n'
