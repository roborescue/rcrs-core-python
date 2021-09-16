import core.RCRSProto_pb2 as RCRSProto_pb2
from world.Entity import Entity
class WorldModel:
    visibleEntities={}
    
    def __init__(self):
        self._entitiesById={}
        self._entitiesByType={}
        pass
    def addEntitiesProto(self,entities):
        for e in entities:
            entity=Entity(e.urn,e.entityID)
            for p in e.properties:
                entity.setProp(p.urn, p)
            self.addEntity(entity)

    def addEntity(self,entity):
        self._entitiesById[entity.id]=entity
        if not(entity.urn in self._entitiesByType):
            self._entitiesByType[entity.urn]=[]
        self._entitiesByType[entity.urn].append(entity)

    def removeEntity(self,entityID):
        if entityID in self._entitiesById:
            entity=self._entitiesById[entityID]
            for i,e in enumerate(self.entitiesByType[entity.urn]):
                if(e.entityID==entity.entityID):
                    del self._entitiesByType[entity.urn][i]
            del self._entitiesById[entityID]
    
    def merge(self,changeSet):
        self.visibleEntities.clear()
        for change in changeSet.changes:
            entity=self.get(change.entityID)
            if(entity==None):
                entity=Entity(change.urn,change.entityID)
                self.addEntity(entity)
            self.visibleEntities[entity.id]=(entity);
            for p in change.properties:
                entity.setProp(p.urn,p)

        for entityID in changeSet.deletes :
            self.removeEntity(entityID)
    
    def get(self,entityID):
        return self._entitiesById.get(entityID,None)

    def getTypes(self, urns):
        if not isinstance(urns, list):
            urns=[urns]
        out=[]
        for urn in urns:
            out+=self._entitiesByType[urn]
        return out
