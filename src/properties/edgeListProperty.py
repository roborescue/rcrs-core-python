from typing import List
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

    def set_value(self, _value: List[Edge]):
        print(type(_value))
        if self.value is not None:
            self.value.clear()
            self.value.extend(_value)
        else:
            self.value = _value

    def set_edges(self, _edges: List[Edge]):
        self.value.clear()
        self.value.extend(_edges)

    def add_edge(self, _edge):
        if isinstance(_edge, Edge):
            self.value.append(_edge)

    def clear_edges(self):
        self.value.clear()

    def take_value(self, _value):
        print('edge list property was not implemented....?')
        pass