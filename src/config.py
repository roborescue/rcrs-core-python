
class Config:
    
    
    def __init__(self) -> None:
        self.data = {}
        self.noCache = {}
        self.intData = {}
        self.floatData = {}
        self.booleanData = {}
        self.arrayData = {}
        self.constraints = {}
        self.violatedConstraints = {}

    def getValue(self, key):
        return self.data[key]
    
    def getFloatValue(self, key):
        pass
    
    def getBooleanValue(self, key):
        pass
    
    def getArrayValue(self, key):
        pass

    def setValue(self, key, value):
        self.data[key] = value
    
