from rcrs_core.connection import URN
from rcrs_core.entities.road import Road


class Hydrant(Road):
    urn = URN.Entity.HYDRANT

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def copy_impl(self):
        return Hydrant(self.get_id())

    def get_entity_name(self):
        return "Hydrant"
    
    def set_entity(self, properties):
        super().set_entity(properties)