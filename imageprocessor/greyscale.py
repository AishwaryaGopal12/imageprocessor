import matplotlib.pyplot as plt
import numpy as np
import cv2


def greyscale(image, output_path):
    '''
    Converting a color image into a greyscale image
    Input:
    -----------------------------
        image: string, path for the input image file
        output_path: string, path for the output image file
   
    Output:
    -----------------------------
        an image file at the specified output path
    '''
    try:
        image = plt.imread(image)
    except FileNotFoundError:
        print("The input file/path does not exist, please double check it. ")
        raise
    except OSError:
        print("The input file is not an image.")
        raise
    except AttributeError:
        print("Please type in  a string as the path for the input image file.")
        raise
    except Exception as e:
        print("Other exceptions, please check your input and output.")
        print(e)
        raise
    if len(image.shape) > 2 and image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

    try:
        plt.imshow(gray_image, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
        plt.savefig(output_path)
    except FileNotFoundError:
        print("The output path does not exist.")
    except AttributeError:
        print("Please provide a string as the path for the output image file.")
    except Exception as e:
        print("Other exceptions, please check your input and output. ")
        print(e)
        raise
