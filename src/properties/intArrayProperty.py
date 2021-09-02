from properties.property import Property
from worldmodel.entityID import EntityID


class IntArrayProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.VALUE = 0

    def set_fields(self, fields):
        _values = []
        data = fields.fields[0].listInt.values
        for d in data:
            _values.append(d)
        self.value = _values
        self.set_defined()

    def set_value(self, _value):
        if self.value != None:
            self.value.clear()
            self.value.extend(_value)
            self.set_defined()
        else:
            self.value = _value

    def copy(self):
        new_int_array_prop = IntArrayProperty(self.urn)
        new_int_array_prop.value = []
        for int_val in self.value:
            new_int_array_prop.value.append(int_val)
        return new_int_array_prop
