from balanced import WithStack
import pytest

def test_stack_method():
    s = WithStack()
    assert s.is_balanced('(123)') == True
    assert s.is_balanced('()[1]{23}') == True
    assert s.is_balanced('(]') == False
    assert s.is_balanced('(11[a])') == True
    assert s.is_balanced('(11[a)]') == False
