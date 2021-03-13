import os
import sys
# import matplotlib.pyplot as plt
from imageprocessor.greyscale import greyscale
import pytest
import numpy as np
import skimage.io
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


def test_greyscale():
    '''
    Check if the greyscale function could get the expected image
    '''
    greyscale("tests/images/sample.png", "tests/images/sample.png")
    output = skimage.io.imread("tests/images/sample.png")
    test_output = skimage.io.imread("tests/images/sample.png")
    assert np.array_equal(output, test_output), \
    "The greyscale function does not work properly"


# Exception Handling
def test_non_string_input():
    '''
    Check unexpected greyscale function input
    '''
    with pytest.raises(AttributeError):
        greyscale(555, 0)


def test_non_string_output():
    '''
    Check unexpected rotating function for output path format
    '''
    with pytest.raises(AttributeError):
        greyscale(0, 555)


def test_nonexistent_input_path():
    '''
    Check unexpected greyscale function for input path
    '''
    with pytest.raises(FileNotFoundError):
        greyscale("./123/456.png", "tests/images/sample.png")


def test_nonexistent_output_path():
    '''
    Check unexpected greyscale function input for output
    '''
    with pytest.raises(FileNotFoundError):
        greyscale("imageprocessor/tests/images/sample.png", "./123/456.png")