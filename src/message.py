
#from encoding_tool import read_int32
from commands.Command import Command
from standardPropertyFactory import StandardPropertyFactory
from changeSet import ChangeSet
from standardEntityFactory import StandardEntityFactory
from config import Config
import ControlMessageProto_pb2 as protoBuf
import random
from standardEntityURN import StandardEntityURN
from standardPropertyURN import StandardPropertyURN
from config import Config
from controlMessageURN import ControlMessageURN
from property import EntityIDProperty
from entityID import EntityID

class Message:
    def __init__(self) -> None:
        #self.urn = ''
        #self.message = b''
        pass
    
    
    def read(self, inputStream):
        pass

    def get_urn(self):
        return self.urn

class AKConnect(Message):
    
    def __init__(self, agent):
        super().__init__()
        self.urn = ControlMessageURN.AK_CONNECT.value
        self.requestID = random.randint(1,100)
        self.agentName = agent.agentName()
        self.requestedEntityTypes = agent.get_requested_entities()
        self.message = self.write()

        print('request id === ', self.requestID )
    
    def write(self):
        akConnect = protoBuf.AKConnectProto()
        akConnect.requestID = self.requestID 
        akConnect.version = 1
        akConnect.agentName = self.agentName
        akConnect.requestedEntityTypes.append(self.requestedEntityTypes)
        return akConnect.SerializeToString()
    
    def read(self, inputStream):
        pass

class AKAcknowledge(Message):
    
    def __init__(self, request_id, agent_id):
        self.urn = ControlMessageURN.AK_ACKNOWLEDGE.value
        self.requestID = request_id
        self.agentId = agent_id
        self.message = self.write()

    def write(self):
        akAck = protoBuf.AKAcknowledgeProto()
        akAck.requestID = self.requestID
        akAck.agentID = self.agentId
        return akAck.SerializeToString()

class KAConnectOK(Message):

    def __init__(self, data):
        self.urn = ControlMessageURN.KA_CONNECT_OK.value
        
        self.data = bytes(data)
        self.config = Config()
        self.world = []
        self.read()

    def read(self):
        kaConnectok = protoBuf.KAConnectOKProto()
        kaConnectok.ParseFromString(self.data)
        self.requestID = kaConnectok.requestID
        self.agentId = kaConnectok.agentID

        for entity_proto in kaConnectok.entities:
            entity = StandardEntityFactory.make_entity(StandardEntityURN.from_id(entity_proto.urnID), entity_proto.entityID)
            properties = {}
            for property_proto in entity_proto.properties:
                properties[StandardPropertyURN.from_id(property_proto.urnID)]= property_proto.fields
            
            entity.set_entity(properties)
            self.world.append(entity)

            
        for key, value in kaConnectok.config.data.items():
            self.config.setValue(key, value)
        
        
    def write(self):
        pass

class KAConnectError(Message):

    def __init__(self):
        Message.__init__(self)
        self.urn = ControlMessageURN.KA_CONNECT_ERROR.value

    def read(self):
        pass
    def write(self):
        pass


class KASense(Message):

    def __init__(self, _data):
       # Message.__init__(self)
        self.urn = ControlMessageURN.KA_SENSE.value
        self.agent_id = None
        self.time = None
        self.updates = None
        self.data = _data
        self.change_set = ChangeSet()
        self.hear = []
        self.read()

    def get_time(self):
        return self.time
    def get_change_set(self):
        return self.change_set
    def get_hearing(self):
        pass

    
    def read(self):
        kaSenseProto = protoBuf.KASenseProto()
        kaSenseProto.ParseFromString(self.data)
        
        self.agent_id = kaSenseProto.agentID
        self.time = kaSenseProto.time

        changes_map = kaSenseProto.changes.changes
        entities_urns = kaSenseProto.changes.entitiesURNs
        for entity_id_proto in changes_map.keys():
            entity_id = EntityID(entity_id_proto)
            urn = entities_urns.get(entity_id_proto)

            property_map_proto = changes_map.get(entity_id_proto)
            for property_urn in property_map_proto.property.keys():
                property = StandardPropertyFactory.make_property(property_urn)
                if property != None:
                    fields = property_map_proto.property.get(property_urn)
                    property.set_fields(fields)

                    self.change_set.add_change(entity_id, urn, property)


        for _entity_id in kaSenseProto.changes.deletes:
            self.change_set.entity_deleted(EntityID(_entity_id))
        
        for command_proto in kaSenseProto.hears:
            _urn = command_proto.urn
            _fields = command_proto.fields

            print(_urn, _fields)

            command = Command()
            command.set_urn(_urn)

    def write(self):
        pass

    def get_change_set(self):
        return self.change_set  

    def get_hearing(self):
        return self.hear

    def get_time(self):
        return self.time


class AKCommand(Message):
    def __init__(self):
        Message.__init__(self)
        self.urn = ControlMessageURN.AK_COMMAND.value



class Shutdown(Message):
    def __init__(self, data) -> None:
        super().__init__()
        self.urn = ControlMessageURN.SHUTDOWN.value