from entities.building import Building
from standardEntityURN import StandardEntityURN

class GasStation(Building):
    urn = StandardEntityURN.GAS_STATION.value

    def __init__(self, entity_id):
        Building.__init__(self, entity_id)
