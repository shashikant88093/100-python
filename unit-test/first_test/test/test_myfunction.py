import pytest
import source.myfunction as myfunction

def test_add():
    result = myfunction.add(1,2)
    assert result == 3