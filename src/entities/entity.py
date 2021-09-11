from worldmodel.entityID import EntityID
from properties.standardPropertyURN import StandardPropertyURN
from properties.intProperty import IntProperty


class Entity:
    def __init__(self, _entity_id):
        self.entity_id = EntityID(_entity_id)
        self.x = IntProperty(StandardPropertyURN.X.value)
        self.y = IntProperty(StandardPropertyURN.Y.value)
        self.properties = {}

        self.register_properties([self.x, self.y])

    def set_entity(self, properties):
        for key, values in properties.items():
            _type = StandardPropertyURN.from_string(key)

            if _type == StandardPropertyURN.X.name:
                self.x.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.Y.name:
                self.y.set_value(values[0].valueInt)

    def get_id(self) -> EntityID:
        return self.entity_id

    def get_properties(self):
        return self.properties

    def register_properties(self, _properties):
        for property in _properties:
            self.properties[property.get_urn()] = property

    def copy_impl(self):
        return Entity(self.get_id())

    def copy(self):
        entity = self.copy_impl()
        for property in self.properties:
            copy = entity.get_property(property.get_urn())
            copy.take_value(property)
        return entity

    def get_urn(self):
        return self.urn

    def __hash__(self):
        return int(self.entity_id.get_value())

    def get_property(self, property_urn):
        return self.properties.get(property_urn)
    
    def get_location(self) -> tuple(IntProperty, IntProperty):
        if self.x.is_defined() and self.y.is_defined():
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
        return self.x.is_defined()

    def undefine_x(self):
        self.x.set_undefined()

    # x property
    def get_y_property(self):
        return self.y

    def get_y(self):
        return self.y.get_value()

    def set_y(self, value):
        self.y.set_value(value)

    def is_y_defined(self):
        return self.y.is_defined()

    def undefine_y(self):
        self.y.set_undefined()

