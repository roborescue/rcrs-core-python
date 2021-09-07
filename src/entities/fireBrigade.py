from properties.standardPropertyURN import StandardPropertyURN
from entities.policeForce import PoliceForceEntity
from entities.standardEntityURN import StandardEntityURN
from entities.human import Human
from properties.intProperty import IntProperty


class FireBrigadeEntity(Human):
    urn = StandardEntityURN.FIRE_BRIGADE.value

    def __init__(self, entity_id):
        super().__init__(entity_id)
        self.water = IntProperty(StandardPropertyURN.WATER_QUANTITY.value)
        
        self.register_properties([self.water])

    def set_entity(self, properties):
        for key, values in properties.items():
            _type = StandardPropertyURN.from_string(key)

            if _type == StandardPropertyURN.WATER_QUANTITY.name:
                super().set_entity(properties)
                self.water.set_value(values[0].valueInt)

    def copy_impl(self):
        return FireBrigadeEntity(self.get_id())

    def get_entity_name(self):
        return "Fire brigade"

    def get_property(self, urn):
        _type = StandardPropertyURN.from_string(urn)

        if(_type == StandardPropertyURN.WATER_QUANTITY.value):
            return self.water
        else:
            return super().get_property(urn)

    def get_water_property(self):
        return self.water

    def get_water(self):
        return self.water.get_value()

    def set_water(self, value):
        self.water.set_value(value)

    def is_water_defined(self):
        return self.water.is_defined()

    def undefine_water(self):
        self.water.set_undefined()
