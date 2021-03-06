import numpy as np
import matplotlib.pyplot as plt
import skimage.io


def flipping(image, direction, output_path):
    '''
    Flipping an image in either horizontal or vertical direction
    
    Arguments:
    -----------------------------
        image: path of the input file
        direction: direction of flip, horizontal="h", vertical = "v"
    Output:
    -----------------------------
        an image file in .png format
    '''
    
    assert direction in ["h","v"], "Invalid flipping direction"
# exception handling

    try:
        input_image = plt.imread(image)
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

    
#Horizontal Flipping
    if direction == "h":
        original=range(0, input_image.shape[1])
        flipped=list(reversed(original))
        output_matrix = input_image.copy()
        output_matrix[:,original] = input_image[:,flipped]

#Vertical Flipping

    elif direction == "v":
        original=range(0, input_image.shape[0])
        flipped=list(reversed(original))
        output_matrix = input_image.copy()
        output_matrix[original] = input_image[flipped]


    #Data.type
    output_matrix=np.array(output_matrix, dtype=np.uint8)


    # exception handling
    try:

        plt.imshow(output_matrix)
        plt.savefig(output_path)
    except FileNotFoundError:
        print("The output path does not exist.")
    except AttributeError:
        print("Please provide a string as the path for the output image file.")
    except Exception as e:
        print("Other exceptions, please check your input and output. ")
        print(e)
        raise
