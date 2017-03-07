#NodeFactory
from OperatorNode import AdditionOperator
from OperatorNode import MultiplicationOperator
from abc import ABC, abstractmethod
from ValueNode import ValueNode

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
          
    def makeOperatorNode(self, nodeType, rightNode, leftNode):
        if nodeType in self.operators.operatorList:
            if nodeType is self.operators.operatorList[0]:
                return AdditionOperator(rightNode, leftNode)
            elif nodeType is self.operators.operatorList[1]:
                return MultiplicationOperator(rightNode, leftNode)
        else:
            raise ValueError('Operator is not contained in the list')           
        # add more nodes here
        
    def makeValueNode(self, value):
        return ValueNode(value)
        