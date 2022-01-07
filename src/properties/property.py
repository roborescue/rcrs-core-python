

class Property:
    def __init__(self, _urn):
        self.urn = _urn
        self.value = None

    def get_urn(self):
        return self.urn

    def get_value(self):
        return self.value

    def set_value(self, _value):
        self.value = _value

    def to_string(self):
        print('property = ', self.urn, self.value)
