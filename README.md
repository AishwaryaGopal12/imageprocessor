# imageprocessor 

![](https://github.com/wang-rui/imageprocessor/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/wang-rui/imageprocessor/branch/main/graph/badge.svg)](https://codecov.io/gh/wang-rui/imageprocessor) ![Release](https://github.com/wang-rui/imageprocessor/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/imageprocessor/badge/?version=latest)](https://imageprocessor.readthedocs.io/en/latest/?badge=latest)

This cookiecutter creates a boilerplate for a Python project.

## Package Overview

Images form a significant part of the data in todays world. However, at most times, these images cannot be used directly and need to be processed in order to extract some information from them. PyGram aims to make the image processing task easy and intuitive. With Pygram, users can rotate the images, convert it to greyscale, flip the image in either horizontal or vertical direction and add padding to the images. The four functions contained in this package are :

- `flipping`: This function can be used to flip the image either in the horizontal or vertical direction. The arguments to be passed to this function are the path of the input image, "h" or "v" indicating the direction of the flip and the path where the output image has to be saved.

- `greyscale`: The greyscale function converts a color image into a greyscale image. This function takes the path of the input image and the path where the resultant image has to be stored as arguments. 

- `padding`: This function can be used to add padding to the the borders of an image. The path of the input image, the width of padding required and the path where the output image has to be saved are the required arguments for this function.

- `rotate`: The rotate function rotates an image by the specified number of degrees. This function takes the path of the input image, degrees to rotate by and the path where the resultant image has to be stored as arguments.

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ imageprocessor
```

## Features

- TODO

## Dependencies

- TODO

## Usage

- TODO

## Documentation

The official documentation is hosted on Read the Docs: https://imageprocessor.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/wang-rui/imageprocessor/graphs/contributors).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
