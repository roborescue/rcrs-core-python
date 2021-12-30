from connection import URN
from entities.building import Building
from entities.standardEntityURN import StandardEntityURN
from properties.standardPropertyURN import StandardPropertyURN
from properties.intProperty import IntProperty


class Refuge(Building):
    urn = StandardEntityURN.REFUGE.value

    def __init__(self, entity_id):
        super().__init__(entity_id)
        self.bed_capacity = IntProperty(URN.Property.BEDCAPACITY)
        self.occupied_beds = IntProperty(URN.Property.OCCUPIEDBEDS)
        self.refill_capacity = IntProperty(URN.Property.REFILLCAPACITY)
        self.waiting_list_size = IntProperty(URN.Property.WAITINGLISTSIZE)

    def set_entity(self, properties):

        super().set_entity(properties)

        for key, values in properties.items():
            if key == URN.Property.BEDCAPACITY:
                self.bed_capacity.set_value(values)

            elif key == URN.Property.OCCUPIEDBEDS:
                self.occupied_beds.set_value(values)

            elif key == URN.Property.REFILLCAPACITY:
                self.refill_capacity.set_value(values)

            elif key == URN.Property.WAITINGLISTSIZE:
                self.waiting_list_size.set_value(values)

            self.register_properties([self.bed_capacity, self.occupied_beds])
            self.register_properties(
                [self.refill_capacity, self.waiting_list_size])

    def get_entity_name(self) -> str:
        return "Refuge"

    def get_property(self, urn):

        if(urn == URN.Property.BEDCAPACITY):
            return self.bed_capacity
        elif(urn == URN.Property.OCCUPIEDBEDS):
            return self.occupied_beds
        elif(urn == URN.Property.REFILLCAPACITY):
            return self.refill_capacity
        elif(urn == URN.Property.WAITINGLISTSIZE):
            return self.waiting_list_size
        else:
            return super().get_property(urn)