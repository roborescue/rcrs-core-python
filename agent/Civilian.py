from core.Agent import Agent
import core.urn as urn
class Civilian(Agent):
    def __init__(self):
        pass
    #override
    def name(self):
        return "PythonCivilian"

    #override
    def requestedEntityTypes(self):
        return [urn.Entity.CIVILIAN,urn.Entity.AMBULANCE_TEAM,urn.Entity.POLICE_FORCE,urn.Entity.FIRE_BRIGADE]
        
    
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
        hp=myentity.getProp(urn.Property.HP)
        if hp == None:
            print(f'my hp is undefined my entity id is: {myentity.id}')
        else:
            print(f'my hp is: {hp} my entity is: {myentity!r}')
            
        # sample get All Buildings
        buildings=self.world.getTypes(urn.Entity.BUILDING)
        road_buidling=self.world.getTypes([urn.Entity.BUILDING,urn.Entity.ROAD])
        print(f'building size={len(buildings)} building_road size={len(road_buidling)}')
        print(f'visible entities= {self.world.visibleEntities.keys()}')
        await self.rest(time)
        pass