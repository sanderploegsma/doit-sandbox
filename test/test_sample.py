"""A sample test suite."""

from doit_sandbox import sample


def test_add():
    """Tests the sample.add function."""
    assert sample.add(1, 2) == 3
