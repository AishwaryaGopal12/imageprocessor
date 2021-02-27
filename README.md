# imageprocessor 

![](https://github.com/wang-rui/imageprocessor/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/wang-rui/imageprocessor/branch/main/graph/badge.svg)](https://codecov.io/gh/wang-rui/imageprocessor) ![Release](https://github.com/wang-rui/imageprocessor/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/imageprocessor/badge/?version=latest)](https://imageprocessor.readthedocs.io/en/latest/?badge=latest)

This cookiecutter creates a boilerplate for a Python project.

## Overview

Images form a significant part of the data in todays world. However, at most times, these images cannot be used directly and need to be processed in order to extract some information from them. PyGram aims to make the image processing task easy and intuitive. With Pygram, users can rotate the images, convert it to greyscale, flip the image in either horizontal or vertical direction and add padding to the images.

## Functions

- `flipping`: This function can be used to flip the image either in the horizontal or vertical direction.

- `greyscale`: The greyscale function converts a color image into a greyscale image.  

- `padding`: This function can be used to add padding to the the borders of an image. 

- `rotate`: The rotate function rotates an image by the specified number of degrees. 

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/ PyGram
```

## Dependencies

- Numpy

## Usage

`from pygram.flipping import flipping`

`from pygram.greyscale import greyscale`

`from pygram.padding import padding`

`from pygram.rotate import rotate`

1. `flipping(input_path, direction, output_path)`

Arguments:\
    - `input_path`: path to input image\
    - `direction`: direction of flip ("h" for horizontal/ "v" for vertical)\
    - `output_path`: path to output image

2. `greyscale(input_path, output_path)`

Arguments:\
    - `input_path`: path to input image\
    - `output_path`: path to output image

3. `padding(input_path, width, output_path)`

Arguments:\
    - `input_path`: path to input image\
    - `width`: number of pixels of padding to be added\
    - `output_path`: path to output image\

4. `rotate(input_path, degrees, output_path)`

Arguments:\
    - `input_path`: path to input image\
    - `degrees`: the degrees to rotate the image by\
    - `output_path`: path to output image\

## Documentation

The official documentation is hosted on Read the Docs: https://pygram.readthedocs.io/en/latest/

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/UBC-MDS/PyGram/blob/main/CONTRIBUTORS.md).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
