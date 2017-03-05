#NodeFactory
from OperatorNode import OperatorNode

class NodeFactory:
    ''' Factory method pattern to create Nodes'''
    #def __init__(self):
        
        
    def makeOperatorNode(self, nodeType):
        
        if nodeType is "PLUS":
            return OperatorNode()
        