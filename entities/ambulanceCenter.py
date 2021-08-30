from entities.policeForce import PoliceForceEntity
from standardEntityURN import StandardEntityURN
from entities.building import Building


class AmbulanceCentreEntity(Building):
	urn = StandardEntityURN.AMBULANCE_CENTRE.value

	def __init__(self, entity_id):
		Building.__init__(self, entity_id)
		print('Ambulance Center Created ... = ', entity_id)