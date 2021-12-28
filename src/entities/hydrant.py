from entities.road import Road
from entities.standardEntityURN import StandardEntityURN


class Hydrant(Road):
    urn = StandardEntityURN.HYDRANT.value

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def copy_impl(self):
        return Hydrant(self.entity_id)

    def get_entity_name(self):
        return "Hydrant"
    
    def set_entity(self, properties):
        super().set_entity(properties)