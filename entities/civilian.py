from standardEntityURN import StandardEntityURN
from entities.human import Human

class Civilian(Human):
    urn = StandardEntityURN.CIVILIAN.value

    def __init__(self, entity_id):
        Human.__init__(self, entity_id)
        print('Civilian created ... = ', entity_id)
