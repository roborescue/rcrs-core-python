import rcrs_encoding_utils
from WorldModel import WorldModel
from abc import ABC, abstractmethod
import asyncio
import ControlMessageProto_pb2
class Agent(ABC):
    def __init__(self):
        pass

    # @abstractmethod
    def name(self):
        return "PythonAgent-None"

    # @abstractmethod
    def requestedEntityTypes(self):
        return ['urn:rescuecore2.standard:entity:civilian']
        
    
    # @abstractmethod
    async def precompute(self):
        pass

    # @abstractmethod
    async def think(self,time,changeSet,hear):
        pass

    async def connect(self,host,port):
        reader, writer = await asyncio.open_connection(host, port)
        self.reader=reader
        self.writer=writer
        await self.sendAKConnect(requestId=1)
        await self.parseMessageFromKernel()

    async def messageReceived(self,msg):
        if(msg.urn=="urn:rescuecore2:messages.control:ka_sense"):
            await self.handleKASense(msg)
        elif(msg.urn=="urn:rescuecore2:messages.control:ka_connect_ok"):
            await self.handleKAConnectOk(msg)
        elif (msg.urn=="urn:rescuecore2:messages.control:ka_connect_error"):
            await self.handleKAConnectError(msg)
    
    async def handleKASense(self,msg):
        agentId=msg.components["Agent ID"].entityID
        time=msg.components['Time'].intValue
        changeSet=msg.components['Updates'].changeSet
        hear=msg.components['Hearing'].commandList
        if(self.id!=agentId):
            print(f'ERRROR this should not never happen agentid={self.id} but receive a sense for {agentId}')
        self.world.merge(changeSet)
        await self.think(time,changeSet,hear)


    async def handleKAConnectOk(self,msg):
        entities=msg.components["Entities"].entityList.entities
        self.world=WorldModel()
        self.world.addEntities(entities)
        requestId=msg.components['Request ID'].intValue
        self.id=msg.components["Agent ID"].entityID
        self.config=msg.components["Agent config"].config
        await self.precompute()
        await self.sendAKAcknowledge(requestId)


    async def handleKAConnectError(self,msg):
        requestId=msg.components['Request ID'].intValue
        reason=msg.components['Reason'].stringValue
        print(f'Connect Error reason={reason} requestId={requestId}')
        self.writer.close()
        await self.writer.wait_closed()
        import sys
        sys.exit()

    async def sendAKConnect(self,requestId):
        msg=ControlMessageProto_pb2.MessageProto()
        msg.urn="urn:rescuecore2:messages.control:ak_connect"
        msg.components['Request ID'].intValue=requestId
        msg.components['Version'].intValue=1
        msg.components['Name'].stringValue=self.name()
        for urn in self.requestedEntityTypes():
            msg.components['Requested entity types'].stringList.values.append(urn)
        await rcrs_encoding_utils.write_msg(msg,self.writer)

    async def sendAKAcknowledge(self,requestId):
        msg=ControlMessageProto_pb2.MessageProto()
        msg.urn="urn:rescuecore2:messages.control:ak_acknowledge"
        msg.components['Request ID'].intValue=requestId
        msg.components['Agent ID'].entityID=self.id
        await rcrs_encoding_utils.write_msg(msg,self.writer)

    async def parseMessageFromKernel(self):
            while 1:
                msg=await rcrs_encoding_utils.read_msg(self.reader)
                print(msg)
                await self.messageReceived(msg)

    

####################################commands
    async def sendAKRest(self,time):
        msg=ControlMessageProto_pb2.MessageProto()
        msg.urn="urn:rescuecore2.standard:message:rest"
        msg.components['Agent ID'].entityID=self.id
        msg.components['Time'].intValue=time
        await rcrs_encoding_utils.write_msg(msg,self.writer)
