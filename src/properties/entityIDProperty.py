from properties.property import Property
from worldmodel.entityID import EntityID


class EntityIDProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.VALUE = 0

    def set_fields(self, fields):
        self.value = EntityID(fields.fields[0].valueInt)
        self.set_defined()

    def copy(self):
        new_entity_id_prop = EntityIDProperty(self.urn)
        new_entity_id_prop.value = EntityID(self.value.get_value())
        return new_entity_id_prop

    def take_value(self, _property):
        if isinstance(_property, EntityIDProperty):
            i = EntityIDProperty(_property)
            if i.is_defined():
                self.set_value(i.get_value())
            else:
                self.set_undefined()
        else:
            raise Exception("cannot take value from ", _property)
