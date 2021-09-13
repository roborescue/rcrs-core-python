import ControlMessageProto_pb2
class WorldModel:
    entitiesById={}
    entitiesByType={}

    def __init__(self):
        pass
    def addEntities(self,entities):
        for entity in entities:
            self.addEntity(entity)

    def addEntity(self,entity):
        self.entitiesById[entity.entityID]=entity
        if not(entity.urn in self.entitiesByType):
            self.entitiesByType[entity.urn]=[]
        self.entitiesByType[entity.urn].append(entity)

    def removeEntity(self,entityID):
        if entityID in self.entitiesById:
            entity=self.entitiesById[entityID]
            for i,e in enumerate(self.entitiesByType[entity.urn]):
                if(e.entityID==entity.entityID):
                    del self.entitiesByType[entity.urn][i]
            del self.entitiesById[entityID]
    
    def merge(self,changeSet):
        for change in changeSet.changes:
            entity=self.entitiesById.get(change.entityID,None)
            if(entity==None):
                entity=ControlMessageProto_pb2.EntityProto()
                entity.urn=change.urn
                entity.entityID=change.entityID
                self.addEntity(entity)

            for p in change.properties:
                entity.properties[p.urn].CopyFrom(p)

        for entityID in changeSet.deletes :
            self.removeEntity(entityID)