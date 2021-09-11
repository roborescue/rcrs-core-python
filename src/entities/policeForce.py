from entities.standardEntityURN import StandardEntityURN
from entities.human import Human


class PoliceForceEntity(Human):
    urn = StandardEntityURN.POLICE_FORCE.value

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def copy_impl(self):
        return PoliceForceEntity(self.get_id())

    def get_entity_name(self):
        return "Police force"

    def set_entity(self, properties):
        super().set_entity(properties)
