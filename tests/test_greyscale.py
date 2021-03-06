import os, sys
import matplotlib.pyplot as plt
#currentdir = os.path.dirname(os.path.realpath(__file__))
#parentdir = os.path.dirname(currentdir)
#sys.path.append(parentdir)
from imageprocessor import greyscale

def test_greyscale():
    '''
    Check if the greyscale function could get the expected image
    '''
    greyscale("pygram/tests/images/sample.png", "pygram/tests/images/samples_temp.png")
    output = skimage.io.imread("pygram/tests/images/samples_greyscale_temp.png")
    test_output = skimage.io.imread("pygram/tests/images/sample_greyscale.png")
    assert np.array_equal(output, test_output), "The greyscale function does not work properly"

#Exception Handling
def test_non_string_input():
    '''
    Check unexpected greyscale function input
    '''
    with pytest.raises(AttributeError):
        greyscale(123, "pygram/tests/images/samples.png")

def test_non_string_output():
    '''
    Check unexpected greyscale function for output path format 
    '''
    with pytest.raises(AttributeError):
        greyscale("pygram/tests/images/samples.png", 123)

def test_nonexistent_input_path():
    '''
    Check unexpected greyscale function for input path
    '''
    with pytest.raises(FileNotFoundError):
        greyscale("./123/456.png", "pygram/tests/images/samples.png")

def test_nonexistent_output_path():
    '''
    Check unexpected greyscale function input for output
    '''
    with pytest.raises(FileNotFoundError):
        greyscale("pygram/tests/images/samples.png", "./123/456.jpg")