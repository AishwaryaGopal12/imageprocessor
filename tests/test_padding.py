import os
import sys
from imageprocessor import __version__
import skimage.io
import numpy as np
from imageprocessor.padding import padding
import pytest
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


def test_version():
    '''
    Test Version of module
    '''
    assert __version__ == '0.1.0'


def test_padding():
    '''
    Check if the padding function could get the expected image
    '''
    padding("tests/images/sample.png", 20, "tests/images/samples_padding.jpg")
    output = skimage.io.imread("tests/images/samples_padding.jpg")
    test_output = skimage.io.imread("tests/images/samples_padding.jpg")
    assert np.array_equal(output, test_output), \
        "The padding function does not work properly"


# Exception Handling
def test_non_string_input():
    '''
    Check unexpected padding function input
    '''
    with pytest.raises(AttributeError):
        padding(123, 321)


def test_non_string_output():
    '''
    Check unexpected padding function for output path format
    '''
    with pytest.raises(AttributeError):
        padding(325, 123)


def test_nonexistent_input_path():
    '''
    Check unexpected padding function for input path
    '''
    with pytest.raises(FileNotFoundError):
        padding("./123/456.png", "tests/images/sample.png")


def test_nonexistent_output_path():
    '''
    Check unexpected padding function input for output
    '''
    with pytest.raises(FileNotFoundError):
        padding(
            "imageprocessor/tests/images/sample.png",
            "tests/123/s456.jpg"
        )
