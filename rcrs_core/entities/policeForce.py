from rcrs_core.connection import URN
from rcrs_core.entities.human import Human


class PoliceForceEntity(Human):
    urn = URN.Entity.POLICE_FORCE

    def __init__(self, entity_id):
        super().__init__(entity_id)

    def copy_impl(self):
        return PoliceForceEntity(self.get_id())

    def get_entity_name(self):
        return "Police force"

    def set_entity(self, properties):
        super().set_entity(properties)
