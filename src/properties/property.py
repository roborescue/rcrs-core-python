

class Property:
    def __init__(self, _urn):
        self.urn = _urn
        self.defined = False
        self.value = None

    def set_defined(self):
        self.defined = True

    def get_value(self):
        return self.value

    def set_value(self, _value):
        self.value = _value
        self.set_defined()

    def to_string(self):
        print('property = ', self.urn, self.value)
