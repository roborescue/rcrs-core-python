from entities.standardEntityURN import StandardEntityURN
from entities.human import Human


class AmbulanceTeamEntity(Human):
    urn = StandardEntityURN.AMBULANCE_TEAM.value

    def __init__(self, entity_id):
        super().__init__(entity_id)
        pass

    def set_entity(self, properties):
        super().set_entity(properties)

    def get_entity_name(self):
        return "Ambulance Team"