from rcrs_core.entities.human import Human
from rcrs_core.connection import URN


class Civilian(Human):
    urn = URN.Entity.CIVILIAN

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def copy_impl(self):
        return Civilian(self.get_id())

    def get_entity_name(self):
        return "Civilian"

    def set_entity(self, properties):
        super().set_entity(properties)
