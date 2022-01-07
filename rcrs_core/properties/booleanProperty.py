from rcrs_core.properties.property import Property


class BooleanProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.value = 0

    def set_fields(self, value):
        self.value = bool(value)

    def copy(self):
        new_boolean_prop = BooleanProperty(self.urn)
        new_boolean_prop.value = self.value
        return new_boolean_prop

    def take_value(self, _property):
        if isinstance(_property, BooleanProperty):
            self.set_value(_property.get_value())
        else:
            raise Exception("cannot take value from ", _property)
