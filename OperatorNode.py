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
        self.priority = 0
        
    def getValue(self):
        evaluated = int(self._rightNode.getValue()) + int(self._leftNode.getValue())
        print("AdditionOperator: " + str(evaluated))
        return evaluated
#     def getValue(self):
# #         evaluated = int(self._rightNode.getValue()) + int(self._leftNode.getValue())
# #         print("Right Node val: " + self._rightNode.getValue() + "Left Node val: "+ self._leftNode.getValue())
#         evaluated = "+"
#         return evaluated
 
    
class MultiplicationOperator(IOperatorNode):
    ''' Class for Multiplication operator'''
    def __init__(self, rightNode, leftNode):
        IOperatorNode.__init__(self, rightNode, leftNode)
        self._value = 0
        self.priority = 1
        
    def getValue(self):
        evaluated = int(self._rightNode.getValue()) * int(self._leftNode.getValue())
        print("MultiplicationOperator: " + str(evaluated))
        return evaluated

#     def getValue(self):
#         evaluated = "*"
#         return evaluated
    
class DummyOperator(IOperatorNode):
    ''' Lowest priority "dummy" operator '''
    def __init__(self):
        IOperatorNode.__init__(self, None, None)
        self._value = 0
        self.priority = -1
        
    def getValue(self):
        return self._value
    
class OperatorTypeStorage:
        def __init__(self):
            self.operatorList = ['+', '*']
            self.startBracket = '('
            self.endBracket = ')'