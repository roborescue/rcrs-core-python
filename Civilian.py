from Agent import Agent
import URN
class Civilian(Agent):
    def __init__(self):
        pass
    #override
    def name(self):
        return "PythonCivilian"

    #override
    def requestedEntityTypes(self):
        return [URN.CIVILIAN]
        
    
    #override
    async def precompute(self):
        print(f'precompute finshed')
        pass

    #override
    async def think(self,time,changeSet,hear):
        print(f'thinking time={time}')
        #sample get entity:
        myentity=self.world.get(self.id)
        #sample get property:
        hp=myentity.properties[URN.HP].value.intValue
        print(f'my hp is: {hp} my entity id is: {myentity.entityID}')
        # sample get All Buildings
        buildings=self.world.getTypes(URN.BUILDING)
        road_buidling=self.world.getTypes([URN.BUILDING,URN.ROAD])
        print(f'building size={len(buildings)} building_road size={len(road_buidling)}')
        await self.rest(time)
        pass