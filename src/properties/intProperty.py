from properties.property import Property
from worldmodel.entityID import EntityID


class IntProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.VALUE = 0

    def set_fields(self, fields):
        self.value = fields.fields[0].valueInt
        self.set_defined()

    def copy(self):
        new_int_prop = IntProperty(self.urn)
        new_int_prop.value = self.value
        return new_int_prop
