#NodeLinker
from abc import ABC, abstractmethod
from ValueNode import ValueNode

class INodeLinker(ABC):
    ''' Interface class to enforce node linker's methods. This allows us to mock out the nodelinker.''' 
    
    @abstractmethod
    def appendCurrentOperatorHead(self, currentOpNode, newHead):
        pass

    @abstractmethod
    def appendCurrentOperatorRight(self, currentOpNode, newRight):
        pass

class NodeLinker(ABC):
    ''' Nodelinker to link together nodes. Cooperates with factory'''
    
    def __init__(self):
        self._currentNode = ValueNode()
    
    def appendCurrentOperatorHead(self, currentOpNode = ValueNode(), newHead):
        temp = newHead.getLeftNode()
        currentOpNode.setLeftNode(temp)
        newHead.setLeftNode(currentOpNode)
        return newHead
        
    def appendCurrentOperatorRight(self, currentOpNode, newRight):
        temp = currentOpNode.getRightNode()
        currentOpNode.setRightNode(newRight)
        newRight.setLeftNode(temp)
        return currentOpNode