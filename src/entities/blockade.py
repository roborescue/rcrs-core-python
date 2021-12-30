from connection import URN
from entities.entity import Entity
from properties.entityIDProperty import EntityIDProperty
from properties.intArrayProperty import IntArrayProperty
from properties.intProperty import IntProperty
from entities.standardEntityURN import StandardEntityURN


class Blockade(Entity):
    urn = StandardEntityURN.BLOCKADE.value

    def __init__(self, entity_id):
        super().__init__(entity_id)
        self.position = EntityIDProperty(URN.Property.POSITION)
        self.apexes = IntArrayProperty(URN.Property.APEXES)
        self.repair_cost = IntProperty(URN.Property.REPAIR_COST)
        self.shape = None

        self.register_properties(
            [self.position, self.apexes, self.repair_cost])

    def get_entity_name(self):
        return "Blockade"

    def set_entity(self, properties):
        super().set_entity(properties)

        for key, values in properties.items():
            if key == URN.Property.POSITION:
                self.position.set_value(values)

            elif key == URN.Property.REPAIR_COST:
                self.repair_cost.set_value(values)

            elif key == URN.Property.APEXES:
                self.apexes.set_value(values)

    def get_property(self, urn):

        if(urn == URN.Property.X):
            return self.x
        elif(urn == URN.Property.Y):
            return self.y
        elif(urn == URN.Property.POSITION):
            return self.position
        elif(urn == URN.Property.APEXES):
            return self.apexes
        elif(urn == URN.Property.REPAIR_COST):
            return self.repair_cost
        else:
            return super().get_property(urn)