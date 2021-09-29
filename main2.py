from multiprocessing import Process
from multiprocessing import Pool

import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f(name):
    import asyncio
    from agent.Civilian import Civilian
    civilian=Civilian()
    # await civilian.connect("127.0.0.1",7000)
    asyncio.run(civilian.connect("127.0.0.1",7000))
    info('function f')

if __name__ == '__main__':
    pool = Pool()                         # Create a multiprocessing Pool
    # pool.map(f, [1,2,3])
    # info('main line')
    for i in range(600):
        p = Process(target=f, args=('bob',))
        p.start()