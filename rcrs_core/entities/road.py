from rcrs_core.connection import URN
from rcrs_core.entities.area import Area


class Road(Area):
    urn = URN.Entity.ROAD

    def __init__(self, entity_id) -> None:
        super().__init__(entity_id)

    def set_entity(self, properties) -> None:
        super().set_entity(properties)

    def get_entity_name(self) -> str:
        return "Road"

    def copy_impl(self):
        return Road(self.get_id())
