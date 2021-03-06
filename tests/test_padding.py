import os, sys
import matplotlib.pyplot as plt
#currentdir = os.path.dirname(os.path.realpath(__file__))
#parentdir = os.path.dirname(currentdir)
#sys.path.append(parentdir)
from imageprocessor import __version__
from imageprocessor import padding

def test_version():
    '''
    Test Version of module
    '''
    assert __version__ == '0.1.0'

def test_padding():
    '''
    Check if the padding function could get the expected image
    '''
    padding("pygram/tests/images/samples.png", 20, "pygram/tests/images/samples_temp.png")
    output = skimage.io.imread("pygram/tests/images/samples_padding_temp.png")
    test_output = skimage.io.imread("pygram/tests/images/sample_padding.jpg")
    assert np.array_equal(output, test_output), "The padding function does not work properly"

#Exception Handling
def test_non_string_input():
    '''
    Check unexpected padding function input
    '''
    with pytest.raises(AttributeError):
        padding(123, "pygram/tests/images/samples.png")

def test_non_string_output():
    '''
    Check unexpected padding function for output path format 
    '''
    with pytest.raises(AttributeError):
        padding("pygram/tests/images/samples.png", 123)

def test_nonexistent_input_path():
    '''
    Check unexpected padding function for input path
    '''
    with pytest.raises(FileNotFoundError):
        padding("./123/456.png", "pygram/tests/images/samples.png")

def test_nonexistent_output_path():
    '''
    Check unexpected padding function input for output
    '''
    with pytest.raises(FileNotFoundError):
        padding("pygram/tests/images/samples.png", "./123/456.jpg")
