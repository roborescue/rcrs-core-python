from rcrs_core.properties.property import Property
from rcrs_core.connection import URN


class IntProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.value = 0

    def set_fields(self, value):
        self.value = value

    def copy(self):
        new_int_prop = IntProperty(self.urn)
        new_int_prop.value = self.value
        return new_int_prop

    def take_value(self, _property):
        if isinstance(_property, IntProperty):
            self.set_value(_property.get_value())
        else:
            raise Exception("cannot take value from ", _property)
