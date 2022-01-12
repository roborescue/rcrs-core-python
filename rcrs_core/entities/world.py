from rcrs_core.connection import URN
from rcrs_core.entities.entity import Entity
from rcrs_core.properties.intProperty import IntProperty


class World(Entity):
    urn = URN.Entity.WORLD

    def __init__(self, entity_id) -> None:
        super().__init__(entity_id)

        self.start_time = IntProperty(URN.Property.START_TIME)
        self.longitude = IntProperty(URN.Property.LONGITUDE)
        self.latitude = IntProperty(URN.Property.LATITUDE)
        self.wind_force = IntProperty(URN.Property.WIND_FORCE)
        self.wind_direction = IntProperty(URN.Property.WIND_DIRECTION)

        self.register_properties([self.start_time, self.longitude, self.latitude])
        self.register_properties([self.wind_force, self.wind_direction])

    def set_entity(self, properties):
        super().set_entity(properties)
        for key, values in properties.items():
            if key == URN.Property.START_TIME:
                self.start_time.set_value(values)

            elif key == URN.Property.LONGITUDE:
                self.longitude.set_value(values)

            elif key == URN.Property.LATITUDE:
                self.latitude.set_value(values)

            elif key == URN.Property.WIND_FORCE:
                self.wind_force.set_value(values)

            elif key == URN.Property.WIND_DIRECTION:
                self.wind_direction.set_value(values)
    
    def copy_impl(self):
        return World(self.get_id())
