from setuptools import setup, find_packages


# JUST FOR TEST

setup(
    name='rcrs',
    version='0.1.0',    
    description='RoboCup Rescue Simulation(RCRS Agent Development Library)',
    url='https://github.com/roborescue/rcrs-core-python',
    packages=find_packages(),
    install_requires=['protobuf', 'rtree'],
)
