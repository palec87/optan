#!/usr/bin/env python

"""Following tomography acquisition with OPTac software, you
can load, process, correct and analyze (to certain extend) your
tomographs with OPTan.

Loading OPTan module, you use notebooks, scripts or CLI to work on the data

Or try a GUI interface (more bugged) by running a main.py or installing
the executable
"""

__author__ = 'David Palecek'
__credits__ = ['Teresa M Correia', 'Rui Guerra']
__license__ = 'GPL'


# import tomopy
import numpy as np
import json
import os


class Optan():
    def __init__(self, folder=None) -> None:
        if folder is not None:
            try:
                self.set_folder(folder)
            except FileNotFoundError:
                print('setting folder to None, use .set_folder(path) to\
                    init existing folder')
                folder = None
        else:
            folder = None

        # for each of this atributes, there is a method to set a value by a user
        self.metadata_attr = [
            'n_sweeps',
            'n_steps',
            'images_per_step',
            'dynamic_range',
            ]

    def set_folder(self, path: str) -> None:
        if os.path.exists(path):
            self.folder = path
        else:
            raise FileNotFoundError('Non-existent path.')

    def load_folder(self, folder=None):
        if folder:
            self.folder = folder
        self.load_metadata(self)

    def load_metadata(self):
        file_path = os.path.join(self.folder, 'metadata.txt')
        with open(file_path, 'r') as f:
            self.metadata = json.load(f)
        for attr in self.metadata_attr:
            if attr not in self.matadata.keys():
                raise

    def rotate_frames_90(direction='clock'):
        return

    def load_single_frame(self, fname):
        return
