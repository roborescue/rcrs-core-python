from entities.building import Building
from connection import URN

class AmbulanceCentreEntity(Building):
    urn = URN.Entity.AMBULANCE_CENTRE

    def __init__(self, entity_id):
        super().__init__(entity_id)
        pass

    def set_entity(self, properties):
        super().set_entity(properties)