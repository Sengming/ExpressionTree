from Stack import Stack
import sys
import argparse
from INode import INode
from ValueNode import ValueNode
from OperatorNode import OperatorNode

def main():
    ''' Argument parsing '''
    mainparser = argparse.ArgumentParser()
    mainparser.add_argument("echo")
    args = mainparser.parse_args()
    print(args.echo)
    node1, node2 = ValueNode(100), ValueNode(300)
    
    operatorNode = OperatorNode(node1, node2)

    return 0

if __name__ == "__main__":
    main()