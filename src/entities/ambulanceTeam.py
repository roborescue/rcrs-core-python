from entities.human import Human
from connection import URN


class AmbulanceTeamEntity(Human):
    urn = URN.Entity.AMBULANCE_TEAM

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def set_entity(self, properties):
        super().set_entity(properties)