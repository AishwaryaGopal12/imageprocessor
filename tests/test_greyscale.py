import os, sys
import matplotlib.pyplot as plt
from imageprocessor import greyscale

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

def test_greyscale():
    '''
    Check if the greyscale function could get the expected image
    '''
    greyscale("imageprocessor/tests/images/sample.png", "imageprocessor/tests/images/samples_temp.png")
    output = skimage.io.imread("imageprocessor/tests/images/samples_greyscale_temp.png")
    test_output = skimage.io.imread("imageprocessor/tests/images/sample_greyscale.png")
    assert np.array_equal(output, test_output), "The greyscale function does not work properly"

#Exception Handling
def test_non_string_input():
    '''
    Check unexpected greyscale function input
    '''
    with pytest.raises(AttributeError):
        greyscale(123, "imageprocessor/tests/images/samples.png")

def test_non_string_output():
    '''
    Check unexpected greyscale function for output path format 
    '''
    with pytest.raises(AttributeError):
        greyscale("imageprocessor/tests/images/samples.png", 123)

def test_nonexistent_input_path():
    '''
    Check unexpected greyscale function for input path
    '''
    with pytest.raises(FileNotFoundError):
        greyscale("./123/456.png", "imageprocessor/tests/images/samples.png")

def test_nonexistent_output_path():
    '''
    Check unexpected greyscale function input for output
    '''
    with pytest.raises(FileNotFoundError):
        greyscale("imageprocessor/tests/images/samples.png", "./123/456.jpg")