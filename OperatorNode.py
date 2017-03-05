#OperatorClass
from INode import INode

class OperatorNode(INode):
    ''' Class for different operators. '''
    def __init__(self, rightNode, leftNode):
        self._rightNode = rightNode
        self._leftNode = leftNode
        
    def getValue(self):
        pass
    
    def getLeftNode(self):
        return self._leftNode
    
    def setLeftNode(self, newLeftNode):
        self._leftNode = newLeftNode
    
    def getRightNode(self):
        return self._rightNode
    
    def setRightNode(self, newRightNode):
        self._rightNode = newRightNode