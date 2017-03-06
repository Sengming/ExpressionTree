#Node
from abc import ABC, abstractmethod

class INode(ABC):
    '''Node interface that operator nodes and value nodes inherit from'''
    
    @abstractmethod
    def getValue(self):
        pass
    