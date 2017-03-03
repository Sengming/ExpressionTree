
class Stack:
    '''This class helps us perform stack operations'''
    def __init__(self):
        self.stackData = []
        self.size = 0
        
    def push(self, inData):
        self.stackData.append(inData)
        ++self.size
        
    def pop(self):
        returnValue = self.stackData.pop()
        --self.size
        return returnValue
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.stackData == []