import pytest
from secondary_structure_splitter import (_verify_lists)

def test__verify_lists():
    """check to make sure lists that are different SystemExit"""
    with pytest.raises(SystemExit):
        _verify_lists([1, 2, 3], [1, 2])
        _verify_lists()

if __name__ == '__main__':
    test__verify_lists()
    print("Everything Passes")
