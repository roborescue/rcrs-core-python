from messages.KASense import KASense
from messages.KAConnectOK import KAConnectOK
from messages.KAConnectError import KAConnectError
from connection import URN


class ControlMessageFactory:
    def __init__(self) -> None:
        pass

    def make_message(self, msg):
        if msg.urn == URN.ControlMSG.KA_SENSE:
            return KASense(msg)
        elif msg.urn == URN.ControlMSG.KA_CONNECT_OK:
            return KAConnectOK(msg)
        elif msg.urn == URN.ControlMSG.KA_CONNECT_ERROR:
            return KAConnectError(msg)

        return None
