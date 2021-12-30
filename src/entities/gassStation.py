from connection import URN
from entities.building import Building
from entities.standardEntityURN import StandardEntityURN


class GasStation(Building):
    urn = URN.Entity.GAS_STATION

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def get_entity_name(self):
        return "Gass Station"

    def set_entity(self, properties):
        super().set_entity(properties)
