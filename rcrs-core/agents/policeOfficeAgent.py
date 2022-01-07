from agents.agent import Agent
from log.logger import Logger
from connection import URN


class PoliceOfficeAgent(Agent):
    def __init__(self, pre):
        Agent.__init__(self, pre)
        self.name = 'PoliceOfficeAgent'
    
    def get_requested_entities(self):
        return [URN.Entity.POLICE_OFFICE]

    def think(self, timestep, change_set, heard):
        pass
