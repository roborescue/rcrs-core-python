from connection import URN
from entities.road import Road


class Hydrant(Road):
    urn = URN.Entity.HYDRANT

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def set_entity(self, properties):
        super().set_entity(properties)