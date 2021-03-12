import os, sys
import matplotlib.pyplot as plt
import skimage.io
import pytest
import numpy as np
import pytest
from imageprocessor.flipping import flipping

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# def test_flippingH():
#     '''
#     Check if the horizontal flipping function 
#     '''
#     flipping("tests/images/sample.png", "h", "tests/images/sample_flipping_h.png")
#     output = skimage.io.imread("tests/images/sample_flipping_h.png")
#     test_output = skimage.io.imread("tests/images/sample_flipping_h.png")
#     assert np.array_equal(output, test_output), "The flipping function does not work properly"   

# def test_flippingV():
#     '''
#     Testing the the vertical flipping function
#     '''
#     flipping("tests/images/sample.png", "v", "tests/images/sample_flipping_v.png")
#     output = skimage.io.imread("tests/images/sample_flipping_v.png")
#     test_output = skimage.io.imread("tests/images/sample_flipping_v.png")
#     assert np.array_equal(output, test_output), "The flipping function does not work properly"


Exception Handling

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
