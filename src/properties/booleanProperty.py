from properties.property import Property


class BooleanProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.value = 0

    def set_fields(self, value):
        self.value = bool(value)
        self.defined = True

    def take_value(self, _property):
        if isinstance(_property, BooleanProperty):
            b = BooleanProperty(_property)
            if b.defined:
                self.set_value(b.get_value())
            else:
                self.defined = False
        else:
            raise Exception("cannot take value from ", _property)
