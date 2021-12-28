from entities.area import Area
from entities.standardEntityURN import StandardEntityURN


class Road(Area):
    urn = StandardEntityURN.ROAD.value

    def __init__(self, entity_id) -> None:
        super().__init__(entity_id)

    def set_entity(self, properties) -> None:
        super().set_entity(properties)

    def get_entity_name(self) -> str:
        return "Road"

    def copy_impl(self):
        return Road(self.entity_id)
