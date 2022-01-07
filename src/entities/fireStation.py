from connection import URN
from entities.building import Building


class FireStationEntity(Building):
    urn = URN.Entity.FIRE_STATION

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def set_entity(self, properties):
        super().set_entity(properties)
