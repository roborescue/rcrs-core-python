from entities.policeForce import PoliceForceEntity
from standardEntityURN import StandardEntityURN
from entities.human import Human

class AmbulanceTeamEntity(Human):
    urn = StandardEntityURN.AMBULANCE_TEAM.value

    def __init__(self, entity_id):
        Human.__init__(self, entity_id)
        pass