
from worldmodel.entityID import EntityID


class Entity:
    def __init__(self, _entity_id):
        self.entity_id = EntityID(_entity_id)
        self.properties = {}

    def add_entity_listener(self, l):
        pass

    def remove_entity_listener(self, l):
        pass

    def get_id(self):
        return self.entity_id

    def get_properties(self):
        return self.properties

    def get_location(self, world_model):
        pass

    def register_properties(self, _properties):
        for property in _properties:
            self.properties[property.get_urn()] = property

    def copy(self):
        pass

    def get_urn(self):
        return self.urn

    def __hash__(self):
        return self.entity_id.get_value()

    def set_entity(self, properties):
        pass

    def get_property(self, property_urn):
        return self.properties.get(property_urn)
