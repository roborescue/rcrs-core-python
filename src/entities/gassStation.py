from connection import URN
from entities.building import Building


class GasStation(Building):
    urn = URN.Entity.GAS_STATION

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def set_entity(self, properties):
        super().set_entity(properties)
