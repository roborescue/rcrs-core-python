from connection import URN
from entities.human import Human


class PoliceForceEntity(Human):
    urn = URN.Entity.POLICE_FORCE

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def set_entity(self, properties):
        super().set_entity(properties)
