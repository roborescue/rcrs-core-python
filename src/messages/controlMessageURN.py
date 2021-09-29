from enum import Enum


class ControlMessageURN(Enum):
    # Agent-Kernel connect.
    AK_CONNECT = "message:ak_connect"

    # Agent-Kernel acknowledge.
    AK_ACKNOWLEDGE = "message:ak_acknowledge"

    # Agent-Kernel command.
    AK_COMMAND = "message:ak_command"

    # Kernel-Agent OK.
    KA_CONNECT_OK = "message:ka_connect_ok"

    # Kernel-Agent error.
    KA_CONNECT_ERROR = "message:ka_connect_error"
    
    # Kernel-Agent perception update.
    KA_SENSE = "message:ka_sense"

    # Shutdown message.
    SHUTDOWN = "message:shutdown"

    # New EntityID request.
    ENTITY_ID_REQUEST = "message:entity_id_request" 

    # New EntityID response.
    ENTITY_ID_RESPONSE =  "message:entity_id_response" 

