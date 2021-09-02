from properties.property import Property
from worldmodel.entityID import EntityID


class EntityIDProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.VALUE = 0

    def __hash__(self):
        return self.value.get_value()

    def set_fields(self, fields):
        self.value = EntityID(fields.fields[0].valueInt)
        self.set_defined()

    def copy(self):
        new_entity_id_prop = EntityIDProperty(self.urn)
        new_entity_id_prop.value = EntityID(self.value.get_value())
        return new_entity_id_prop
