import unittest

from tools.ContentMathML import mml2sympy

from lxml import etree
from sympy import sympify

def testParsingSympifying(self, xml, msg) :
    mml = None
    try :
        mml = mml2sympy(etree.XML(xml))
    except :
        self.fail('failed to parse ' + msg)
    try :
        sympify(mml)
    except :
        self.fail('failed to sympify ' + msg)

class ParsingTest(unittest.TestCase):
    def testAddition(self):
        xml = """
        <apply>
            <plus/>
            <ci>E</ci>
            <ci>D</ci>
        </apply>
        """
        testParsingSympifying(self, xml, 'addition')
    def testSubtraction(self):
        xml = """
        <apply>
            <minus/>
            <ci>E</ci>
            <ci>D</ci>
        </apply>
        """
        testParsingSympifying(self, xml, 'subtraction')
    def testMultiplication(self):
        xml = """
        <apply>
            <times/>
            <ci>E</ci>
            <ci>D</ci>
        </apply>
        """
        testParsingSympifying(self, xml, 'multiplication')
