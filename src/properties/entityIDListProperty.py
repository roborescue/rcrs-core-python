from properties.property import Property
from typing import List


class EntityIDListProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.value = []

    def set_fields(self, data):
        _values = []
        for d in data.values:
            _values.append(d)
        self.value = _values

    def set_value(self, _value: List[int]):
        if self.value is not None:
            self.value.clear()
            self.value.extend(_value)
        else:
            self.value = _value

    def take_value(self, _property):
        if isinstance(_property, EntityIDListProperty):
            self.set_value(_property.get_value())
        else:
            raise Exception("cannot take value from ", _property)
