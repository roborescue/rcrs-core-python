from core.RCRSProto_pb2 import EntityURN,PropertyURN
class Entity:
    
    def __init__(self,urn,id):
        self.properties={}
        self.urn=urn
        self.id=id
    
    def getURN(self):
        return self.urn
    def getID(self):
        return self.id
    
    def getProp(self,purn):
        return self.properties.get(purn,None)
    def setProp(self,purn,val):
        self.properties[purn]=val

    def __str__(self):
        return f'{EntityURN.Name(self.urn)}({self.id})'

    def __repr__(self):
        s= f'{self!s}\n'
        for p in self.properties:
            pstr=str.replace(f'{self.properties[p]}','\n',', ')
            s+=f'\t {pstr}\n'
        return s