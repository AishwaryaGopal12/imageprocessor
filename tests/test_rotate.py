import os
import sys
import numpy as np
# import matplotlib.pyplot as plt
import skimage.io
from imageprocessor.rotate import rotate
import pytest
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


def test_rotate1():
    '''
    Check if the rotate function works properly for a specific 360 degree
    '''
    input1 = "tests/images/sample.png"
    output2 = "tests/images/sample_rotateval_360.png"
    rotate(input1, 360, output2)

    output = skimage.io.imread(output2)
    test_output = skimage.io.imread(output2)
    assert np.array_equal(output2, test_output), \
        "The rotate function does not work properly"


def test_rotate2():
    '''
    Check if the rotate function works properly for a specific 0 degree
    '''
    input1 = "tests/images/sample.png"
    output2 = "tests/images/sample_rotateval_0.png"
    rotate(input1, 0, output2)

    output = skimage.io.imread(output2)
    test_output = skimage.io.imread(output2)
    assert np.array_equal(output, test_output), \
        "The rotate function does not work properly"


# Exception Handling
def test_non_string_input():
    '''
    Check unexpected rotating function input
    '''
    with pytest.raises(AttributeError):
        rotate(123, 60, "imageprocessor/tests/images/samples_rotate_0.png")


def test_non_string_output():
    '''
    Check unexpected rotating function for output path format
    '''
    with pytest.raises(AttributeError):
        rotate("tests/images/sample.png", 60, 123)


def test_nonexistent_input_path():
    '''
    Check unexpected rotating function for input path
    '''
    with pytest.raises(FileNotFoundError):
        rotate("./123/456.png", 60,  "tests/images/sample.png")


def test_nonexistent_output_path():
    '''
    Check unexpected rotating function input for output
    '''
    with pytest.raises(FileNotFoundError):
        rotate("tests/images/sample.png", 60,  "./123/456.jpg")
