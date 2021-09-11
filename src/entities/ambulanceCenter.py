from entities.standardEntityURN import StandardEntityURN
from entities.building import Building


class AmbulanceCentreEntity(Building):
    urn = StandardEntityURN.AMBULANCE_CENTRE.value

    def __init__(self, entity_id):
        super().__init__(entity_id)
        pass

    def set_entity(self, properties):
        super().set_entity(properties)

    def get_entity_name(self):
        return "Ambulance Centre"

    def copy_impl(self):
        return AmbulanceCentreEntity(self.get_id())
