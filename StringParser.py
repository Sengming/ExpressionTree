# Parse strings
from OperatorNode import OperatorTypeStorage
from NodeLinker import INodeLinker
from NodeLinker import NodeLinker
from NodeFactory import INodeFactory
from NodeFactory import NodeFactory
from Stack import Stack
from ValueNode import ValueNode
import OperatorNode

class StringParser:
    ''' Parses a given string, takes a nodelinker interface'''
    def __init__(self, iNodeLinker, iNodeFactory, opStorage, stack):
        self._linker = iNodeLinker
        self._factory = iNodeFactory
        self._opStorage = opStorage
        self._stack = stack
        self._currentNode = None
        self._previousOperator = None
        
    def parseString(self, stringToParse):
        ''' Parses the tree and links it together '''        
        for symbol in stringToParse:
            if self.is_endBracket(symbol) is False:
                self._stack.push(symbol)
#             elif self.is_operator(symbol) is True:
#                 self.parseOperator(symbol)
#             elif self.is_startBracket(symbol) is True:
#                 self.parseStartBracket()
            elif self.is_endBracket(symbol) is True:
                self.parseEndBracket()
        
        if self._stack.isEmpty() is False:
            self.popAndEvalStack()
             
             
    def parseOperator(self, operator):
        tempOperatorNode = self._factory.makeOperatorNode()
        
        if self._previousOperator.order > tempOperatorNode.order:
            self._linker.appendCurrentOperatorHead(self._previousOperator, tempOperatorNode)
        elif self._previousOperator.order < tempOperatorNode.order:
            self._linker.appendCurrentOperatorRight(self._previousOperator, tempOperatorNode)
            
    
    def parseValue(self, value):
        self._currentNode = self._factory.makeValueNode(value)
    
    def parseEndBracket(self):
        self._previousOperator = None
        self.popAndEvalStack()
        pass
    
    def parseStartBracket(self):
        pass
    
    def popAndEvalStack(self):
        value = self._stack.pop()
        
        while self.is_startBracket(value) is False and self.stack.isEmpty() is False:
            if self.is_number(value) is True:
                self.parseValue(value)
            elif self.is_operator(value) is True:
                self.parseOperator(value)
                
            value = self._stack.pop()
        
    def is_number(self, symbol):
        try:
            int(symbol)
            return True
        except ValueError:
            return False
        
    def is_operator(self, symbol):
        if symbol in self._opStorage.operatorList:
            return True
        else:
            return False
            
    def is_startBracket(self, symbol):
        if symbol is self._opStorage.startBracket:
            return True
        else:
            return False
        
    def is_endBracket(self, symbol):
        if symbol is self._opStorage.endBracket:
            return True
        else:
            return False
            