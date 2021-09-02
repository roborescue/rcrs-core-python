from agents.policeForceAgent import PoliceForceAgent
from agents.ambulanceTeamAgent import AmbulanceTeamAgent
from agents.fireBrigadeAgent import FireBrigadeAgent

import time
import sys


class Launcher:
    def __init__(self) -> None:

        police = PoliceForceAgent()
        time.sleep(2)
        ambulance = AmbulanceTeamAgent()
        time.sleep(2)
        fire = FireBrigadeAgent()


if __name__ == '__main__':

    launcher = Launcher()

    while True:
        try:
            time.sleep(100)
        except KeyboardInterrupt:
            sys.exit(1)
