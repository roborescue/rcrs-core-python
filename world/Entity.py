import core.urn as urn


class Entity:

    def __init__(self, urn, id):
        self.properties = {}
        self.urn = urn
        self.id = id


    def __getitem__(self, property_urn):  # []
        return self.properties.get(property_urn)

    def __setitem__(self, property_urn, val):  # []
        self.properties[property_urn] = val

    def hasProp(self, property_urn):
        return property_urn in self.properties

    # TODO remove
    def getProp(self, property_urn):
        return self[property_urn]

    # TODO remove
    def setProp(self, purn, val):
        self[purn] = val

    def __str__(self):
        return f'{self.urn.name}({self.id})'

    def __repr__(self):
        s = f'{self!s}\n'
        for p in self.properties:
            pstr = str.replace(f'{self.properties[p]}', '\n', ', ')
            s += f'\t {p.name}= {pstr}\n'
        return s
