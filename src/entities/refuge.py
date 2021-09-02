from entities.building import Building

from entities.standardEntityURN import StandardEntityURN
from properties.standardPropertyURN import StandardPropertyURN
from properties.intProperty import IntProperty


class Refuge(Building):

    urn = StandardEntityURN.REFUGE.value

    def __init__(self, entity_id):
        super().__init__(entity_id)
        pass
