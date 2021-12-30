from properties.property import Property

class IntArrayProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.value = []

    def set_fields(self, data):
        self.value = data.values[:]
        _values = []
        for d in data.values:
            _values.append(d)
        self.value = _values
        self.defined = True

    def set_value(self, data):
        if self.value is not None:
            self.value.clear()
            self.value.extend(data.values)
            self.defined = True
        else:
            self.value = data.values[:]

    def take_value(self, _property):
        if isinstance(_property, IntArrayProperty):
            i = IntArrayProperty(_property)
            if i.defined:
                self.set_value(i.get_value())
            else:
                self.defined = False
        else:
            raise Exception("cannot take value from ", _property)
