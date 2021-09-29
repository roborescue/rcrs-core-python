from agents.agent import Agent
from messages.AKCommand import AKCommand
from commands.AKMove import AKMove
from log.logger import Logger


class AmbulanceTeamAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        self.name = 'AmbulanceTeamAgent'

    def get_requested_entities(self):
        return 'entity:ambulanceteam'
    
    def post_connect(self, world, agent_id):
        self.Log = Logger(self.get_name(), self.get_id())

    def think(self, time, change_set, heard):
        self.Log.info(time)

        path = self.random_walk()
        cmd = AKMove(self.get_id(), time, path)

        akcommand = AKCommand()
        akcommand.add_command(cmd)

        self.send_msg(akcommand)
