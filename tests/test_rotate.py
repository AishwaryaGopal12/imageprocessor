import os 
import sys
import numpy as np
#import matplotlib.pyplot as plt
import skimage.io
from imageprocessor.rotate import rotate
import pytest
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
input = 

def test_rotate1():
    '''
    Check if the rotate function works properly for a specific degree, 360
    '''
    input = "tests/images/sample.png"
    output = "tests/images/sample_rotateval_360.png"
    rotate(input, 360, output)

    output = skimage.io.imread(output)
    test_output = skimage.io.imread(output)
    assert np.array_equal(output, test_output), "The rotate function does not work properly"



def test_rotate2():
    '''
    Check if the rotate function works properly for a specific degree, 0 is the same as degree of 360
    '''
    rotate("tests/images/sample.jpg", 0, \
    "tests/images/samples_rotate_0.png")

    output = skimage.io.imread("tests/images/samples_rotate_0.png")
    test_output = skimage.io.imread("tests/images/samples_rotate_0.png")
    assert np.array_equal(output, test_output), \
    "The rotate function does not work properly"


#Exception Handling
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
