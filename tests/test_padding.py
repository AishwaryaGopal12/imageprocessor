from pygram import __version__
from pygram import padding
import matplotlib.pyplot as plt


def test_version():
    assert __version__ == '0.1.0'


def test_padding():
    padding("pygram/tests/images/samples.png", 20, "pygram/tests/images/samples_temp.png")
    output = skimage.io.imread("pygram/tests/images/samples_padding_temp.png")
    test_output = skimage.io.imread("pygram/tests/images/sample_padding.jpg")
    assert np.array_equal(output, test_output), "The padding function does not work properly"

#Exception Handling
def test_non_string_input():
    with pytest.raises(AttributeError):
        padding(123, "pygram/tests/images/samples.png")

def test_non_string_output():
    with pytest.raises(AttributeError):
        padding("pygram/tests/images/samples.png", 123)

def test_nonexistent_input_path():
    with pytest.raises(FileNotFoundError):
        padding("./123/456.png", "pygram/tests/images/samples.png")

def test_nonexistent_output_path():
    with pytest.raises(FileNotFoundError):
        padding("pygram/tests/images/samples.png", "./123/456.jpg")
