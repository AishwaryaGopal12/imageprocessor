import numpy as np
import matplotlib.pyplot as plt
# import cv2
# import skimage.io


def flipping(input_path, output_path):
    '''
    Flipping an image in either horizontal or vertical direction

    Arguments:
    -----------------------------
        input_path: path of the input file
    Output:
    -----------------------------
        an image file in .png format
    '''

# exception handling

    try:
        input_image = plt.imread(input_path)
        print("Success")
    except FileNotFoundError:
        print("The input file/path does not exist")
        raise
    except OSError:
        print("The input file is not an image.")
        raise
    except AttributeError:
        print("Please type in  a string as the path for the input image file.")
        raise
    except Exception as e:
        print("Other Errors")
        print(e)
        raise

    input_image = np.dot(input_image[..., :3], [0.2989, 0.5870, 0.1140])

# Horizontal Flipping
    original = range(0, input_image.shape[1])
    flipped = list(reversed(original))
    output_matrix = input_image.copy()
    output_matrix[:, original] = input_image[:, flipped]

# Data.type
    output_matrix = np.array(output_matrix, dtype=np.uint8)

    # exception handling
    try:
        plt.imshow(output_matrix)
        plt.imsave(output_path, output_matrix, cmap=plt.get_cmap("gray"))
    except FileNotFoundError:
        print("The output path does not exist.")
    except AttributeError:
        print("Please provide a string as the path for the output image file.")
    except Exception as e:
        print("Other exceptions, please check your input and output. ")
        print(e)
        raise
