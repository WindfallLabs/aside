#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setup.py for aside by Garin Wally.

Additional Arguments:
    help, -h: print this docstring.
    test: run the test suite with pytest and output coverage report
    clean: cleans the current directory of artifacts
"""

import glob
import os
import shutil
import sys
import warnings

from distutils.core import setup

# Help
if sys.argv[-1] in ["help", "-h"]:
    print(__doc__)

# Lint
if "lint" in sys.argv:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        os.system("flake8 aside.py")
        sys.exit(0)

# Test
if "test" in sys.argv:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        os.system("coverage run --source aside -m py.test")
        os.system("coverage html")
        sys.exit(0)

# Clean
if sys.argv[-1] == "clean":
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        [os.remove(p) for p in glob.glob("*.pyc")]
        [os.remove(p) for p in glob.glob(".coverage")]
        try:
            shutil.rmtree("htmlcov")
        except:
            pass
        sys.exit(0)


setup(
    name='aside',
    version='0.1.0',
    packages=[],
    license='MIT',
    description="Glorified Print-statements for process messaging",
    long_description=open('README.rst').read(),
    install_requires=[p for p in open("REQUIREMENTS.txt", 'r').readlines()],
    test_suite="tests",
    tests_require=["pytest", "coverage"],
    platforms='Python 2.6.x',
    classifiers=[
            'Programming Language :: Python',
            'Development Status :: 2 - Pre-Alpha',
            'Natural Language :: English',
            'Environment :: Database',  #
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Operating System :: Windows',
            'Topic :: Scintific/Engineering'
            ],
)
