from properties.property import Property
from entities.edge import Edge
from worldmodel.entityID import EntityID


class EdgeListProperty(Property):
    EDGES = 0

    def __init__(self, urn):
        super().__init__(urn)

    def get_fields(self):
        pass

    def set_fields(self, fields):
        _values = []
        edges = fields.get(EdgeListProperty.EDGES)

        for i in range(len(edges)):

            if edges[i][4] == -1:
                
                edge = Edge(edges[i][0], edges[i][1],
                            edges[i][2], edges[i][3], None)
            else:
                edge = Edge(edges[i][0], edges[i][1], edges[i]
                            [2], edges[i][3], EntityID(edges[i][4]))

            _values.append(edge)

        self.value = _values
        self.set_defined()

    def set_value(self, _value):
        if self.value is not None:
            self.value.clear()
            self.value.extend(_value)
            self.set_defined()
        else:
            self.value = _value

    def set_edges(self, _edges):
        self.value.clear()
        self.value.extend(_edges)
        self.set_defined()

    def add_edge(self, _edge):
        if isinstance(_edge, Edge):
            self.value.append(_edge)

    def clear_edges(self):
        self.value.clear()

    def take_value(self, _value):
        pass

    def copy(self):
        new_edge_list_prop = EdgeListProperty(self.urn)
        new_edge_list_prop.value = []
        for edge in self.value:
            new_edge_list_prop.value.append(Edge(edge.get_start_x(), edge.get_start_y(),
                                                 edge.get_end_x(), edge.get_end_y(),
                                                 EntityID(edge.get_neighbor().get_value())))
        return new_edge_list_prop
