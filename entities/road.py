from entities.area import Area
from entities.edge import Edge

from standardEntityURN import StandardEntityURN
from standardPropertyURN import StandardPropertyURN

class Road(Area):
    urn = StandardEntityURN.ROAD.value

    def __init__(self, entity_id):
        Area.__init__(self, entity_id)
        #print("Creating Road = ", entity_id)

    def set_entity(self, properties):
        for key, values in properties.items():
            _type = StandardPropertyURN.from_string( key )
            
            if _type == StandardPropertyURN.X.name:
                self.x.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.Y.name:
                self.y.set_value(values[0].valueInt)

            elif _type == StandardPropertyURN.EDGES.name:
                egdes_list = []
                for edges in values[0].matrixInt.values:
                    edge = Edge(edges.values[0], edges.values[1], edges.values[2], edges.values[3], edges.values[4])
                    egdes_list.append(edge)
                self.edges.set_value(egdes_list)

            elif _type == StandardPropertyURN.BLOCKADES.name:
                print('Road -> set_entity : NOT DEFINED')
                
            
            
            