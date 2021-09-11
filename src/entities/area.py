from entities.blockade import Blockade
from entities.entity import Entity
from properties.edgeListProperty import EdgeListProperty
from properties.entityIDListProperty import EntityIDListProperty
from properties.standardPropertyURN import StandardPropertyURN
from entities.edge import Edge


class Area(Entity):
    def __init__(self, entity_id):
        super().__init__(entity_id)
        self.edges = EdgeListProperty(StandardPropertyURN.EDGES.value)
        self.blockades = EntityIDListProperty(
            StandardPropertyURN.BLOCKADES.value)

        #self.apexes = None
        self.neighbours = None
        self.shape = None

        self.register_properties([self.edges, self.blockades])

    def set_entity(self, properties):
        super().set_entity(properties)
        for key, values in properties.items():
            _type = StandardPropertyURN.from_string(key)

            if _type == StandardPropertyURN.EDGES.name:
                egdes_list = []
                for edges in values[0].matrixInt.values:
                    edge = Edge(
                        edges.values[0], edges.values[1], edges.values[2], edges.values[3], edges.values[4])
                    egdes_list.append(edge)
                self.edges.set_value(egdes_list)

            elif _type == StandardPropertyURN.BLOCKADES.name:
                self.blockades.set_value(values[0].listInt.values)

    # def get_apexes(self):
    #     if self.apexes is None:
    #         self.apexes = []
    #         for edge in self.get_edges():
    #             self.apexes.append(edge.get_start_x())
    #             self.apexes.append(edge.get_start_y())

    #     return self.apexes

    def get_location(self):
        if self.x.is_defined() and self.y.is_defined():
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
        _type = StandardPropertyURN.from_string(urn)

        if(_type == StandardPropertyURN.X.value):
            return self.x
        elif(_type == StandardPropertyURN.Y.value):
            return self.y
        elif(_type == StandardPropertyURN.EDGES.value):
            return self.edges
        elif(_type == StandardPropertyURN.BLOCKADES.value):
            return self.blockades
        else:
            return super().get_property(urn)

    def get_edges_property(self):
        return self.edges

    def get_edges(self):
        return self.edges.get_value()

    def set_edges(self, value):
        self.edges.set_edges(value)

    def is_edges_defined(self):
        return self.edges.is_defined()

    def undefine_edges(self):
        self.edges.set_undefined()

    def add_edge(self, edge):
        self.edges.add_edge(edge)

    def get_blockades_property(self):
        return self.blockades

    def get_blockades(self):
        return self.blockades.get_value()

    def set_blockades(self, value):
        self.blockades.set_value(value)

    def is_blockades_defined(self):
        return self.blockades.is_defined()

    def undefine_blockades(self):
        self.blockades.set_undefined()

    def get_shape(self):
        return None
