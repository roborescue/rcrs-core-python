from multiprocessing import Process
import time


def func():
    time.sleep(5)


if __name__ == '__main__':
    
    processes = []

    for i in range(5):
        p = process = Process(target=func, args=())
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    while True:
        pass

