# from setuptools import setup, find_packages


# # JUST FOR TEST

# setup(
#     name='rcrs',
#     version='0.1.0',    
#     description='RoboCup Rescue Simulation(RCRS Agent Development Library',
#     url='https://github.com/roborescue/rcrs-core-python',
#     packages=find_packages(),
#     # install_requires=['mpi4py>=2.0',
#     #                   'numpy',                     
#     #                   ],

#     classifiers=[
#         'Development Status :: 1 - Planning',
#         'Intended Audience :: Science/Research',
#         'Operating System :: POSIX :: Linux',        
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.4',
#         'Programming Language :: Python :: 3.5',
#         'Programming Language :: Python :: 3.8',
#     ],
# )

from setuptools import setup, find_packages

# from my_pip_package import __version__

extra_math = [
    'returns-decorator',
]

extra_bin = [
    *extra_math,
]

extra_test = [
    *extra_math,
    'pytest>=4',
    'pytest-cov>=2',
]
extra_dev = [
    *extra_test,
]

extra_ci = [
    *extra_test,
    'python-coveralls',
]

setup(
    name='my_pip_package',
    version=__version__,
    description='RoboCup Rescue Simulation core python',

    url='https://github.com/roborescue/rcrs-core-python',
    author='Farshid Faraji',
    author_email='faraji.farshid@gmail.com',

    packages=find_packages(),

    extras_require={
        'math': extra_math,

        'bin': extra_bin,

        'test': extra_test,
        'dev': extra_dev,

        'ci': extra_ci,
    },

#     entry_points={
#         'console_scripts': [
#             'add=my_pip_package.math:cmd_add',
#         ],
#     },

    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
