from properties.property import Property
from entities.edge import Edge

class EdgeListProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.value = []

    def get_fields(self):
        pass

    def set_fields(self, data):
        _values = []
        edges = data.edges

        for i in range(len(edges)):
            if edges[i].neighbour == -1:
                edge = Edge(edges[i].startX, edges[i].startY,
                            edges[i].endX, edges[i].endY, None)
            else:
                edge = Edge(edges[i].startX, edges[i].startY, edges[i]
                            .endX, edges[i].endY, edges[i].neighbour)

            _values.append(edge)

        self.value = _values
        self.defined = True

    def set_value(self, _value):
        if self.value is not None:
            self.value.clear()
            self.value.extend(_value)
            self.defined = True
        else:
            self.value = _value

    def set_edges(self, _edges):
        self.value.clear()
        self.value.extend(_edges)
        self.defined = True

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
                                                 edge.get_neighbor().get_value()))
        return new_edge_list_prop
