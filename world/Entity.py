import core.urn as urn
class Entity:
    
    def __init__(self,urn,id):
        self.properties={}
        self.urn=urn
        self.id=id
    
    def getURN(self):
        return self.urn
    def getID(self):
        return self.id
    
    def getProp(self,property_urn):
        return self.properties.get(property_urn,None)
    
    def __getitem__(self,property_urn):
        return self.getProp(property_urn)
    def setProp(self,purn,val):
        self.properties[purn]=val

    
    def __str__(self):
        return f'{self.urn.name}({self.id})'

    def __repr__(self):
        s= f'{self!s}\n'
        for p in self.properties:
            pstr=str.replace(f'{self.properties[p]}','\n',', ')
            s+=f'\t {p.name}= {pstr}\n'
        return s