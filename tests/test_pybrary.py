"""
test_pybrary.py

Tests for pybrary.
"""
import logging

from pybrary import __version__

logging.disable(logging.CRITICAL)


def test_version():
    assert __version__ == '0.1.0'
