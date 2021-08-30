from standardEntityURN import StandardEntityURN
from entities.human import Human

class PoliceForceEntity(Human):
    urn = StandardEntityURN.POLICE_FORCE.value

    def __init__(self, entity_id):
        Human.__init__(self, entity_id)
        print('PoliceForce Created ... = ', entity_id)

    