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

def test_flippingH():
    '''
    Check if the horizontal flipping function 
    '''
    flipping("imageprocessor/tests/images/sample.png", "h", "imageprocessor/tests/images/sample_flipping_h.png")
    output = skimage.io.imread("imageprocessor/tests/images/samples_flipping_temp.png")
    test_output = skimage.io.imread("imageprocessor/tests/images/sample_flipping_h.jpg")
    assert np.array_equal(output, test_output), "The flipping function does not work properly"   

def test_flippingV():
    '''
    Testing the the vertical flipping function
    '''
    flipping("imageprocessor/tests/images/sample.png", "v", "imageprocessor/tests/images/sample_flipping_v.png")
    output = skimage.io.imread("imageprocessor/tests/images/sample_flipping_temp.png")
    test_output = skimage.io.imread("imageprocessor/tests/images/sample_flipping_v.jpg")
    assert np.array_equal(output, test_output), "The flipping function does not work properly"


#Exception Handling

def test_non_string_input():
    
    '''
    Check unexpected flipping function input
    '''    
    
    with pytest.raises(AttributeError):
        flipping(555, "h", "imageprocessor/tests/images/sample.png")
        
def test_non_string_output():
    
    '''
    Check unexpected flipping function for output path format 
    '''
    with pytest.raises(AttributeError):
        flipping("imageprocessor/tests/images/sample.png", "v", 555)

def test_nonexistent_input_path():
    
    '''
    Check unexpected flipping function for input path
    '''
    with pytest.raises(FileNotFoundError):
        flipping("./555/456.png", "v", "imageprocessor/tests/images/sample.png")

def test_nonexistent_output_path():
    
    '''
    Check unexpected flipping function input for output
    '''
    with pytest.raises(FileNotFoundError):
        flipping("imageprocessor/tests/images/samples.png", "h", "./555/456.jpg")

