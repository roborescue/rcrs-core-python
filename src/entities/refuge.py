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

    def copy_impl(self):
        return Refuge(self.get_id())

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

    # bed_capacity
    def get_bed_capacity_property(self):
        return self.bed_capacity

    def get_bed_capacity(self):
        return self.bed_capacity.get_value()

    def set_bed_capacity(self, value):
        self.bed_capacity.set_value(value)

    def is_bed_capacity_defined(self):
        return self.bed_capacity.is_defined()

    def undefine_bed_capacity(self):
        self.bed_capacity.set_undefined()

    # occupied_beds
    def get_occupied_beds_property(self):
        return self.occupied_beds

    def get_occupied_beds(self):
        return self.occupied_beds.get_value()

    def set_occupied_beds(self, value):
        self.occupied_beds.set_value(value)

    def is_occupied_beds_defined(self):
        return self.occupied_beds.is_defined()

    def undefine_occupied_beds(self):
        self.occupied_beds.set_undefined()

    # refill_capacity
    def get_refill_capacity_property(self):
        return self.refill_capacity

    def get_refill_capacity(self):
        return self.refill_capacity.get_value()

    def set_refill_capacity(self, value):
        self.refill_capacity.set_value(value)

    def is_refill_capacity_defined(self):
        return self.refill_capacity.is_defined()

    def undefine_refill_capacity(self):
        self.refill_capacity.set_undefined()

    # waiting_list_size
    def get_waiting_list_size_property(self):
        return self.waiting_list_size

    def get_waiting_list_size(self):
        return self.waiting_list_size.get_value()

    def set_waiting_list_size(self, value):
        self.waiting_list_size.set_value(value)

    def is_waiting_list_size_defined(self):
        return self.waiting_list_size.is_defined()

    def undefine_waiting_list_size(self):
        self.waiting_list_size.set_undefined()
