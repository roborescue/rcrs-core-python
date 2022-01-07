from typing import List
from connection import URN
from entities.entity import Entity
from properties.edgeListProperty import EdgeListProperty
from properties.entityIDListProperty import EntityIDListProperty


class Area(Entity):

    def __init__(self, entity_id):
        super().__init__(entity_id)
        self.edges = EdgeListProperty(URN.Property.EDGES)
        self.blockades = EntityIDListProperty(URN.Property.BLOCKADES)
        self.neighbours = None
        self.shape = None
        self.apexList = List[int]
        self.register_properties([self.edges, self.blockades])

    def set_entity(self, properties):
        super().set_entity(properties)
        for key, values in properties.items():
            if key == URN.Property.EDGES:
                self.edges.set_fields(values)
            elif key == URN.Property.BLOCKADES:
                self.blockades.set_value(values)

    def get_location(self):
        return self.x.get_value(), self.y.get_value()

    def get_neighbours(self):
        if self.neighbours is None:
            self.neighbours = []
            for edge in self.edges.get_value():
                if edge.is_passable():
                    self.neighbours.append(edge.get_neighbour())
        return self.neighbours

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

    def get_edges_property(self):
        return self.edges

    def get_edges(self) -> List[Entity]:
        return self.edges.get_value()

    def set_edges(self, value):
        self.edges.set_edges(value)

    def add_edge(self, edge):
        self.edges.add_edge(edge)

    def get_blockades_property(self):
        return self.blockades

    def get_blockades(self):
        return self.blockades.get_value()

    def set_blockades(self, value):
        self.blockades.set_value(value)

    def get_shape(self):
        return None
