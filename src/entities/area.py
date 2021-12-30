from connection import URN
from entities.entity import Entity
from properties.edgeListProperty import EdgeListProperty
from properties.entityIDListProperty import EntityIDListProperty
from entities.edge import Edge


class Area(Entity):
    def __init__(self, entity_id):
        super().__init__(entity_id)
        self.edges = EdgeListProperty(URN.Property.EDGES)
        self.blockades = EntityIDListProperty(URN.Property.BLOCKADES)

        self.apexes = None
        self.neighbours = None
        self.shape = None

        self.register_properties([self.edges, self.blockades])

    def set_entity(self, properties):
        super().set_entity(properties)
        for key, values in properties.items():
            if key == URN.Property.EDGES:
                self.edges.set_fields(values)
                egdes_list = []
                for edges in values.edges:
                    edge = Edge(edges.startX, edges.startY, edges.endX, edges.endY, edges.neighbour)
                    egdes_list.append(edge)
                self.edges.set_value(egdes_list)

            elif key == URN.Property.BLOCKADES:
                self.blockades.set_value(values)

    def get_apexes(self):
        if self.apexes is None:
            self.apexes = []
            for edge in self.get_edges():
                self.apexes.append(edge.get_start_x())
                self.apexes.append(edge.get_start_y())

        return self.apexes

    def get_location(self):
        if self.x.defined and self.y.defined:
            return self.x.get_value(), self.y.get_value()

        return None, None

    def get_neighbours(self):
        if self.neighbours is None:
            neighbours = []
            for edge in self.edges.get_value():
                if edge.is_passable():
                    neighbours.append(edge.get_neighbour())

        return neighbours

    def get_edge_to(self, neighbour):
        for edge in self.get_edges():
            if neighbour.equals(edge.get_neighbour()):
                return edge
        return None

    def get_property(self, urn):

        if(urn == URN.Property.X):
            return self.x
        elif(urn == URN.Property.Y):
            return self.y
        elif(urn == URN.Property.EDGES):
            return self.edges
        elif(urn == URN.Property.BLOCKADES):
            return self.blockades
        else:
            return super().get_property(urn)