from messages.message import Message
from connection import URN, RCRSProto_pb2


class Shutdown(Message):
    def __init__(self, data) -> None:
        super().__init__(URN.ControlMSG.SHUTDOWN)

    def read(self):
        pass

    def write(self):
        pass
