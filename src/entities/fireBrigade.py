from connection import URN
from properties.standardPropertyURN import StandardPropertyURN
from entities.standardEntityURN import StandardEntityURN
from entities.human import Human
from properties.intProperty import IntProperty


class FireBrigadeEntity(Human):
    urn = StandardEntityURN.FIRE_BRIGADE.value

    def __init__(self, entity_id):
        super().__init__(entity_id)
        self.water = IntProperty(URN.Property.WATER_QUANTITY)

        self.register_properties([self.water])

    def set_entity(self, properties):
        super().set_entity(properties)
        for key, values in properties.items():
            if key == URN.Property.WATER_QUANTITY:
                self.water.set_value(values)

    def get_entity_name(self):
        return "Fire brigade"

    def get_property(self, urn):
        if urn == URN.Property.WATER_QUANTITY:
            return self.water
        else:
            return super().get_property(urn)