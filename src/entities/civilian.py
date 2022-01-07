from entities.human import Human
from connection import URN


class Civilian(Human):
    urn = URN.Entity.CIVILIAN

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def set_entity(self, properties):
        super().set_entity(properties)
