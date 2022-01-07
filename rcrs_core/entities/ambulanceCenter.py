from rcrs_core.entities.building import Building
from rcrs_core.connection import URN

class AmbulanceCentreEntity(Building):
    urn = URN.Entity.AMBULANCE_CENTRE

    def __init__(self, entity_id):
        super().__init__(entity_id)
        pass

    def set_entity(self, properties):
        super().set_entity(properties)

    def get_entity_name(self):
        return "Ambulance Centre"

    def copy_impl(self):
        return AmbulanceCentreEntity(self.get_id())
