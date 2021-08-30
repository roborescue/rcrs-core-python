from entities.entity import Entity

from property import EntityIDProperty
from property import IntArrayProperty
from property import IntProperty

from standardEntityURN import StandardEntityURN
from standardPropertyURN import StandardPropertyURN

class Blockade(Entity):
    urn = StandardEntityURN.BLOCKADE.value

    def __init__(self, entity_id):
        Entity.__init__(self, entity_id)
        print('Blockade Createed = ', entity_id)
        self.x = IntProperty(StandardPropertyURN.X.value)
        self.y = IntProperty(StandardPropertyURN.Y.value)
        self.position = EntityIDProperty(StandardPropertyURN.POSITION.value)
        self.apexes = IntArrayProperty(StandardPropertyURN.APEXES.value)
        self.repair_cost = IntProperty(StandardPropertyURN.REPAIR_COST.value)
        self.register_properties([self.x, self.y, self.position, self.apexes, self.repair_cost])

    def get_apexes(self):
        return self.apexes.get_value()

    def get_location(self, world_model):
        if self.x.is_defined() and self.y.is_defined():
            return self.x.get_value(), self.y.get_value()
        else:
            return None, None

    def set_entity(self, properties):
        for key, values in properties.items():
            _type = StandardPropertyURN.from_string( key )
            
            if _type == StandardPropertyURN.X.name:
                self.x.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.Y.name:
                self.y.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.POSITION.name:
                self.position.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.REPAIR_COST.name:
                self.repair_cost.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.APEXES.name:
                print('Blockade -> set_entity : NOT DEFINED')
            

            
           