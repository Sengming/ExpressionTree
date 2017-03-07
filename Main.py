from Stack import Stack
import sys
import argparse
from INode import INode
from ValueNode import ValueNode
from OperatorNode import IOperatorNode
from OperatorNode import OperatorTypeStorage
from NodeFactory import NodeFactory

def main():
    ''' Argument parsing '''
    mainparser = argparse.ArgumentParser()
    mainparser.add_argument("echo")
    args = mainparser.parse_args()
    print(args.echo)
    node1, node2 = ValueNode(100), ValueNode(300)
    
    opStorage = OperatorTypeStorage()
    #operatorNode = OperatorNode(node1, node2)
    factory = NodeFactory(opStorage)
    
    resultNode = factory.makeOperatorNode("*", node1, node2)
    print(resultNode.getValue())
#     operatorNode = factory.makeOperatorNode("PLUS", node1, node2)
#     
#     val1, val2 = operatorNode.getValue()
# 
#     print(val1.getValue() + val2.getValue())


if __name__ == "__main__":
    main()