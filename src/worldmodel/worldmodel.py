from entities.entity import Entity
from entities.standardEntityFactory import StandardEntityFactory
from entities.human import Human
from entities.area import Area
from entities.blockade import Blockade


from rtree import index
import sys


class WorldModel:
    def __init__(self) -> None:
        #print(agent_name, ': world model created')

        self.index = index.Index()

        self.stored_types = {}
        self.unindexedـetities = {}
        self.human_rectangles = {}
        self.indexed = False
        self.minx = None
        self.miny = None
        self.maxx = None
        self.maxy = None
        self.num = 0

    def add_entities(self, entities):
        for entity in entities:
            self.unindexedـetities[entity.get_id()] = entity
        print(len(entities), ' entities added to world_model')

    def get_entity(self, entity_id) -> Entity:
        if entity_id in self.unindexedـetities:
            return self.unindexedـetities.get(entity_id)
    
        return None

    def add_entity(self, entity):
        self.unindexedـetities[entity.get_id()] = entity

    def remove_entity(self, entity_id):
        del self.unindexedـetities[entity_id]

    def get_entities(self):
        return self.unindexedـetities.values()

    def merge(self, change_set):
        for entity_id in change_set.get_changed_entities():
            existing_entity = self.get_entity(entity_id)
            added = False
            if existing_entity is None:
                existing_entity = StandardEntityFactory.make_entity(
                    change_set.get_entity_urn(entity_id), entity_id.get_value())
                if existing_entity is None:
                    print('world model merge existing entity is still None')
                    continue
                added = True

            for property in change_set.get_changed_properties(entity_id):
                existing_property = existing_entity.get_property(property.get_urn())
                existing_property.take_value(property)

            if added:
                self.add_entity(existing_entity)

        for entity_id in change_set.get_deleted_entities():
            self.remove_entity(entity_id)

        # update human rectangles
        # new_human_rectangles_to_push = {}
        # for human, rectangle in self.human_rectangles.iteritems():
        #     self.index.delete(human.get_id().get_value(), rectangle)
        #     left, bottom, right, top = self.make_rectangle(human)
        #     if left is not None:
        #         self.index.insert(human.get_id().get_value(),
        #                           (left, bottom, right, top))
        #         new_human_rectangles_to_push[human] = (
        #             left, bottom, right, top)

        # for human, rectangle in new_human_rectangles_to_push:
        #     self.human_rectangles[human] = rectangle

    # def index(self):
    #     if not self.indexed:
    #         self.minx = sys.maxint
    #         self.miny = sys.maxint
    #         self.maxx = sys.minint
    #         self.maxy = sys.minint

    #         self.index = index.Index()
    #         self.human_rectangles.clear()

    #         for entity in self.unindexedـetities.values():
    #             left, bottom, right, top = self.make_rectangle(entity)
    #             if left is not None:
    #                 self.index.insert(entity.get_id().get_value(),
    #                                   (left, bottom, right, top))
    #                 self.minx = min(self.minx, left, right)
    #                 self.maxx = max(self.maxx, left, right)
    #                 self.miny = min(self.miny, bottom, top)
    #                 self.maxy = max(self.maxy, bottom, top)
    #                 if isinstance(entity, Human):
    #                     self.human_rectangles[entity] = (
    #                         left, bottom, right, top)
    #         self.indexed = True

    # def make_rectangle(self, entity):
    #     x1 = sys.maxint
    #     x2 = sys.minint
    #     y1 = sys.maxint
    #     y2 = sys.minint
    #     apexes = None
    #     if isinstance(entity, Area):
    #         apexes = entity.get_apexes()
    #     elif isinstance(entity, Blockade):
    #         apexes = entity.get_apexes()
    #     elif isinstance(entity, Human):
    #         apexes = []
    #         human_x, human_y = entity.get_location(self)
    #         apexes.append(human_x)
    #         apexes.append(human_y)
    #     else:
    #         return None, None, None, None

    #     if len(apexes) == 0:
    #         print('this area, blockade or human entity does not have apexes!!')
    #         return None
    #     for i in range(0, len(apexes), 2):
    #         x1 = min(x1, apexes[i])
    #         x2 = max(x2, apexes[i])
    #         y1 = min(y1, apexes[i+1])
    #         y2 = max(y2, apexes[i+1])
    #     return x1, y1, x2, y2
