from core.Agent import Agent
from core.RCRSProto_pb2 import EntityURN
from core.RCRSProto_pb2 import PropertyURN
class Civilian(Agent):
    def __init__(self):
        pass
    #override
    def name(self):
        return "PythonCivilian"

    #override
    def requestedEntityTypes(self):
        return [EntityURN.CIVILIAN,EntityURN.AMBULANCE_TEAM,EntityURN.POLICE_FORCE,EntityURN.FIRE_BRIGADE]
        
    
    #override
    async def precompute(self):
        print(f'precompute finshed')
        pass

    #override
    async def think(self,time,changeSet,hear):
        print(f'thinking time={time}')
        #sample get entity:
        myentity=self.world.get(self.id)
        print(f'I am {myentity!s}')
        #sample get property:
        p=myentity.getProp(PropertyURN.HP)
        if(p.defined):
            hp=p.intValue
            print(f'my hp is: {hp} my entity is: {myentity!r}')
        else:
            print(f'my hp is undifined my entity id is: {myentity.id}')
        # sample get All Buildings
        buildings=self.world.getTypes(EntityURN.BUILDING)
        road_buidling=self.world.getTypes([EntityURN.BUILDING,EntityURN.ROAD])
        print(f'building size={len(buildings)} building_road size={len(road_buidling)}')
        print(f'visible entities= {self.world.visibleEntities.keys()}')
        await self.rest(time)
        pass