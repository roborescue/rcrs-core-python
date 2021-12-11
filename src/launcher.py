import multiprocessing
from agents import agent
from connection.componentLauncher import ComponentLauncher
from agents.policeForceAgent import PoliceForceAgent
from agents.ambulanceTeamAgent import AmbulanceTeamAgent
from agents.fireBrigadeAgent import FireBrigadeAgent
from agents.fireStationAgent import FireStationAgent
from agents.policeOfficeAgent import PoliceOfficeAgent
from agents.ambulanceCenterAgent import AmbulanceCenterAgent
from constants.constants import DEFAULT_KERNEL_PORT_NUMBER
from constants.constants import DEFAULT_KERNEL_HOST_NAME
import time
import sys
import os
import ipaddress
from multiprocessing import Process, Pipe
#from multiprocessing import Manager
#from multiprocessing import Queue


class Launcher:
    def __init__(self, **kwargs):

        self.launcher = ComponentLauncher(kwargs['port'], kwargs['host'])
        fb = kwargs['fb'] if kwargs['fb'] > 0 else sys.maxsize
        fs = kwargs['fs'] if kwargs['fs'] > 0 else sys.maxsize
        pf = kwargs['pf'] if kwargs['pf'] > 0 else sys.maxsize
        po = kwargs['po'] if kwargs['po'] > 0 else sys.maxsize
        at = kwargs['at'] if kwargs['at'] > 0 else sys.maxsize
        ac = kwargs['ac'] if kwargs['ac'] > 0 else sys.maxsize

        processes = []

        for _ in range(pf):
            request_id = self.launcher.generate_request_ID()
            process = Process(target=self.launch, args=(PoliceForceAgent(), request_id))
            process.daemon = True
            process.start()
            processes.append(process)
            #time.sleep(1/100)
            #multiprocessing.active_children()

        # time.sleep(1)
        # #mpq = Queue()
        # #mpq.put(True)
        # for _ in range(at):
        #     if True:
        #         request_id = self.launcher.generate_request_ID()
        #         process = Process(target=self.launch, args=(AmbulanceTeamAgent(), request_id, mpq))
        #         process.daemon = True
        #         process.start()
        #         processes.append(process)
        #         #time.sleep(1/10)
        #         multiprocessing.active_children()
        #     else:
        #         break
        
        # time.sleep(1)
        # #mpq = Queue()
        # #mpq.put(True)
        # for _ in range(fb):
        #     if True:
        #         request_id = self.launcher.generate_request_ID()
        #         process = Process(target=self.launch, args=(FireBrigadeAgent(), request_id, mpq))
        #         process.daemon = True
        #         process.start()
        #         processes.append(process)
        #         #time.sleep(1/10)
        #         multiprocessing.active_children()
        #     else:
        #         break

        # time.sleep(1)
        # #mpq = Queue()
        # mpq.put(True)
        # for _ in range(po):
        #     if mpq.get():
        #         request_id = self.launcher.generate_request_ID()
        #         process = Process(target=self.launch, args=(PoliceOfficeAgent(), request_id, mpq))
        #         process.daemon = True
        #         process.start()
        #         processes.append(process)
        #         #time.sleep(1/10)
        #         multiprocessing.active_children()
        #     else:
        #         break

        # time.sleep(1)
        # #mpq = Queue()
        # mpq.put(True)
        # for _ in range(ac):
        #     if mpq.get():
        #         request_id = self.launcher.generate_request_ID()
        #         process = Process(target=self.launch, args=(AmbulanceCenterAgent(), request_id, mpq))
        #         process.daemon = True
        #         process.start()
        #         processes.append(process)
        #         #time.sleep(1/10)
        #         multiprocessing.active_children()
        #     else:
        #         break

        # time.sleep(1)
        # #mpq = Queue()
        # mpq.put(True)
        # for _ in range(fs):
        #     if mpq.get():
        #         request_id = self.launcher.generate_request_ID()
        #         process = Process(target=self.launch, args=(FireStationAgent(), request_id, mpq))
        #         process.daemon = True
        #         process.start()
        #         processes.append(process)
        #         #time.sleep(1/10)
        #         multiprocessing.active_children()
        #     else:
        #         break

    def launch(self, agent, _request_id):
        self.launcher.connect(agent, _request_id)
        status = agent.test_sucsses()
        while status:
            time.sleep(2)


if __name__ == '__main__':

    filelist = [f for f in os.listdir('logs') if f.endswith(".log")]
    for f in filelist:
        os.remove(os.path.join('logs', f))
    

    port = None
    host = None
    fb = -1
    fs = -1
    pf = -1
    po = -1
    at = -1
    ac = -1

    args = {}
    arg = sys.argv.pop(0)
    while(arg is not None and len(sys.argv) >= 2):
        arg = sys.argv.pop(0)
        value = sys.argv.pop(0)
        args[arg] = value

    if(len(sys.argv) > 0):
        print('Usage: python3 launcher.py')
        print('[options]')
        print('-p    RCRS server port number')
        print('-h    RCRS server host IP')
        print('-fb   number of Firebrigade       (-1 to run all)')
        print('-fs   number of FireStation       (-1 to run all)')
        print('-pf   number of PoliceForce       (-1 to run all)')
        print('-po   number of PoliceOffice      (-1 to run all)')
        print('-at   number of AmbulanceTeam     (-1 to run all)')
        print('-ac   number of AmbulanceCenter   (-1 to run all)')
        sys.exit(0)

    try:
        if '-p' in args:
            port = int(args.get('-p'))
        else:
            port = int(DEFAULT_KERNEL_PORT_NUMBER)
    except ValueError as err:
        print('-p error: ', err)
        sys.exit(0)

    try:
        if '-h' in args:
            host = args.get('-h')
            if host != 'localhost':
                ipaddress.ip_address(host)
        else:
            host = DEFAULT_KERNEL_HOST_NAME
    except ValueError as err:
        print(err)
        sys.exit(0)

    try:
        if '-fb' in args:
            fb = int(args.get('-fb'))

        if '-fs' in args:
            fs = int(args.get('-fs'))

        if '-pf' in args:
            pf = int(args.get('-pf'))

        if '-po' in args:
            po = int(args.get('-po'))

        if '-at' in args:
            at = int(args.get('-at'))

        if '-ac' in args:
            ac = int(args.get('-ac'))

    except ValueError as err:
        print(err)
        sys.exit(0)

    print("start launcher...")
    launcher = Launcher(host=host, port=port, fb=fb, fs=fs, pf=pf, po=po, at=at, ac=ac)
    while True:
        try:
            time.sleep(100)
        except KeyboardInterrupt:
            sys.exit(1)
    print("launcher exited...")
