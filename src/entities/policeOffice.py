from connection import URN
from entities.building import Building


class PoliceOfficeEntity(Building):
    urn = URN.Entity.POLICE_OFFICE

    def __init__(self, entity_id):
        Building.__init__(self, entity_id)

    def set_entity(self, properties):
        super().set_entity(properties)
