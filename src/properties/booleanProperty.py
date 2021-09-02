from properties.property import Property


class BooleanProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.VALUE = 0

    def set_fields(self, fields):
        self.value = bool(fields.fields[0].valueBool)
        self.set_defined()

    def copy(self):
        new_boolean_prop = BooleanProperty(self.urn)
        new_boolean_prop.value = self.value
        return new_boolean_prop
