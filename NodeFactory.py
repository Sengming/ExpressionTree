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
             
    def makeOperatorNode(self, nodeType, rightNode, leftNode):       
        if nodeType is "+":
            return AdditionOperator(rightNode, leftNode)
        elif nodeType is "*":
            return MultiplicationOperator(rightNode, leftNode)
        # add more nodes here
        
    def makeValueNode(self, value):
        return ValueNode(value)
        