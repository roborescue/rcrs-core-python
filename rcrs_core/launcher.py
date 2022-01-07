from rcrs_core.connection.componentLauncher import ComponentLauncher
from agents.policeForceAgent import PoliceForceAgent
from agents.ambulanceTeamAgent import AmbulanceTeamAgent
from agents.fireBrigadeAgent import FireBrigadeAgent
from agents.fireStationAgent import FireStationAgent
from agents.policeOfficeAgent import PoliceOfficeAgent
from agents.ambulanceCenterAgent import AmbulanceCenterAgent
from rcrs_core.constants.constants import DEFAULT_KERNEL_PORT_NUMBER
from rcrs_core.constants.constants import DEFAULT_KERNEL_HOST_NAME
import time
import sys
import os
import ipaddress
from multiprocessing import Process, Pipe


class Launcher:
    def __init__(self, **kwargs):

        processes = []
        agents = {}
        self.launcher = ComponentLauncher(kwargs['port'], kwargs['host'])
        agents['FireBrigadeAgent'] = kwargs['fb'] if kwargs['fb'] >= 0 else 100
        agents['FireStationAgent'] = kwargs['fs'] if kwargs['fs'] >= 0 else 100
        agents['PoliceForceAgent'] = kwargs['pf'] if kwargs['pf'] >= 0 else 100
        agents['PoliceOfficeAgent'] = kwargs['po'] if kwargs['po'] >= 0 else 100
        agents['AmbulanceTeamAgent'] = kwargs['at'] if kwargs['at'] >= 0 else 100
        agents['AmbulanceCenterAgent'] = kwargs['ac'] if kwargs['ac'] >= 0 else 100
        precomute = True if kwargs['pre'].lower() == 'true' else False
        print(precomute)
        FireBrigadeAgent(precomute)
        for agn, num in agents.items():
            for _ in range(num):
                request_id = self.launcher.generate_request_ID()
                process = Process(target=self.launch, args=(eval(agn)(precomute), request_id))
                process.start()
                processes.append(process)
                time.sleep(1/100)
        
        for p in processes:
            p.join()

    def launch(self, agent, _request_id):
        self.launcher.connect(agent, _request_id)


if __name__ == '__main__':

    filelist = [f for f in os.listdir('logs') if f.endswith(".log")]
    for f in filelist:
        os.remove(os.path.join('logs', f))

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
        print('-pre  precompute flag. default is false')
        sys.exit(0)

    try:
        host = args.get('-h') if '-h' in args else DEFAULT_KERNEL_HOST_NAME
        if host != 'localhost':
            ipaddress.ip_address(host)
    except ValueError as err:
        print(err)
        sys.exit(0)

    try:
        port = int(args.get('-p')) if '-p' in args else int(DEFAULT_KERNEL_PORT_NUMBER)
        precumpute = args.get('-pre') if '-pre' in args else 'False' 
        fb = int(args.get('-fb')) if '-fb' in args else 0
        fs = int(args.get('-fs')) if '-fs' in args else 0
        pf = int(args.get('-pf')) if '-pf' in args else 0
        po = int(args.get('-po')) if '-po' in args else 0
        at = int(args.get('-at')) if '-at' in args else 0
        ac = int(args.get('-ac')) if '-ac' in args else 0
    except ValueError as err:
        print(err)
        sys.exit(0)

    print("start launcher...")
    launcher = Launcher(host=host, port=port, fb=fb, fs=fs, pf=pf, po=po, at=at, ac=ac, pre=precumpute)
    while True:
        try:
            time.sleep(2)
        except KeyboardInterrupt:
            sys.exit(1)
    print("launcher exited...")
