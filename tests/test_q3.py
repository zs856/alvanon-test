import pytest
from alvanon_test.q3 import Stack


def test_push():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.data == [1, 2, 3]


def test_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    assert s.data == [1, 2]


def test_inc():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.inc(2, 2)
    assert s.data == [3, 4, 3]


def test_normal_case():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.inc(2, 2)
    s.pop()
    assert s.data == [3, 4]


def test_pop_from_empty_stack():
    """
    An empty stack cannot be popped as there is nothing to be removed from the stack.
    """
    with pytest.raises(IndexError) as e_info:
        s = Stack()
        s.pop()


def test_inc_on_empty_stack():
    """
    Performing an inc operation on an empty stack should have no effect on the stack
    """
    s = Stack()
    s.inc(1, 1)
    assert s.data == []
def test_push_with_non_integer_element():
    """
    The stack should not allow adding non-integer elements
    """
    with pytest.raises(TypeError) as e_info:
        s = Stack()
        s.push('c')