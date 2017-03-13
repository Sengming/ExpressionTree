# Parse strings
from OperatorNode import OperatorTypeStorage
from NodeLinker import INodeLinker
from NodeLinker import NodeLinker
from NodeFactory import INodeFactory
from NodeFactory import NodeFactory
from Stack import Stack
from StackParser import StackParser
from ValueNode import ValueNode
from ValueNode import StartBracketNode

class StringParser:
    ''' Parses a given string, takes a nodelinker interface'''
    def __init__(self, iNodeFactory, iStackParser, bracketStack, mainStack, opList):
        self._factory = iNodeFactory
        self._parser  = iStackParser
        self._bracketStack = bracketStack
        self._mainStack = mainStack
        self._currentNode = None
        self._previousOperator = None
        self._opStorage = opList
        
    def parseString(self, stringToParse):
        ''' Main method used to populate the stack with Node objects ''' 
        retVal = None       
        for symbol in stringToParse:
            if self.is_endBracket(symbol) is False:
                if self.is_operator(symbol) is True:
                    self.parseOperator(symbol)
                    print("parsing operator")
                elif self.is_number(symbol) is True:
                    self.parseValue(symbol)
                    print("parsing value")
                elif self.is_startBracket(symbol) is True:
                    self.parseStartBracket()
            elif self.is_endBracket(symbol) is True:
                evaluatedBracketNode = self.parseEndBracket()
                evaluatedBracketNode.priority = 99
                retVal = self._mainStack.push(evaluatedBracketNode)
        
        if self._mainStack.isEmpty() is False:
            print("parsing whole stack now")
            retVal = self.parseEntireStack()
        return retVal
              
    def parseOperator(self, operator):
        ''' Uses the factory to create new node and add to the main stack '''
        tempOpNode = self._factory.makeOperatorNode(operator)
        self._mainStack.push(tempOpNode)
#         tempOperatorNode = self._factory.makeOperatorNode()
#         
#         if self._previousOperator.order > tempOperatorNode.order:
#             self._linker.appendCurrentOperatorHead(self._previousOperator, tempOperatorNode)
#         elif self._previousOperator.order < tempOperatorNode.order:
#             self._linker.appendCurrentOperatorRight(self._previousOperator, tempOperatorNode)
#             
#     
    def parseValue(self, value):
        ''' Uses the factory to create a new node and add to the main stack '''
        tempValNode = self._factory.makeValueNode(value)
        self._mainStack.push(tempValNode)
#         self._currentNode = self._factory.makeValueNode(value)
#     
    def parseEndBracket(self):
        ''' If we hit an end bracket, pop the stack until the first start-bracket hit, and send to parser for evaluation '''
        print("parsing and handling end bracket")
        # Clear the bracket stack before sending
        self._bracketStack.emptyStack()
        mainStackVal = self._mainStack.pop()
        
        while type(mainStackVal) is not StartBracketNode and self._mainStack.isEmpty() is False:
            self._bracketStack.push(mainStackVal)
            mainStackVal = self._mainStack.pop()
        
        # Stack comes out in the wrong order
        self._bracketStack.reverse()
        
#         self._bracketStack.printWholeStack()
        
        # Return the evaluated stack. This should be a node.
        return self._parser.parseStack(self._bracketStack)

    def parseStartBracket(self):
        tempBracketNode = self._factory.makeStartBracketNode()
        self._mainStack.push(tempBracketNode)
    
    def parseEntireStack(self):
        ''' After evaluating everything, parse the entire stack, assuming there are no longer any brackets within it '''
        return self._parser.parseStack(self._mainStack)
#     def parseStartBracket(self):
#         pass
#     
#     def popAndEvalStack(self):
#         value = self._bracketStack.pop()
#         
#         while self.is_startBracket(value) is False and self.stack.isEmpty() is False:
#             if self.is_number(value) is True:
#                 self.parseValue(value)
#             elif self.is_operator(value) is True:
#                 self.parseOperator(value)
#                 
#             value = self._bracketStack.pop()
#         
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
            