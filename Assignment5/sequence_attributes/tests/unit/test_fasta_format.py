"""Test script for fasta_format.py."""

import pytest
from sequence_attributes import get_fasta_lists, _verify_lists


def test_get_fasta_lists(_create_fasta_file_for_testing):
    """Function to test get_fasta_lists()."""
    # make sure we get back the right data sizes with a test parse fh_in created for the test script
    # assert for both the header and seq list

    headers, seqs = get_fasta_lists(_create_fasta_file_for_testing)
    assert isinstance(headers, list) is True, "Get non-list object for headers "
    assert isinstance(seqs, list) is True, "Get non-list object for headers "
    assert len(headers) == 4, "list of headers is not 4"
    assert len(seqs) == 4, "list of sequences is not 4"


def test__verify_lists_different():
    """Function to test _verify_lists() when lists are different sizes"""

    # check to make sure lists that are different SystemExit
    with pytest.raises(SystemExit):
        _verify_lists([1, 2, 3], [1, 2])


def test__verify_lists_same():
    """Function to test _verify_lists() when lists are same"""

    # test things are ok when the lists are the same sizes
    assert _verify_lists([1, 2, 3], [1, 2, 3]) is True, \
        "Found different number of elements in the list"


if __name__ == "__main__":
    pytest.main()
