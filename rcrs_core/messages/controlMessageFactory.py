from rcrs_core.messages.KASense import KASense
from rcrs_core.messages.KAConnectOK import KAConnectOK
from rcrs_core.messages.KAConnectError import KAConnectError
from rcrs_core.messages.Shutdown import Shutdown
from rcrs_core.connection import URN


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
        elif msg.urn == URN.ControlMSG.SHUTDOWN:
            return Shutdown(msg)

        return None
