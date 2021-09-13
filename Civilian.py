from Agent import Agent
class Civilian(Agent):
    def __init__(self):
        pass
    #override
    def name(self):
        return "PythonCivilian"

    #override
    def requestedEntityTypes(self):
        return ['urn:rescuecore2.standard:entity:civilian']
        
    
    #override
    async def precompute(self):
        pass

    #override
    async def think(self,time,changeSet,hear):
        await self.sendAKRest(time)
        pass