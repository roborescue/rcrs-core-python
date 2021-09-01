from agent import *
import time
import sys

import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


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

