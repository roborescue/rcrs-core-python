from messages.AKAcknowledge import AKAcknowledge
from messages.AKCommand import AKCommand
from messages.KAConnectOK import KAConnectOK
from messages.KAConnectError import KAConnectError
from messages.KASense import KASense
from messages.AKConnect import AKConnect
from messages.AKCommand import AKCommand
from commands.AKSubscribe import AKSubscribe
import queue
from worldmodel.worldmodel import WorldModel
import random
import sys
from log.logger import Logger

from messages.controlMessageFactory import ControlMessageFactory



class Agent:

    def __init__(self):
        print('agent created .... ')
        #self.connection_send_msg = None
        self.name = ''
        self.connect_request_id = None
        self.world_model = WorldModel()
        self.config = None
        self.random = None
        self.agent_id = None
        self.queue = queue.Queue()

    def get_name(self):
        return self.name

    def set_send_msg(self, connection_send_func):
        self.send_msg = connection_send_func

    def start_up(self, request_id):

        ak_connect = AKConnect()
        self.send_msg(ak_connect.prepare_message(request_id, self))

    def test_sucsses(self):
        return self.queue.get()

    def message_received(self, msg):
        c_msg = ControlMessageFactory().make_message(msg)
        
        if isinstance(c_msg, KASense):
            self.process_sense(c_msg)
        elif isinstance(c_msg, KAConnectOK):
            self.handle_connect_ok(c_msg)
        elif isinstance(c_msg, KAConnectError):
            self.handle_connect_error(c_msg)

    def handle_connect_error(self, msg):
        Log = Logger(self.get_name())
        Log.warning( 'failed {0} : {1}'.format(msg.request_id, msg.reason) )
        self.queue.put(False)
        sys.exit(1)

    def handle_connect_ok(self, msg):
        self.agent_id = msg.agent_id
        self.world_model.add_entities(msg.world)
        self.config = msg.config

        self.sendAKAcknowledge(msg.request_id)

        self.queue.put(True)


    def sendAKAcknowledge(self, request_id):
        ak_ack = AKAcknowledge()
        self.send_msg(ak_ack.prepare_message(request_id, self.agent_id))

    def get_position(self):
        return self.world_model.get_entity(self.agent_id).get_position()

    def process_sense(self, msg):

        _id = msg.agent_id
        time = msg.time
        change_set = msg.change_set
        hear = msg.hear

        self.world_model.merge(change_set)
        self.think(time, change_set, hear)

    def random_walk(self):
        # calculate 10 step path
        path = []
        start_pos = self.get_position()
        for i in range(50):
            edges = self.world_model.get_entity(start_pos).get_edges()
            neighbors = []
            for edge in edges:
                if edge.get_neighbour() is not None:
                    neighbors.append(edge.get_neighbour())
            if neighbors:
                next = random.choice(neighbors)
                path.append(next)
                start_pos = next
            start_pos = self.get_position()

        return path

    def send_subscribe(self, time, channel):
        akcommand = AKCommand()
        akcommand.add_command(AKSubscribe(self.agent_id(), time, channel))

        self.send_msg(akcommand)
