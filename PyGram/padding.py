# This script is to add frame on the image
import matplotlib.pyplot as plt
import numpy as np 
def padding(image='', width=1, output_path=''):
    '''
    Add a padding to the border of the image
    Arguments:
    -----------------------------
        image: path of input file
        width: the pixels of the padding, the padding width for left, right, top, bottom are the same
    Output: 
    -----------------------------
        an image file in .png format
    '''
    # exception handling
    try:
        image = plt.imread(image)
    except FileNotFoundError:
        print("The input file/path does not exist, please double check it. ")
    except OSError:
        print("The input file is not an image.")
    except AttributeError:
        print("Please type in  a string as the path for the input image file.")
    except Exception as e:
        print("Other exceptions, please check your input and output.")
        print(e)
        raise

    extra_left, extra_right = 1, 1
    extra_top, extra_bottom = 1, 1
    image_pad = np.pad(image_stack, ((extra_left, extra_right), (extra_top, extra_bottom), (0, 0)),
       mode='constant', constant_values=0)
    # exception handling
    try:
        
        plt.imshow(image_pad)
        plt.savefig(output_path)
    except FileNotFoundError:
        print("The output path does not exist.")
    except AttributeError:
        print("Please provide a string as the path for the output image file.")
    except Exception as e:
        print("Other exceptions, please check your input and output. ")
        print(e)
        raise
