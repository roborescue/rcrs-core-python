from agents.agent import Agent


class FireStationAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'rescue_agent.FireStationAgent'

    def get_requested_entities(self):
        return 'entity:firestation'

    def think(self, timestep, change_set, heard):
        print(f'FireStationAgent({self.get_id()}): think method. timestep = ', timestep)
