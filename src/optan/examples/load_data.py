#!/usr/bin/env python
"""
Example of basic loading of the optac data to Optan class

You can also run the script after importing optan module for
example like this:

import optan as o
o.load_data()
"""

import os
import sys
from pathlib import Path
sys.path.insert(0, os.path.abspath('.'))

from optan.main import Optan


def main(show_plots=False):
    print("Example how to load test data from '/data' directory.")
    # initialize Optan class
    exp = Optan()

    # list of available methods
    exp.set_file_format('jpg')
    exp.get_method_list()
    exp.load_folder(
        os.path.join(
            os.getcwd(),
            Path('src/optan/data/shepp_3d'),
        ),
    )

    # two ways to print out dictionary of
    # properties(attributes) of exp.
    exp.__dict__.keys()
    exp.get_instance_attributes(with_values=False)

    # index in order, swee, step, image_per_step
    if show_plots:
        exp.show_image_raw(index=(0, 0, 0))

    # this includes calculating sinogram, if it has not been done
    exp.recon_data(imin=64, imax=65)

    # plot sinogram
    if show_plots:
        exp.show_image_sino(idx=64)

    # show iradon transformed image.
    if show_plots:
        exp.show_image_radon()

    return 'finished'


if __name__ == '__main__':
    main()
