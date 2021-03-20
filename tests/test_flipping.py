import os
import sys
import matplotlib.pyplot as plt
# import skimage.io
import pytest
import numpy as np
from imageprocessor.flipping import flipping

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


# def test_flipping():
#     '''
#     Testing the horizontal flipping function
#     '''
#     flipping("tests/images/sample.jpg", "tests/images/sample_flipping_h.png")
#     output = plt.imread("tests/images/sample_flipping_h.png")
#     test_output = plt.imread("tests/images/flipped_sample.png")
#     assert np.array_equal(output, test_output), "The image was not flipped properly"


# Exception Handling

def test_non_string_input():
    '''
    testing input format
    '''
    with pytest.raises(AttributeError):
        flipping(555, 0)


def test_non_string_output():
    '''
    Testing output format
    '''
    with pytest.raises(AttributeError):
        flipping(0, 555)


def test_nonexistent_input_path():
    '''
    Testing input path
    '''
    with pytest.raises(FileNotFoundError):
        flipping("./123/456.png", "tests/images/sample.png")


def test_nonexistent_output_path():
    '''
    Testing output path
    '''
    with pytest.raises(FileNotFoundError):
        flipping("img/tests/images/sample.png", "./3/5.png")
