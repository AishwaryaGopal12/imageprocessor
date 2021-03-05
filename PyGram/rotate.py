# This script is for the rotate function
import numpy as np
import matplotlib.pyplot as plt
import cv2


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

    # Get the image size
    image_size = (image.shape[1], image.shape[0])
    image_center = tuple(np.array(image_size) / 2)

    # Convert the OpenCV 3x2 rotation matrix to 3x3
    rot_mat = np.vstack([cv2.getRotationMatrix2D(image_center, degree, 1.0), [0, 0, 1]])

    rot_mat_notranslate = np.matrix(rot_mat[0:2, 0:2])

    # Shorthand for below calcs
    image_w2 = image_size[0] * 0.5
    image_h2 = image_size[1] * 0.5

    # Obtain the rotated coordinates of the image corners
    rotated_coords = [
        (np.array([-image_w2, image_h2]) * rot_mat_notranslate).A[0],
        (np.array([image_w2, image_h2]) * rot_mat_notranslate).A[0],
        (np.array([-image_w2, -image_h2]) * rot_mat_notranslate).A[0],
        (np.array([image_w2, -image_h2]) * rot_mat_notranslate).A[0],
    ]

    # Find the size of the new image
    x_coords = [pt[0] for pt in rotated_coords]
    x_pos = [x for x in x_coords if x > 0]
    x_neg = [x for x in x_coords if x < 0]

    y_coords = [pt[1] for pt in rotated_coords]
    y_pos = [y for y in y_coords if y > 0]
    y_neg = [y for y in y_coords if y < 0]

    right_bound = max(x_pos)
    left_bound = min(x_neg)
    top_bound = max(y_pos)
    bot_bound = min(y_neg)

    new_w = int(abs(right_bound - left_bound))
    new_h = int(abs(top_bound - bot_bound))

    # We require a translation matrix to keep the image centred
    trans_mat = np.matrix(
        [
            [1, 0, int(new_w * 0.5 - image_w2)],
            [0, 1, int(new_h * 0.5 - image_h2)],
            [0, 0, 1],
        ]
    )

    # Compute the tranform for the combined rotation and translation
    affine_mat = (np.matrix(trans_mat) * np.matrix(rot_mat))[0:2, :]

    # Apply the transform
    result = cv2.warpAffine(image, affine_mat, (new_w, new_h), flags=cv2.INTER_LINEAR)

    # exception handling
    try:
        plt.imshow(result)
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