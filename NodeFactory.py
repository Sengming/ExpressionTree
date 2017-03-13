#NodeFactory
from OperatorNode import AdditionOperator, SubtractionOperator, DivisionOperator
from OperatorNode import MultiplicationOperator
from abc import ABC, abstractmethod
from ValueNode import ValueNode
from ValueNode import StartBracketNode

class INodeFactory(ABC):
    '''Interface factory class for us to create mock factory'''
    @abstractmethod
    def makeOperatorNode(self, nodeType, rightNode, leftNode):
        pass
    
    @abstractmethod
    def makeValueNode(self, value):
        pass

class NodeFactory(INodeFactory):
    ''' Factory method pattern to create Nodes'''
    def __init__(self, operatorTypeStorage):
        self.operators = operatorTypeStorage
          
    def makeOperatorNode(self, nodeType, rightNode = None, leftNode = None):
        if nodeType in self.operators.operatorList:
            if nodeType is self.operators.operatorList[0]:
                return AdditionOperator(rightNode, leftNode)
            elif nodeType is self.operators.operatorList[1]:
                return SubtractionOperator(rightNode, leftNode)
            elif nodeType is self.operators.operatorList[2]:
                return MultiplicationOperator(rightNode, leftNode)
            elif nodeType is self.operators.operatorList[3]:
                return DivisionOperator(rightNode, leftNode)
        else:
            raise ValueError('Operator is not contained in the list')           
        # add more nodes here
        
    def makeValueNode(self, value):
        return ValueNode(value)
    
    def makeStartBracketNode(self):
        return StartBracketNode()
        