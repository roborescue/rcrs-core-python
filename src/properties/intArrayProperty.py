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
        self.set_defined()

    def set_value(self, data):
        if self.value is not None:
            self.value.clear()
            self.value.extend(data.values)
            self.set_defined()
        else:
            self.value = data.values[:]

    def copy(self):
        new_int_array_prop = IntArrayProperty(self.urn)
        new_int_array_prop.value = []
        for int_val in self.value:
            new_int_array_prop.value.append(int_val)
        return new_int_array_prop
    
    def take_value(self, _property):
        if isinstance(_property, IntArrayProperty):
            i = IntArrayProperty(_property)
            if i.defined:
                self.set_value(i.get_value())
            else:
                self.set_value(None)
        else:
            raise Exception("cannot take value from ", _property)
