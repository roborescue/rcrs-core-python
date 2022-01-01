from connection import URN
from entities.area import Area


class Road(Area):
    urn = URN.Entity.ROAD

    def __init__(self, entity_id) -> None:
        super().__init__(entity_id)

    def set_entity(self, properties) -> None:
        super().set_entity(properties)