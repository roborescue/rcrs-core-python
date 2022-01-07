from properties.property import Property

class IntArrayProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.value = []

    def set_fields(self, data):
        self.value = data.values[:]

    def set_value(self, data):
        if self.value is not None:
            self.value.clear()
            self.value.extend(data.values[:])
        else:
            self.value = data[:]

    def take_value(self, _property):
        if isinstance(_property, IntArrayProperty):
            if self.value is not None:
                self.value.clear()
                self.value.extend(_property.get_value())
            else:
                self.value = _property.get_value()
        else:
            raise Exception("cannot take value from ", _property)
