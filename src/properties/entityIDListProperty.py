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
        self.defined = True

    def set_value(self, _value: List[int]):
        if self.value is not None:
            self.value.clear()
            self.value.extend(_value)
            self.defined = True
        else:
            self.value = _value

    def copy(self):
        new_entity_id_list_prop = EntityIDListProperty(self.urn)
        new_entity_id_list_prop.value = []
        for entity_id in self.value:
            new_entity_id_list_prop.value.append(
                entity_id)
        return new_entity_id_list_prop

    def take_value(self, _property):
        if isinstance(_property, EntityIDListProperty):
            i = EntityIDListProperty(_property)
            if i.defined:
                self.set_value(i.get_value())
            else:
                self.defined = False
        else:
            raise Exception("cannot take value from ", _property)