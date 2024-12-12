import pytest
from nt_fasta_stats import (_verify_lists, _get_num_nucleotides)

def test__verify_lists():
    """check to make sure lists that are different SystemExit"""
    with pytest.raises(SystemExit):
        _verify_lists([1, 2, 3], [1, 2])
        _verify_lists()

def test__get_num_nucleotides():
    with pytest.raises(SystemExit):
        _get_num_nucleotides()

if __name__ == '__main__':
    test__verify_lists()
    test__get_num_nucleotides()
    print("Everything Passes")