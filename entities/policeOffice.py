from entities.policeForce import PoliceForceEntity
from standardEntityURN import StandardEntityURN
from entities.building import Building


class PoliceOfficeEntity(Building):
    urn = StandardEntityURN.POLICE_OFFICE.value

    def __init__(self, entity_id):
        Building.__init__(self, entity_id)
        print('PoliceOffice Created ... = ', entity_id)
