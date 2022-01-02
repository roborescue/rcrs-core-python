from properties.property import Property
from connection import URN


class EntityIDProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.value = 0

    def set_fields(self, value):
        self.value = value

    def take_value(self, _property):
        if isinstance(_property, EntityIDProperty):
            self.set_value(_property.get_value())
        else:
            raise Exception("cannot take value from ", _property)
