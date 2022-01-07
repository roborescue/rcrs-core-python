from setuptools import setup, find_packages


# JUST FOR TEST

setup(
    name='rcrs',
    version='0.1.0',    
    description='RoboCup Rescue Simulation(RCRS Agent Development Library',
    url='https://github.com/roborescue/rcrs-core-python',
    packages=find_packages(),
    # install_requires=['mpi4py>=2.0',
    #                   'numpy',                     
    #                   ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
    ],
)
