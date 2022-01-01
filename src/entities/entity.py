from connection import URN
from properties.intProperty import IntProperty
from abc import ABC, abstractmethod


class Entity(ABC):
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

    def get_id(self) -> int:
        return self.entity_id

    def get_properties(self):
        return self.properties

    def register_properties(self, _properties):
        for property in _properties:
            self.properties[property.urn] = property

    def get_property(self, property_urn):
        return self.properties.get(property_urn)