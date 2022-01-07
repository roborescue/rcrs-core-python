from rcrs_core.connection import URN
from rcrs_core.entities.building import Building


class FireStationEntity(Building):
    urn = URN.Entity.FIRE_STATION

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def copy_impl(self):
        return FireStationEntity(self.get_id())

    def get_entity_name(self):
        return "Fire Station"

    def set_entity(self, properties):
        super().set_entity(properties)
