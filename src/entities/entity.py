from connection import URN
from properties.intProperty import IntProperty


class Entity:
    def __init__(self, _entity_id):
        self.entity_id = _entity_id
        self.x = IntProperty(URN.Property.X)
        self.y = IntProperty(URN.Property.Y)
        self.properties = {}

        self.register_properties([self.x, self.y])

    def set_entity(self, properties):
        for key, values in properties.items():

            if key == URN.Property.X:
                self.x.set_value(values)

            elif key == URN.Property.Y:
                self.y.set_value(values)

    def get_properties(self):
        return self.properties

    def register_properties(self, _properties):
        for property in _properties:
            self.properties[property.urn] = property

    def copy_impl(self):
        return Entity(self.entity_id)

    def copy(self):
        entity = self.copy_impl()
        for property in self.properties:
            copy = entity.get_property(property.urn)
            copy.take_value(property)
        return entity

    def __hash__(self):
        return int(self.entity_id.get_value())

    def get_property(self, property_urn):
        return self.properties.get(property_urn)
    
    def get_location(self):
        if self.x.defined and self.y.defined:
            return self.x.get_value(), self.y.get_value()
        else:
            return None, None
    
    # y property
    def get_x_property(self):
        return self.x

    def get_x(self):
        return self.x.get_value()

    def set_x(self, value):
        self.x.set_value(value)

    def is_x_defined(self):
        return self.x.defined

    # x property
    def get_y_property(self):
        return self.y

    def get_y(self):
        return self.y.get_value()

    def set_y(self, value):
        self.y.set_value(value)

    def is_y_defined(self):
        return self.y.defined