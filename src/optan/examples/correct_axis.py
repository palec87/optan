#!/usr/bin/env python
"""
Real fish data to demonstrate correction of the rotation axis

You can also run the script after importing optan module for
example like this:

import optan as o
o.correct_axis(folder_to_process)
"""

import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))

from src.optan.main import Optan


def main(folder):
    print("Example how to load test data from '/data' directory.")
    # initialize Optan class
    exp = Optan()
    exp.set_file_format('jpg')
    exp.load_folder(folder)

    exp.show_image_raw(index=(0, 0, 0))

    exp.average_raw_data()

    print(exp.data.shape)

    exp.rotate_frames_90('anticlock')
    print(exp.data.shape)

    exp.calc_sinogram()

    exp.recon_data(imin=360, imax=365)

    exp.show_image_radon()


if __name__ == '__main__':
    main(sys.argv[1])
