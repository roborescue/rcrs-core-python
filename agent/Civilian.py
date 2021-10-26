from core.Agent import Agent
import core.URN as URN
class Civilian(Agent):
    def __init__(self):
        pass
    #override
    def name(self):
        return "PythonCivilian"

    #override
    def requestedEntityTypes(self):
        return [URN.Entity.CIVILIAN,URN.Entity.AMBULANCE_TEAM,URN.Entity.POLICE_FORCE,URN.Entity.FIRE_BRIGADE]
        
    
    #override
    def precompute(self):
        print(f'precompute finshed')
        pass

    #override
    def think(self,time,changeSet,hear,overtime):
        print(f'thinking time={time} overtime={overtime}')
        #sample get entity:
        myentity=self.world[self.id] # euvalent > myentity=self.world.get(self.id)
        print(f'I am {myentity!s}')
        #sample get property:
        hp=myentity[URN.Property.HP] #equvalent> hp=myentity.getProp(urn.Property.HP)
        
        
        myentity.get_position()
        
        human[URN.Property.EDGES]

        if not hp:
            print(f'my hp is: {hp} my entity is: {myentity!r}')
        else:
            print(f'my hp is undefined my entity id is: {myentity.id}')
            
            
        # sample get All Buildings
        buildings=self.world.getTypes(URN.Entity.BUILDING)
        road_buidling=self.world.getTypes([URN.Entity.BUILDING,URN.Entity.ROAD])
        print(f'building size={len(buildings)} building_road size={len(road_buidling)}')
        print(f'visible entities= {[f"{e!s}" for e in self.world.visibleEntities.values()]}')
        # import time
        # time.sleep(3)
        return self.rest(time)