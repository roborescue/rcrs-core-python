from entities.policeForce import PoliceForceEntity
from standardEntityURN import StandardEntityURN
from entities.building import Building


class FireStationEntity(Building):
    urn = StandardEntityURN.FIRE_STATION.value

    def __init__(self, entity_id):
        super().__init__(entity_id)
    
    def copy_impl(self):
        return FireStationEntity(self.get_id())
    
    def get_entity_name():
        return "Fire Station"