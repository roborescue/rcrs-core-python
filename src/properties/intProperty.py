from properties.property import Property


class IntProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.value = 0

    def set_fields(self, value):
        self.value = value
        self.set_defined()

    def copy(self):
        new_int_prop = IntProperty(self.urn)
        new_int_prop.value = self.value
        return new_int_prop

    def take_value(self, _property):
        if isinstance(_property, IntProperty):
            i = IntProperty(_property)
            if i.defined:
                self.set_value(i.get_value())
            else:
                self.set_undefined()
        else:
            raise Exception("cannot take value from ", _property)
