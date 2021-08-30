from entities.road import Road
from standardEntityURN import StandardEntityURN


class Hydrant(Road):
    urn = StandardEntityURN.HYDRANT.value

    def __init__(self, entity_id):
        Road.__init__(self, entity_id)
