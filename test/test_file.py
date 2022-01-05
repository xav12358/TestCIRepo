# content of conftest.py
import pytest


def test_command(request):
    a = 1
    assert(a == 2)