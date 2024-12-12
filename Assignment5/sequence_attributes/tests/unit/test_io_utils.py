"""Test script for io_utils.py."""

import os
import pytest
from sequence_attributes import FileHandler


def test_file_handler_open_and_closing():
    """Function to test file_handler opening and closing"""

    # create test file to use
    # test if able to write 'this is a test' to it and read it with filehandler.
    test_file = "test_file.txt"
    with open(test_file, 'w', encoding="utf-8") as test_file:
        test_file.write('this is a test')

    with FileHandler(test_file, 'r') as file:
        file_content = file.read()
        assert file_content == 'this is a test'

    assert file.closed

    # make sure to remove test file when done
    try:
        os.remove(test_file)
    except OSError as error:
        print("Error with cleaning:", error)


def test_file_handler_os_error():
    """Function to test file_handler os error"""

    # error raised if there is os error trying to read file with filehandler
    with pytest.raises(OSError, match="OSError: Could not open the file"):
        with FileHandler("fake_test_file.txt", "r") as file:
            file.read()


def test_file_handler_value_error():
    """Function to test file_handler value error"""

    # error raised if there is a value error raised trying to write to file with filehandler
    with pytest.raises(ValueError, match="ValueError: Invalid mode for file"):
        with FileHandler("test_file.txt", "x") as file:
            file.write("test")


def test_file_handler_type_error():
    """Function to test file_handler type error"""

    # error raised if there is a type error raised trying to write to file with filehandler
    with pytest.raises(TypeError, match="TypeError: Invalid type for file"):
        with FileHandler("test_file.txt", 1) as file:
            file.write("test")


def test_file_handler_write():
    """Function to test file_handler ability to write"""

    # create test file
    # try to write to test file using filehandler and then read
    test_file = "test_file.txt"
    with FileHandler(test_file, 'w') as file:
        file.write('this is a test')
    with open(test_file, 'r', encoding="utf-8") as file:
        file_content = file.read()
        assert file_content == 'this is a test'

    # make sure to remove test file when done
    try:
        os.remove(test_file)
    except OSError as error:
        print("Error with cleaning:", error)


if __name__ == "__main__":
    pytest.main()
