from agents.agent import Agent


class FireBrigadeAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'rescue_agent.FireBrigadeAgent'

    def get_requested_entities(self):
        return 'entity:firebrigade'

    def think(self, timestep, change_set, heard):
        print(f'FireBrigadeAgent({self.get_id()}): think method. timestep = ', timestep)
