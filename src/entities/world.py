from entities.entity import Entity
from properties.standardPropertyURN import StandardPropertyURN
from standardEntityURN import StandardEntityURN

from properties.intProperty import IntProperty
from properties.entityIDProperty import EntityIDProperty
from properties.intArrayProperty import IntArrayProperty


class World(Entity):
    urn = StandardEntityURN.WORLD.value

    def __init__(self, entity_id) -> None:
        super().__init__(entity_id)

        self.start_time = IntProperty(StandardPropertyURN.START_TIME.value)
        self.longitude = IntProperty(StandardPropertyURN.LONGITUDE.value)
        self.latitude = IntProperty(StandardPropertyURN.LATITUDE.value)
        self.wind_force = IntProperty(StandardPropertyURN.WIND_FORCE.value)
        self.wind_direction = IntProperty(StandardPropertyURN.WIND_DIRECTION.value)

        self.register_properties([self.start_time, self.longitude, self.latitude])
        self.register_properties([self.wind_force, self.wind_direction])
        
    def set_entity(self, properties):
        super().set_entity(properties)
        for key, values in properties.items():
            _type = StandardPropertyURN.from_string(key)

            if _type == StandardPropertyURN.START_TIME.name:
                self.start_time.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.LONGITUDE.name:
                self.longitude.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.LATITUDE.name:
                self.latitude.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.WIND_FORCE.name:
                self.wind_force.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.WIND_DIRECTION.name:
                self.wind_direction.set_value(values[0].valueInt)
    
    def copy_impl(self):
        return World(self.get_id())
