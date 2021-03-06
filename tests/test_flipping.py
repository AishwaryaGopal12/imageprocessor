import os, sys
import matplotlib.pyplot as plt
import skimage.io
import pytest
import numpy as np
from imageprocessor import flipping


def test_flippingH():
    '''
    Check if the horizontal flipping function 
    '''
    flipping("pygram/tests/images/sample.png", "h", "pygram/tests/images/sample_flipping_h.png")
    output = skimage.io.imread("pygram/tests/images/samples_flipping_temp.png")
    test_output = skimage.io.imread("pygram/tests/images/sample_flipping_h.jpg")
    assert np.array_equal(output, test_output), "The flipping function does not work properly"   

def test_flippingV():
    '''
    Testing the the vertical flipping function
    '''
    flipping("pygram/tests/images/sample.png", "v", "pygram/tests/images/sample_flipping_v.png")
    output = skimage.io.imread("pygram/tests/images/sample_flipping_temp.png")
    test_output = skimage.io.imread("pygram/tests/images/sample_flipping_v.jpg")
    assert np.array_equal(output, test_output), "The flipping function does not work properly"


#Exception Handling

def test_non_string_input():
    
    '''
    Check unexpected flipping function input
    '''    
    
    with pytest.raises(AttributeError):
        flipping(555, "h", "pygram/tests/images/sample.png")
        
def test_non_string_output():
    
    '''
    Check unexpected flipping function for output path format 
    '''
    with pytest.raises(AttributeError):
        flipping("pygram/tests/images/sample.png", "v", 555)

def test_nonexistent_input_path():
    
    '''
    Check unexpected flipping function for input path
    '''
    with pytest.raises(FileNotFoundError):
        flipping("./555/456.png", "v", "pygram/tests/images/sample.png")

def test_nonexistent_output_path():
    
    '''
    Check unexpected flipping function input for output
    '''
    with pytest.raises(FileNotFoundError):
        flipping("pygram/tests/images/samples.png", "h", "./555/456.jpg")
