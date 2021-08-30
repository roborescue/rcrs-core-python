from entities.entity import Entity
from property import *
from standardPropertyURN import StandardPropertyURN

class Area(Entity):
    def __init__(self, entity_id):
        Entity.__init__(self, entity_id)
        self.x = IntProperty(StandardPropertyURN.X.value)
        self.y = IntProperty(StandardPropertyURN.Y.value)
        self.edges = EdgeListProperty(StandardPropertyURN.EDGES.value)
        self.blockades = EntityIDListProperty(StandardPropertyURN.BLOCKADES.value)

        self.register_properties([self.x, self.y, self.edges, self.blockades])
        self.apexes = None

    def get_edges(self):
        return self.edges.get_value()

    def get_apexes(self):
        if self.apexes is None:
            self.apexes = []
            for edge in self.get_edges():
                self.apexes.append(edge.get_start_x())
                self.apexes.append(edge.get_start_y())

        return self.apexes

    def get_location(self, world_model):
        if self.x.is_defined() and self.y.is_defined():
            return self.x.get_value(), self.y.get_value()
        else:
            return None, None