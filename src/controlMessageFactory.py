from message import *
from controlMessageURN import ControlMessageURN

class ControlMessageFactory:
    def __init__(self) -> None:
        pass

    def make_message( urn, data ):
        if urn == ControlMessageURN.AK_CONNECT.value:
            return AKConnect( data )
        if urn == ControlMessageURN.AK_ACKNOWLEDGE.value:
            return AKAcknowledge( data )
        if urn ==  ControlMessageURN.KA_SENSE.value:
            return KASense( data )
        if urn == ControlMessageURN.AK_COMMAND.value:
            return AKCommand( data )
        if urn == ControlMessageURN.KA_CONNECT_OK.value:
            return KAConnectOK( data )
        if urn ==  ControlMessageURN.KA_CONNECT_ERROR.value:
            return KAConnectError( data )
        if urn ==  ControlMessageURN.SHUTDOWN.value:
            return Shutdown( data )
        
            