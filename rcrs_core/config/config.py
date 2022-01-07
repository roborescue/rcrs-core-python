
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

    def get_value(self, key):
        return self.data[key]
    
    def get_float_value(self, key):
        pass
    
    def get_boolean_value(self, key):
        pass
    
    def get_array_value(self, key):
        pass

    def set_value(self, key, value):
        self.data[key] = value
    
