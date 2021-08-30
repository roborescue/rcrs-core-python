from entities.policeForce import PoliceForceEntity
from standardEntityURN import StandardEntityURN
from entities.building import Building


class FireStationEntity(Building):
    urn = StandardEntityURN.FIRE_STATION.value

    def __init__(self, entity_id):
        Building.__init__(self, entity_id)
        print('FireStation Created .. = ', entity_id)
