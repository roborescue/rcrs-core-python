from entities.policeForce import PoliceForceEntity
from standardEntityURN import StandardEntityURN
from entities.building import Building


class PoliceOfficeEntity(Building):
    urn = StandardEntityURN.POLICE_OFFICE.value

    def __init__(self, entity_id):
        Building.__init__(self, entity_id)
        print('PoliceOffice Created ... = ', entity_id)

    def copy_impl(self):
        return PoliceOfficeEntity(self.get_id())
    
    def get_entity_name():
        return "Police office"