#OperatorClass
from INode import INode
from abc import ABC

class IOperatorNode(INode, ABC):
    ''' Abstract Class for different operators. '''
    def __init__(self, rightNode, leftNode):
        self._rightNode = rightNode
        self._leftNode = leftNode
    
    def getLeftNode(self):
        return self._leftNode
    
    def setLeftNode(self, newLeftNode):
        self._leftNode = newLeftNode
    
    def getRightNode(self):
        return self._rightNode
    
    def setRightNode(self, newRightNode):
        self._rightNode = newRightNode
        
        
class AdditionOperator(IOperatorNode):
    ''' Class for addition operator'''
    def __init__(self, rightNode, leftNode):
        IOperatorNode.__init__(self, rightNode, leftNode)
        self._value = 0
        
    def getValue(self):
        evaluated = self._leftNode.getValue() + self._rightNode.getValue()
        return evaluated
 
    
class MultiplicationOperator(IOperatorNode):
    ''' Class for Multiplication operator'''
    def __init__(self, rightNode, leftNode):
        IOperatorNode.__init__(self, rightNode, leftNode)
        self._value = 0
        
    def getValue(self):
        evaluated = self._leftNode.getValue() * self._rightNode.getValue()
        return evaluated
    
    