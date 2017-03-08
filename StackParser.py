# Stack parser
from abc import ABC, abstractmethod
from Stack import Stack
from NodeLinker import NodeLinker
from ValueNode import ValueNode
from OperatorNode import AdditionOperator
from OperatorNode import MultiplicationOperator
from OperatorNode import OperatorTypeStorage

class IStackParser(ABC):
    ''' Handles the parsing of a given stack, allows us to mock out stack parser '''
    
    @abstractmethod
    def parseStack(self, stack):
        pass
    
    
class StackParser(IStackParser):
    ''' The main class used to parse stack given to it by the string parser '''
    
    def __init__(self, linker, operatorList):
        self._linker = linker
        self._operatorList = operatorList
        self._previousOperator = None
        self._currentHead = None

    def parseStack(self, stackToParse):
        previousOperator = None
        currentHead = None
        assembledHead = None
        ''' Handles the linking and parsing of nodes in the stack ''' 
        while stackToParse.isEmpty() is False:
            pass
        
class StackparserMachine():
    ''' Stack parser state machine context '''
    def __init__(self):
        self.
        self._currentState
    

class IStackParserState(ABC):
    ''' Represents the interface class for the stack parser's state machine ''' 
    @abstractmethod
    def executeState(self):
        pass
    
class Parser_initState(IStackParserState):
    ''' Parser's initial state '''
    
    
    
    
    
    
    
    
    