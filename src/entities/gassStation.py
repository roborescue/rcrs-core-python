from entities.building import Building
from entities.standardEntityURN import StandardEntityURN


class GasStation(Building):
    urn = StandardEntityURN.GAS_STATION.value

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def copy_impl(self):
        return GasStation(self.get_id())

    def get_entity_name(self):
        return "Gass Station"

    def set_entity(self, properties):
        super().set_entity(properties)
