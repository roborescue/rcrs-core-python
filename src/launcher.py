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
import ipaddress


class Launcher:
    def __init__(self, **kwargs):

        launcher = ComponentLauncher(kwargs['port'], kwargs['host'])
        fb = kwargs['fb'] if kwargs['fb'] > 0 else sys.maxsize
        fs = kwargs['fs'] if kwargs['fs'] > 0 else sys.maxsize
        pf = kwargs['pf'] if kwargs['pf'] > 0 else sys.maxsize
        po = kwargs['po'] if kwargs['po'] > 0 else sys.maxsize
        at = kwargs['at'] if kwargs['at'] > 0 else sys.maxsize
        ac = kwargs['ac'] if kwargs['ac'] > 0 else sys.maxsize

        for i in range(pf):
            if launcher.connect(PoliceForceAgent()):
                continue
            break

        for i in range(at):
            if launcher.connect(AmbulanceTeamAgent()):
                continue
            break

        for i in range(fb):
            if launcher.connect(FireBrigadeAgent()):
                continue
            break

        for i in range(po):
            if launcher.connect(PoliceOfficeAgent()):
                continue
            break

        for i in range(ac):
            if launcher.connect(AmbulanceCenterAgent()):
                continue
            break

        for i in range(fs):
            if launcher.connect(FireStationAgent()):
                continue
            break


if __name__ == '__main__':

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

    launcher = Launcher(host=host, port=port, fb=fb,
                        fs=fs, pf=pf, po=po, at=at, ac=ac)
    while True:
        try:
            time.sleep(100)
        except KeyboardInterrupt:
            sys.exit(1)
