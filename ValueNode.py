from INode import INode
#ValueNode

class ValueNode(INode):
    ''' Nodes for storing values, allows setting of values'''
    
    def __init__(self, value):
        self.value = value
        
    def setValue(self, value):
        self.value = value
        
    def getValue(self):
        return self.value