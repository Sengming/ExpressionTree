from INode import INode
#ValueNode

class ValueNode(INode):
    ''' Nodes for storing values, allows setting of values'''
    
    def __init__(self, value = 'EmptyNode'):
        self.value = value
        
    def setValue(self, value):
        self.value = value
        
    def getValue(self):
        return self.value
    
class StartBracketNode(INode):
    ''' Dummy node to denote(pun intended)a start bracket node. Should not be included in any tree parse stack'''
    
    def __init__(self):
        self.value = '('
        
    def getValue(self):
        return self.value
        