from properties.property import Property
from worldmodel.entityID import EntityID


class EntityIDListProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.VALUE = 0

    def set_fields(self, fields):
        _values = []
        _fields = fields.fields[0].listInt.values
        for field in _fields:
            _values.append(EntityID(field))
        self.value = _values
        self.set_defined()

    def set_value(self, _value):
        if self.value is not None:
            self.value.clear()
            self.value.extend(_value)
            self.set_defined()
        else:
            self.value = _value

    def copy(self):
        new_entity_id_list_prop = EntityIDListProperty(self.urn)
        new_entity_id_list_prop.value = []
        for entity_id in self.value:
            new_entity_id_list_prop.value.append(EntityID(entity_id.get_value()))
        return new_entity_id_list_prop

