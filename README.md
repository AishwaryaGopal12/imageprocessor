# ImageProcessor

![](https://github.com/wang-rui/imageprocessor/workflows/build/badge.svg) [![codecov](https://codecov.io/gh/wang-rui/imageprocessor/branch/main/graph/badge.svg)](https://codecov.io/gh/wang-rui/imageprocessor) ![Release](https://github.com/wang-rui/imageprocessor/workflows/Release/badge.svg) [![Documentation Status](https://readthedocs.org/projects/imageprocessor/badge/?version=latest)](https://imageprocessor.readthedocs.io/en/latest/?badge=latest)

This cookiecutter creates a boilerplate for a Python project.

## Overview

Images form a significant part of the data in today's world. Whether you want to enhance your poorly-lit profile picture or analyze satellite images, filters are your best friends. In scientific image processing, at most times, the images cannot be used directly and need to be processed to extract information from them. ImageProcessor aims to make the image processing task easy and intuitive. With ImageProcessor, users can rotate the image, convert it to greyscale, flip it in either a horizontal or vertical direction, and add padding to it (frame). 

## Python ecosystem

To fit the package in the Python ecosystem, we are enhancing an existing package called [InstaPy](https://github.com/UBC-MDS/InstaPy) by adding more features. Moreover, we're planning to add some of the image processing functions from [DSCI 511, lab3](https://github.ubc.ca/MDS-2020-21/DSCI_511_py-prog_students/blob/master/release/lab3/lab3_release.ipynb) and [DSCI 572](https://github.ubc.ca/MDS-2020-21/DSCI_572_sup-learn-2_students) into the package for use by MDS instructors in the future. 

## Functions

- `flipping`: This function can be used to flip the image either in the horizontal or vertical direction.

- `greyscale`: The greyscale function converts a color image into a greyscale image.  

- `padding`: This function can be used to add padding to the the borders of an image. 

- `rotate`: The rotate function rotates an image by the specified number of degrees. 

## Installation

```bash
$ pip install -i https://test.pypi.org/simple/imageprocessor
```

## Dependencies

- Numpy, matplotlib, skimage

## Usage

`from imageprocessor.flipping import flipping`

`from imageprocessor.greyscale import greyscale`

`from imageprocessor.padding import padding`

`from imageprocessor.rotate import rotate`

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
    - `output_path`: path to output image

4. `rotate(input_path, degrees, output_path)`

Arguments:\
    - `input_path`: path to input image\
    - `degrees`: the degrees to rotate the image by\
    - `output_path`: path to output image

## Documentation

The official documentation is hosted on Read the Docs: https://imageprocessor.readthedocs.io/en/latest/

## Contributors

We welcome all contributions to this project! If you notice a bug, or have a feature request, please open up an issue here. If you'd like to contribute a feature or bug fix, you can fork our repo and submit a pull request. We will review pull requests within 7 days. All contributors must abide by our [code of conduct](https://github.com/UBC-MDS/PyGram/blob/main/CONDUCT.rst).

### Credits

This package was created with Cookiecutter and the UBC-MDS/cookiecutter-ubc-mds project template, modified from the [pyOpenSci/cookiecutter-pyopensci](https://github.com/pyOpenSci/cookiecutter-pyopensci) project template and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage).
