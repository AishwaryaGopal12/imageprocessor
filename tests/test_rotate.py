import numpy as np
import matplotlib.pyplot as plt
import skimage.io
from pygram import rotate



def test_rotate1():
    '''
    Check if the rotate function works properly for a specific degree
    '''
    rotate("pygram/tests/images/samples.jpg", 60, "pygram/tests/images/samples_rotate_60.png")

    output = skimage.io.imread("pygram/tests/images/samples_rotate_60.png")
    test_output = skimage.io.imread("pygram/tests/images/samples_rotateval_60.png")
    assert np.array_equal(output, test_output), "The rotate function does not work properly"



def test_rotate2():
    '''
    Check if the rotate function works properly for a specific degree, 360
    '''
    rotate("pygram/tests/images/samples.jpg", 360, "pygram/tests/images/samples_rotate_360.png")

    output = skimage.io.imread("pygram/tests/images/samples_rotate_360.png")
    test_output = skimage.io.imread("pygram/tests/images/samples_rotateval_360.png")
    assert np.array_equal(output, test_output), "The rotate function does not work properly"



def test_rotate3():
    '''
    Check if the rotate function works properly for a specific degree, 0 is the same as degree of 360
    '''
    rotate("pygram/tests/images/samples.jpg", 0, "pygram/tests/images/samples_rotate_0.png")

    output = skimage.io.imread("pygram/tests/images/samples_rotate_0.png")
    test_output = skimage.io.imread("pygram/tests/images/samples_rotateval_360.png")
    assert np.array_equal(output, test_output), "The rotate function does not work properly"


#Exception Handling
def test_non_string_input():
    '''
    Check unexpected rotating function input
    '''
    with pytest.raises(AttributeError):
        rotate(123, 60, "pygram/tests/images/samples_rotate_0.png")

def test_non_string_output():
    '''
    Check unexpected rotating function for output path format 
    '''
    with pytest.raises(AttributeError):
        rotate("pygram/tests/images/samples.png", 60, 123)

def test_nonexistent_input_path():
    '''
    Check unexpected rotating function for input path
    '''
    with pytest.raises(FileNotFoundError):
        rotate("./123/456.png", 60,  "pygram/tests/images/samples.png")

def test_nonexistent_output_path():
    '''
    Check unexpected rotating function input for output
    '''
    with pytest.raises(FileNotFoundError):
        rotate("pygram/tests/images/samples.png", 60,  "./123/456.jpg")
