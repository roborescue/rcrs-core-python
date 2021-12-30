

class Property:
    def __init__(self, _urn):
        self.urn = _urn
        self.defined = False
        self.value = None

    def get_value(self):
        return self.value

    def set_value(self, _value):
        self.value = _value
        self.defined = True

    def to_string(self):
        print('property = ', self.urn, self.value)
