#!/usr/bin/env python3
'''
CV Clean: Test Framework
'''
import importlib.util
import sys


# Import ../__init__.py as cvclean
SPEC = importlib.util.spec_from_file_location('cvclean', '__init__.py')
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules['cvclean'] = MODULE
SPEC.loader.exec_module(MODULE)
