import random
import sys
from connection.URN import Entity
from commands.AKSubscribe import AKSubscribe
from commands.AKClear import AKClear
from commands.AKClearArea import AKClearArea
from commands.AKLoad import AKLoad
from commands.AKMove import AKMove
from commands.AKRescue import AKRescue
from commands.AKUnload import AKUnload
from commands.AKSay import AKSay
from commands.AKSpeak import AKSpeak
from commands.AKTell import AKTell

from messages.AKAcknowledge import AKAcknowledge
from messages.KAConnectOK import KAConnectOK
from messages.KAConnectError import KAConnectError
from messages.KASense import KASense
from messages.AKConnect import AKConnect
from worldmodel.worldmodel import WorldModel
from log.logger import Logger
from messages.controlMessageFactory import ControlMessageFactory
from abc import ABC, abstractmethod

from commands.AKRest import AKRest
from entities.human import Human


class Agent(ABC):

    def __init__(self, pre):
        print('agent created .... ')
        self.name = 'Abstract_Agent'
        self.connect_request_id = None
        self.world_model = WorldModel()
        self.config = None
        self.random = None
        self.agent_id = None
        self.precompute_flag = pre
    
    @abstractmethod
    def precompute(self):
        pass
    
    @abstractmethod
    def think(self, time, change_set, hear):
        pass

    def get_name(self):
        return self.name

    def get_id(self):
        return self.agent_id

    def set_send_msg(self, connection_send_func):
        self.send_msg = connection_send_func

    def start_up(self, request_id):
        ak_connect = AKConnect()
        self.send_msg(ak_connect.write(request_id, self))
    
    def post_connect(self):
        self.Log = Logger(self.get_name(), self.get_id())

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
        Log.warning('failed {0} : {1}'.format(msg.request_id, msg.reason))
        sys.exit(1)

    def handle_connect_ok(self, msg):
        self.agent_id = msg.agent_id
        self.world_model.add_entities(msg.world)
        self.config = msg.config
        self.sendAKAcknowledge(msg.request_id)
        self.post_connect()
        if self.precompute_flag:
            print('self.precompute_flag: ', self.precompute_flag)
            self.precompute()

    def sendAKAcknowledge(self, request_id):
        ak_ack = AKAcknowledge()
        self.send_msg(ak_ack.write(request_id, self.agent_id))

    def process_sense(self, msg):
        _id = msg.agent_id
        time = msg.time
        change_set = msg.change_set
        hear = msg.hear

        if _id != self.get_id():
            self.Log.warning('agent recieved a message which not blongs to him')
            return

        self.world_model.merge(change_set)
        self.think(time, change_set, hear)

    def me(self) -> Human:
        return self.world_model.get_entity(self.get_id())

    def location(self) -> Entity:
        return self.world_model.get_entity(self.me().position.value)

    def random_walk(self):
        path = []
        seen = set()
        current = self.location().get_id()
        for _ in range(10):
            path.append(current)
            seen.add(current)
            rd = self.world_model.get_entity(current)
            if not rd:
                break
            edges = rd.edges.value
            neighbors = []
            for edge in edges:
                if edge.get_neighbour() is not None:
                    neighbors.append(edge.get_neighbour())
            random.shuffle(neighbors)
            found = False
            for e in neighbors:
                if e in seen:
                    continue
                current = e
                found = True
                break
            if not found:
                break
        return path[0:-1]

    def send_clear(self, time, target):
        cmd = AKClear(self.get_id(), time, target)
        msg = cmd.prepare_cmd()
        self.send_msg(msg)

    def send_clear_area(self, time, x=-1, y=-1):
        cmd = AKClearArea(self.get_id(), time, x, y)
        msg = cmd.prepare_cmd()
        self.send_msg(msg)
    
    def send_load(self, time, target):
        cmd = AKLoad(self.get_id(), time, target)
        msg = cmd.prepare_cmd()
        self.send_msg(msg)

    def send_move(self, time, path, x=-1, y=-1):
        cmd = AKMove(self.get_id(), time, path[:], x, y)
        msg = cmd.prepare_cmd()
        self.send_msg(msg)

    def send_rescue(self, time, target):
        cmd = AKRescue(self.get_id(), time, target)
        msg = cmd.prepare_cmd()
        self.send_msg(msg)

    def send_rest(self, time_step):
        cmd = AKRest(self.get_id(), time_step)
        msg = cmd.prepare_cmd()
        self.send_msg(msg)

    def send_say(self, time_step: int, message: str):
        cmd = AKSay(self.get_id(), time_step, message)
        msg = cmd.prepare_cmd()
        self.send_msg(msg)
    
    def send_speak(self, time_step: int, message: str, channel: int):
        cmd = AKSpeak(self.get_id(), time_step, message, channel)
        msg = cmd.prepare_cmd()
        self.send_msg(msg)

    def send_subscribe(self, time, channel):
        cmd = AKSubscribe(self.get_id(), time, channel)
        msg = cmd.prepare_cmd()
        self.send_msg(msg)
    
    def send_tell(self, time_step: int, message: str):
        cmd = AKTell(self.get_id(), time_step, message)
        msg = cmd.prepare_cmd()
        self.send_msg(msg)
    
    def send_unload(self, time):
        cmd = AKUnload(self.get_id(), time)
        msg = cmd.prepare_cmd()
        self.send_msg(msg)
    
