from entities.building import Building

from standardEntityURN import StandardEntityURN
from standardPropertyURN import StandardPropertyURN
from property import IntProperty

class Refuge(Building):

    urn = StandardEntityURN.REFUGE.value

    def __init__(self, entity_id):
        Building.__init__(self, entity_id)
        #print('Refuge Createed = ', entity_id)
