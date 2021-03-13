import os
import sys
# import matplotlib.pyplot as plt
# import skimage.io
import pytest
# import numpy as np
from imageprocessor.flipping import flipping

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# def test_flippingH():
#     '''
#     Testing the horizontal flipping function
#     '''
#     flipping("tests/images/sample.png", "h", \
#      "tests/images/sample_flipping_h.png")
#     output = skimage.io.imread("tests/images/sample_flipping_h.png")
#     test_output = skimage.io.imread("tests/images/sample_flipping_h.png")
#     assert np.array_equal(output, test_output), \
#       "The flipping function does not work properly"

# def test_flippingV():
#     '''
#     Testing the the vertical flipping function
#     '''
#     flipping("tests/images/sample.png", "v", \
#       "tests/images/sample_flipping_v.png")
#     output = skimage.io.imread("tests/images/sample_flipping_v.png")
#     test_output = skimage.io.imread("tests/images/sample_flipping_v.png")
#     assert np.array_equal(output, test_output), \
#      "The flipping function does not work properly"


# Exception Handling

def test_non_string_input():
    '''
    testing input format
    '''
    with pytest.raises(AttributeError):
        flipping(555, "h", 0)


def test_non_string_output():
    '''
    Testing output format
    '''
    with pytest.raises(AttributeError):
        flipping(0, "h", 555)


def test_nonexistent_input_path():
    '''
    Testing input path
    '''
    with pytest.raises(FileNotFoundError):
        flipping("./123/456.png", "h", "tests/images/sample.png")


def test_nonexistent_output_path():
    '''
    Testing output path
    '''
    with pytest.raises(FileNotFoundError):
        flipping\
        ("imageprocessor/tests/images/sample.png", "h", "./123/456.png")
