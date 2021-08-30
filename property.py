from entities.edge import Edge
from entityID import EntityID

class Property:
    def __init__(self, _urn):
        self.urn = _urn
        self.defined = False
        self.value = None

    def get_urn(self):
        return self.urn

    def is_defined(self):
        return self.defined

    def set_defined(self):
        self.defined = True

    def set_undefined(self):
        self.defined = False

    def get_value(self):
        return self.value
    
    def set_value(self, _value):
        self.value = _value
        self.set_defined()
    
    def to_string(self):
        print('property = ', self.urn, self.value)
    


class EdgeListProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)

    def set_fields(self, fields):
        _values = []
        edges = fields.get(EdgeListProperty.EDGES)

        for i in range(len(edges)):

            if edges[i][4] == -1:
                edge = Edge( edges[i][0], edges[i][1], edges[i][2], edges[i][3])
            else:
                edge = Edge( edges[i][0], edges[i][1], edges[i][2], edges[i][3], EntityID( edges[i][4] ) )

            _values.append(edge)

        self.value = _values
        self.set_defined()
    
    def copy(self):
        new_edge_list_prop = EdgeListProperty(self.urn)
        new_edge_list_prop.value = []
        for edge in self.value:
            new_edge_list_prop.append(Edge(edge.get_start_x(), edge.get_start_y(),
                                              edge.get_end_x(), edge.get_end_y(),
                                              EntityID(edge.get_neighbor().get_value())))
        return new_edge_list_prop



class EntityIDProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.VALUE = 0

    def __hash__(self):
        return self.value.get_value()

    def set_fields(self, fields):
        self.value = EntityID(fields.fields[0].valueInt)
        self.set_defined()
    
    def copy(self):
        new_entity_id_prop = EntityIDProperty(self.urn)
        new_entity_id_prop.value = EntityID(self.value.get_value())
        return new_entity_id_prop

    
class EntityIDListProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.VALUE = 0
    
    def set_fields(self, fields):
        _values = []
        _fields = fields.fields[0].listInt.values
        for field in _fields:
            _values.append(EntityID(field))
        self.value = _values
        self.set_defined()

    def copy(self):
        new_entity_id_list_prop = EntityIDListProperty(self.urn)
        new_entity_id_list_prop.value = []
        for entity_id in self.value:
            new_entity_id_list_prop.value.append(EntityID(entity_id.get_value()))
        return new_entity_id_list_prop

    
class BooleanProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.VALUE = 0
    
    def set_fields(self, fields):
        self.value = bool(fields.fields[0].valueBool)
        self.set_defined()
    
    def copy(self):
        new_boolean_prop = BooleanProperty(self.urn)
        new_boolean_prop.value = self.value
        return new_boolean_prop


class IntProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.VALUE = 0
    
    def set_fields(self, fields):
        self.value = fields.fields[0].valueInt  
        self.set_defined()  
    
    def copy(self):
        new_int_prop = IntProperty(self.urn)
        new_int_prop.value = self.value
        return new_int_prop
    
    
class IntArrayProperty(Property):
    def __init__(self, urn):
        super().__init__(urn)
        self.VALUE = 0
    
    def set_fields(self, fields):
        _values = []
        data = fields.fields[0].listInt.values
        for d in data:
            _values.append(d)
        self.value = _values
        self.set_defined()

    def copy(self):
        new_int_array_prop = IntArrayProperty(self.urn)
        new_int_array_prop.value = []
        for int_val in self.value:
            new_int_array_prop.value.append(int_val)
        return new_int_array_prop

    




    