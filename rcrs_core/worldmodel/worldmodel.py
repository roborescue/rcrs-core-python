from typing import List
from rcrs_core.entities.entity import Entity
from rcrs_core.entities import standardEntityFactory
from rcrs_core.entities import human
from rcrs_core.entities.area import Area
from rcrs_core.entities.blockade import Blockade
from rcrs_core.connection import URN

from rtree import index
import sys

from rcrs_core.worldmodel.changeSet import ChangeSet
from rcrs_core.worldmodel.entityID import EntityID


class WorldModel:
    def __init__(self) -> None:

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

    def add_entities(self, entities: List[Entity]):
        for entity in entities:
            self.unindexedـetities[entity.get_id()] = entity
        # print(len(entities), ' entities added to world_model')

    def get_entity(self, entity_id: EntityID) -> Entity:
        if entity_id in self.unindexedـetities:
            return self.unindexedـetities.get(entity_id)

        return None

    def add_entity(self, entity):
        self.unindexedـetities[entity.get_id()] = entity

    def remove_entity(self, entity_id):
        del self.unindexedـetities[entity_id]

    def get_entities(self):
        return self.unindexedـetities.values()

    def merge(self, change_set: ChangeSet):
        for entity_id in change_set.get_changed_entities():
            existing_entity = self.get_entity(entity_id)
            added = False
            if existing_entity is None:
                existing_entity = standardEntityFactory.StandardEntityFactory.make_entity(
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

        