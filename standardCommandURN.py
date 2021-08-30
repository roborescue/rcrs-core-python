from enum import Enum
from constants import COMMAND_URN_PREFIX

class StandardCommandURN(Enum):
    # Rest command. 
    AK_REST = COMMAND_URN_PREFIX + "rest" 
    # Move command. 
    AK_MOVE = COMMAND_URN_PREFIX + "move" 
    # Load command. 
    AK_LOAD = COMMAND_URN_PREFIX + "load" 
    # Unload command. 
    AK_UNLOAD = COMMAND_URN_PREFIX + "unload" 
    # Say command. 
    AK_SAY = COMMAND_URN_PREFIX + "say" 
    # Tell command. 
    AK_TELL = COMMAND_URN_PREFIX + "tell" 
    # Extinguish command. 
    AK_EXTINGUISH = COMMAND_URN_PREFIX + "extinguish" 
    # Rescue command. 
    AK_RESCUE = COMMAND_URN_PREFIX + "rescue" 
    # Clear command. 
    AK_CLEAR = COMMAND_URN_PREFIX + "clear" 
    # Clear-Area command. 
    AK_CLEAR_AREA = COMMAND_URN_PREFIX + "clear_area" 
    # Channel subscribe command. 
    AK_SUBSCRIBE = COMMAND_URN_PREFIX + "subscribe" 
    # Channel speak command. 
    AK_SPEAK = COMMAND_URN_PREFIX + "speak" 

    def from_id(index):
        return list(StandardCommandURN)[index].value
    
    def from_string(urn):
        for key in StandardCommandURN:
            if key.name == urn:
                return key.value
        return ''