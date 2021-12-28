from entities.standardEntityURN import StandardEntityURN
from entities.human import Human


class Civilian(Human):
    urn = StandardEntityURN.CIVILIAN.value

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def copy_impl(self):
        return Civilian(self.entity_id)

    def get_entity_name(self):
        return "Civilian"

    def set_entity(self, properties):
        super().set_entity(properties)
