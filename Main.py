from Stack import Stack
import sys
import argparse
from INode import INode
from ValueNode import ValueNode
from OperatorNode import IOperatorNode
from OperatorNode import OperatorTypeStorage
from NodeFactory import NodeFactory
from StackParser import Parser_idleState, Parser_appendPairState,\
    Parser_makePairState, Parser_initialElementState, StackParser
from StringParser import StringParser

def main():
    ''' Argument parsing '''
    mainparser = argparse.ArgumentParser()
    mainparser.add_argument("string")
    args = mainparser.parse_args()
    # Instantiate the states:
    appendPairState = Parser_appendPairState()
    makePairState = Parser_makePairState(appendPairState)
    makeInitialState = Parser_initialElementState(makePairState)
    idleState = Parser_idleState(makeInitialState)
    appendPairState.setNextState(makePairState)
    
    parserStateList = [idleState, makeInitialState, makePairState, appendPairState]
    
    operatorList = OperatorTypeStorage()

    mainStack = Stack()
    bracketStack = Stack()
    
    factory = NodeFactory(operatorList)

    stackParser = StackParser(operatorList, parserStateList)
    stringParser = StringParser(factory, stackParser, bracketStack, mainStack, operatorList)
    
    returnNode = stringParser.parseString(args.string)
    
    print(returnNode.getValue())
#     print(returnNode)
#     resultNode = factory.makeOperatorNode("*", node1, node2)
#     print(resultNode.getValue())
#     operatorNode = factory.makeOperatorNode("PLUS", node1, node2)
#     
#     val1, val2 = operatorNode.getValue()
# 
#     print(val1.getValue() + val2.getValue())


if __name__ == "__main__":
    main()