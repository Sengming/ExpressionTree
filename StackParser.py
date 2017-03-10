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
    
    def __init__(self, operatorList, stateList):
        self._operatorList = operatorList
        self._previousOperator = None
        self._currentHead = None
        # Initializing state machine with injected state list. We don't need to inject the state machine. They're tightly coupled
        self._stateMachine = StackParserMachine(stateList)

    def parseStack(self, stackToParse):
        self._stateMachine.resetStateMachine()
        self._stateMachine.setStack(stackToParse)
#         stackToParse.printWholeStack()
        
        ''' Handles the linking and parsing of nodes in the stack ''' 
        while True:
            retVal = self._stateMachine.executeCurrentState()
            if self._stateMachine.checkExitCondition() is True:
                self._stateMachine.resetStateMachine()
                break
            else:
                self._stateMachine.moveToNextState()
        
        return retVal
    
class StackParserMachine():
    ''' Stack parser state machine context. Accepts a list of states. Construction logic is separate'''
    def __init__(self, stateList):
        self._stateList = stateList
        self._currentState = self._stateList[0]
        self._stack = None
        
    def getCurrentState(self):
        return self._currentState

    def resetStateMachine(self):
        self._currentState = self._stateList[0]
        self._stack = None
        
    def setNextState(self, stateNumber):
        self._currentState.setNextState(self._stateList[stateNumber])
        
    def executeCurrentState(self):
        return self._currentState.executeState(self._stack)
    
    def checkExitCondition(self):
        return self._currentState.checkExitCondition()
    
    def moveToNextState(self):
        self._currentState = self._currentState.getNextState()
        
    def setStack(self, stack):
        self._stack = stack
    
class IStackParserState(ABC):
    ''' Represents the interface class for the stack parser's state machine ''' 
    @abstractmethod
    def executeState(self, stack):
        pass
    
    @abstractmethod
    def passArgsForward(self):
        pass
    
    @abstractmethod
    def checkExitCondition(self):
        pass
    
    @abstractmethod
    def setArgList(self, arglist):
        pass
        
    @abstractmethod
    def getNextState(self):
        pass
    
    @abstractmethod
    def setNextState(self, state):
        pass
    
class Parser_idleState(IStackParserState):
    ''' Parser's idle state '''
    def __init__(self, nextState = None):
        self._nextState = nextState
        self._argList = ParserArgs()
    
    def executeState(self, stack):
        print("Parser_IdleState")
        self._argList.currentHead = None
        self._argList.previousOp = None
        self._argList.tempOp = None
        self.passArgsForward()
    
    def passArgsForward(self):
        self._nextState.setArgList(self._argList)

    def setArgList(self, arglist):
        self._argList = arglist
    
    def getNextState(self):
        return self._nextState
    
    def setNextState(self, state):
        self._nextState = state
        
    def checkExitCondition(self):
        return False
    
class Parser_initialElementState(IStackParserState):
    ''' Parser's state where it makes single element'''
    def __init__(self, nextState = None):
        self._nextState = nextState
        self._argList = None
        
    def executeState(self, stack):
        print("Parser_InitialElementState")
        self._argList.currentHead = stack.pop()
        print(self._argList.currentHead.getValue())
        self.passArgsForward()
        return None
    
    def passArgsForward(self):
        self._nextState.setArgList(self._argList)
    
    def setArgList(self, arglist):
        self._argList = arglist
    
    def getNextState(self):
        return self._nextState
    
    def setNextState(self, state):
        self._nextState = state
        
    def checkExitCondition(self):
        return False
    
class Parser_makePairState(IStackParserState):
    ''' We make a temp pair of elements to add to main tree'''
    def __init__(self, nextState = None):
        self._nextState = nextState
        self._argList = None
               
    def executeState(self, stack):
        print("Parser_makePairState")
        opNode = stack.pop()
        valNode = stack.pop()
        opNode.setRightNode(valNode)
#         print("MakePairstate currenthead value: " + self._argList.currentHead.getValue())
        self._argList.tempOp = opNode
        self.passArgsForward()
        return None
    
    def passArgsForward(self):
        self._nextState.setArgList(self._argList)

    def setArgList(self, arglist):
        self._argList = arglist
    
    def getNextState(self):
        return self._nextState
    
    def setNextState(self, state):
        self._nextState = state
        
    def checkExitCondition(self):
        return False
    
class Parser_appendPairState(IStackParserState):
    ''' Append the pair of elements to the main tree, depending on operator precedence '''
    def __init__(self, nextState = None):
        self._nextState = nextState
        self._argList = None
        self._stack = None
               
    def executeState(self, stack):
        print("Parser_appendPairState")
        self._stack = stack
        # if it's a value node, append differently. Only happens in the beginning
        if type(self._argList.currentHead) is ValueNode:
            print("appendtoValueNode")
            self._argList.tempOp.setLeftNode(self._argList.currentHead)
            self._argList.previousOp = self._argList.tempOp
            self._argList.currentHead = self._argList.tempOp
            self._argList.tempOp = None
        else:
            if self._argList.tempOp.priority >= self._argList.previousOp.priority:
                self._argList.previousOp = self.appendCurrentOperatorRight(self._argList.previousOp, self._argList.tempOp)
                print("nextOperatorisBigger")
            else:
                self._argList.currentHead = self.appendCurrentOperatorHead(self._argList.currentHead, self._argList.tempOp)
                self._argList.previousOp = self._argList.currentHead
                print("nextOperatorisSmaller")
#                 print("currentHead: " + self._argList.currentHead.getValue())
        self.passArgsForward()
        return self._argList.currentHead

    def checkExitCondition(self):
        retVal = False
        if self._stack.isEmpty() is True:
            retVal =  True
        else:
            retVal = False
        return retVal
             
    def appendCurrentOperatorHead(self, currentOpNode, newHead):
        newHead.setLeftNode(currentOpNode)
        return newHead
    
    #shifts if right larger priority
    def appendCurrentOperatorRight(self, oldRight, newRight):
        temp = oldRight.getRightNode()
        oldRight.setRightNode(newRight)
        newRight.setLeftNode(temp)
        return newRight
    
    def getRightLeafParent(self, headNode):
        retVal = None
        if type(headNode.getRightNode()) is not ValueNode:
            retVal = self.getRightLeafParent(headNode.getRightNode())
        else:
            retVal = headNode
        return retVal
        
    
    def passArgsForward(self):
        self._nextState.setArgList(self._argList)
    
    def setArgList(self, arglist):
        self._argList = arglist
    
    def getNextState(self):
        return self._nextState
    
    def setNextState(self, state):
        self._nextState = state


class ParserArgs():
    def __init__(self):
        self.currentHead = None
        self.previousOp = None
        self.tempOp = None
    
    
    
    
    
    
    