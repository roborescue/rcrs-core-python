from rcrs_core.properties.property import Property
from rcrs_core.worldmodel.entityID import EntityID
from typing import List


class EntityIDListProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.value = []

    def set_fields(self, data):
        _values = []
        for d in data.values:
            _values.append(EntityID(d))
        self.value = _values

    def set_value(self, _value: List[EntityID]):
        if self.value is not None:
            self.value.clear()
            self.value.extend(_value)
        else:
            self.value = _value

    def copy(self):
        new_entity_id_list_prop = EntityIDListProperty(self.urn)
        new_entity_id_list_prop.value = []
        for entity_id in self.value:
            new_entity_id_list_prop.value.append(
                EntityID(entity_id.get_value()))
        return new_entity_id_list_prop

    def take_value(self, _property):
        if isinstance(_property, EntityIDListProperty):
            self.set_value(_property.get_value())
        else:
            raise Exception("cannot take value from ", _property)
