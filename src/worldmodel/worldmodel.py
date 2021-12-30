from entities.entity import Entity
from entities.standardEntityFactory import StandardEntityFactory
from entities.human import Human
from entities.area import Area
from entities.blockade import Blockade
from connection import URN

from rtree import index
import sys

from worldmodel.changeSet import ChangeSet

class WorldModel:
    def __init__(self) -> None:

        self.index = index.Index()

        self.stored_types = {}
        self.unindexedـentities = {}
        self.human_rectangles = {}
        self.indexed = False
        self.minx = None
        self.miny = None
        self.maxx = None
        self.maxy = None
        self.num = 0

    def add_entities(self, entities):
        for entity in entities:
            self.unindexedـentities[entity.entity_id] = entity
        print(len(entities), ' entities added to world_model')

    def get_entity(self, entity_id: int) -> Entity:
        if entity_id in self.unindexedـentities:
            return self.unindexedـentities.get(entity_id)
        return None

    def add_entity(self, entity):
        self.unindexedـentities[entity.entity_id] = entity

    def remove_entity(self, entity_id):
        del self.unindexedـentities[entity_id]

    def get_entities(self):
        return self.unindexedـentities.values()

    def merge(self, change_set: ChangeSet):
        for entity_id in change_set.get_changed_entities():
            existing_entity = self.get_entity(entity_id)
            added = False
            if existing_entity is None:
                existing_entity = StandardEntityFactory.make_entity(
                    change_set.get_entity_urn(entity_id), entity_id)
                if existing_entity is None:
                    print('world model merge existing entity is still None')
                    continue
                added = True

            for property in change_set.get_changed_properties(entity_id):
                existing_property = existing_entity.get_property(property.urn)
                existing_property.take_value(property)

            if added:
                self.add_entity(existing_entity)

        for entity_id in change_set.get_deleted_entities():
            self.remove_entity(entity_id)

        # update human rectangles
        # new_human_rectangles_to_push = {}
        # for human, rectangle in self.human_rectangles.iteritems():
        #     self.index.delete(human.entity_id, rectangle)
        #     left, bottom, right, top = self.make_rectangle(human)
        #     if left is not None:
        #         self.index.insert(human.entity_id,
        #                           (left, bottom, right, top))
        #         new_human_rectangles_to_push[human] = (
        #             left, bottom, right, top)

        # for human, rectangle in new_human_rectangles_to_push:
        #     self.human_rectangles[human] = rectangle

    def index_entities(self):
        if not self.indexed:
            self.minx = float('inf')
            self.miny = float('inf')
            self.maxx = float('inf')
            self.maxy = float('inf')

            self.index = index.Index()
            self.human_rectangles.clear()

            for entity in self.unindexedـentities.values():
                left, bottom, right, top = self.make_rectangle(entity)
                if left is not None:
                    self.index.insert(entity.entity_id,
                                      (left, bottom, right, top))
                    self.minx = min(self.minx, left, right)
                    self.maxx = max(self.maxx, left, right)
                    self.miny = min(self.miny, bottom, top)
                    self.maxy = max(self.maxy, bottom, top)
                    if isinstance(entity, Human):
                        self.human_rectangles[entity] = (
                            left, bottom, right, top)
            self.indexed = True

    def make_rectangle(self, entity):
        x1 = x2 = y1 = y2 = float('inf')
        apexes = None
        
        if isinstance(entity, Area):
            apexes = entity.get_apexes()    
        elif isinstance(entity, Blockade):
            apexes = entity.get_apexes()
        # elif isinstance(entity, Human):
        #     apexes = []
        #     human_x, human_y = entity.get_location(self)
        #    apexes.append(human_x)
        #    apexes.append(human_y)
        else:
            return None, None, None, None

        if len(apexes) == 0:
            print('this area, blockade or human entity does not have apexes!!')
            return None
        print('len of apexes = ' + str(len(apexes)))
        for i in range(0, len(apexes), 2):
            print('i = '+str(i))
            print(str(apexes[i]))
            print(str(apexes[i+1]))
            x1 = min(x1, apexes[i])
            x2 = max(x2, apexes[i])
            y1 = min(y1, apexes[i+1])
            y2 = max(y2, apexes[i+1])
        return x1, y1, x2, y2

    # returns rect(x, y, w, h)
    def get_rect_bounds(self):
        if self.indexed == False:
            self.index_entities()

        return self.minX, self.minY, self.maxX - self.minX, self.maxY - self.minY

    # returns minX, minY, maxX, maxY
    def get_world_bounds(self):
        if self.indexed == False:
            self.index_entities()

        return self.minX, self.minY, self.maxX, self.maxY

    # TODO
    def get_objects_in_rectangle(self, x1, y1, x2, y2):
        if self.indexed == False:
            self.index_entities()

        return None

    def get_objects_in_range(self, x, y, range):
        if self.indexed == False:
            self.index_entities()

        return self.get_objects_in_rectangle(x - range, y - range, x + range, y + range)