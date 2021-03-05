# This script is for the rotate function
import numpy as np
import math
import matplotlib.pyplot as plt


def rotate(image, degree, output_path):
    """
    Rotate an image by a given degree
    Arguments:
    -----------------------------
        image: path of input file
        degree: int of degree
    Output:
    -----------------------------
        an image file in .png format
    """

    # exception handling
    try:
        image = plt.imread(image)
    except AttributeError:
        print("Please type in  a string as the path for the input image file.")
        raise
    except TypeError:
        print("Please provide a string as the path for the input image file.")
        raise
    except FileNotFoundError:
        print("The input file/path does not exist, please double check it. ")
        raise
    except OSError:
        print("The input file is not an image.")
        raise
    except Exception as e:
        print("General Error:")
        print(e)
        raise

    # Adapted from stackoverflow
    # convert rotation amount to radian
    rotation_amount_rad = degree * np.pi / 180.0
    # get dimension info
    height, width, num_channels = image.shape
    # create output image, for worst case size (45 degree)
    max_len = int(math.sqrt(height * height + width * width))
    rotated_image = np.zeros((max_len, max_len, num_channels))
    rotated_height, rotated_width, _ = rotated_image.shape
    mid_row = int((rotated_height + 1) / 2)
    mid_col = int((rotated_width + 1) / 2)

    for r in range(rotated_height):
        for c in range(rotated_width):
            #  apply rotation matrix, the other way
            y = (r - mid_col) * math.cos(rotation_amount_rad) + (
                c - mid_row
            ) * math.sin(rotation_amount_rad)
            x = -(r - mid_col) * math.sin(rotation_amount_rad) + (
                c - mid_row
            ) * math.cos(rotation_amount_rad)

            #  add offset
            y += mid_col
            x += mid_row

            #  get nearest index, a better way is linear interpolation
            x = round(x)
            y = round(y)
            #  check if x/y corresponds to a valid pixel in input image
            if x >= 0 and y >= 0 and x < width and y < height:
                rotated_image[r][c][:] = image[y][x][:]

    # exception handling
    try:
        plt.imshow(rotated_image)
        plt.savefig(output_path)
    except FileNotFoundError:
        print("The output path does not exist.")
        raise
    except AttributeError:
        print("Please provide a string as the path for the output image file.")
        raise
    except TypeError:
        print("Please provide a string as the path for the output image file.")
        raise
    except Exception as e:
        print("Other exceptions, please check your input and output. ")
        print(e)
        raise
