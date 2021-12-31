from properties.property import Property
from worldmodel.entityID import EntityID


class IntArrayProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.value = []

    def set_fields(self, data):
        self.value = data.values[:]

    def set_value(self, data):
        if self.value is not None:
            self.value.clear()
            self.value.extend(data.values[:])
        else:
            self.value = data[:]

    def copy(self):
        new_int_array_prop = IntArrayProperty(self.urn)
        new_int_array_prop.value = []
        for int_val in self.value:
            new_int_array_prop.value.append(int_val)
        return new_int_array_prop
    
    def take_value(self, _property):
        if isinstance(_property, IntArrayProperty):
            if self.value is not None:
                self.value.clear()
                self.value.extend(_property.get_value())
            else:
                self.value = _property.get_value[:]
        else:
            raise Exception("cannot take value from ", _property)
