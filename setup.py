from setuptools import setup, find_packages, Command
import os
from commands import *

name = 'pysorter'
base_dir = os.path.dirname(__file__)

tests_require=['pytest', 'testfixtures', 'pytest-cov'],

setup(
    name='pysorter',
    version=open(os.path.join(base_dir, name, 'version.txt')).read().strip(),
    description='A regex based file organizer',
    long_description=open(os.path.join(base_dir, 'description.txt')).read().strip(),
    license='GPL',
    url='https://github.com/chriscz/pySorter',

    author='Chris Coetzee',
    author_email='chriscz93@gmail.com',

    packages=find_packages(),
    setup_requires=['pytest-runner'],
    tests_require=tests_require,

    include_package_data=True,
    zip_safe=False,

    cmdclass={
        'coverage': CoverageCommand,
    },

    entry_points={
        "console_scripts": ['pysorter=pysorter.core.pysorter:main']
    },
    extras_require=dict(
        build=['twine'],
        test=['pytest', 'testfixtures', 'pytest-cov'],
    ),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
    ]
)
