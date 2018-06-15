# Always prefer setuptools over distutils
import sys  # NOQA

import os
from codecs import open
from os import path

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))
from setuptools import setup, find_packages

# To use a consistent encoding
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# read from environment variable
searchEngine_version = "1.0.0"

# read from file, if this is not present


setup(
    name='searchEngine',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=searchEngine_version,

    description='searchEngine',
    long_description=long_description,
    # The project's main homepage.
    url='no public url available',
    # Author details
    author='Mohit Khanna',
    author_email='mohit.khanna2008@gmail.com',
    license='proprietary',


    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        # Indicate who your project is intended for
        'Intended Audience :: any user',
        'Topic :: Software Development :: Build Tools',
        'License :: proprietary :: Open source'
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='searchEngine',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['test']),

    include_package_data=True,

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'cmd2>=0.7.5',
        'flask>=0.11.1',
        'whoosh>=2.7.4',
        'requests>=2.18.4',
        'python-docx>=0.8.6',
        'PyPDF2>=1.26.0',
        'bs4>=0.0.1'
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
#        'dev': ['check-manifest'],
#        'test': ['coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'sample': ['searchEngine/server/static/*.jpg','searchEngine/server/static/*.ico','searchEngine/server/templates/*.html'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': ['search_engine_shell=searchEngine.engine.se_shell:init_commands',
                            'server_start=searchEngine.server.search_server:runServer']
    },
)
