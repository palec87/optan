#!/usr/bin/env python3

"""
After correcting raw images, preprocess data cube for the
reconstruction

1. Center of rotation
2. Rotation tilt (I need experimental procedure too)
3. cut out volume for the reconstruction
"""

import os
from pathlib import Path
import numpy as np
from PIL import Image

from tomopy.recon.rotation import find_center_vo
import tomopy as tom


class Opt(object):
    def __init__(self, folder, depth, format) -> None:
        self.formats = ['tiff', 'jpeg']
        self.depths = [np.int8, np.int16]

        self.folder = self.set_folder(folder)
        self.depth = self.set_depth(depth)
        self.file_format = self.set_file_format(format)

    def set_file_format(self, format: str) -> str:
        """
        sets file format of the data images. It should be
        part of experimental metadata. Currently supports jpeg and tiff

        Args:
            format (str): one of the supported formats

        Raises:
            ValueError: If format none of the above

        Returns:
            str: validated/supported file type
        """
        if format not in self.formats:
            raise ValueError(
                'Unsupported file format. See .formats for options',
                )
        return format

    def set_depth(self, depth: np.dtype) -> np.dtype:
        """Set expected depth of the images

        Args:
            depth (np.dtype): Expects int type, currently np.int8 or
             np.int16

        Raises:
            ValueError: If depth not in supported options

        Returns:
            np.dtype: validated depth type
        """
        if depth not in self.depths:
            raise ValueError('Unsupported depth, etiher np.int8 or np.int16')
        return depth

    def set_folder(self, path: str) -> Path:
        """Set folder path, where the data is.

        Args:
            path (str): OS dependent path

        Raises:
            FileNotFoundError: raised if path does not exist

        Returns:
            pathlib.Path: path which exists
        """
        if os.path.exists(Path(path)):
            return Path(path)
        else:
            raise FileNotFoundError('Non-existent path.')

    def load_folder(self, mode='simple'):
        if mode == 'simple':
            self.load_folder_simple()
        # nested dataset, step-wise acquisition, with averages and sweeps
        # can be averaged separately later
        elif mode == 'nested':
            raise NotImplementedError
            self.load_folder_nested(average=False)
        elif mode == 'nested_av':
            raise NotImplementedError
            self.load_folder_nested(average=True)
        else:
            raise ValueError('Wrong mode option')

    def load_folder_simple(self):
        files = [file for file in self.folder.iterdir()
                 if file.name.endswith(self.file_format)]

        # load first one for preallocation
        f0 = np.array(Image.open(files[0]), dtype=self.depth)
        # preallocate
        data = np.empty((len(files), *f0.shape), dtype=self.depth)
        for i in range(len(files)):
            # construct fname
            fname = f'{i:04d}.{self.file_format}'
            # load data
            data[i] = np.array(Image.open(self.folder.joinpath(fname)),
                               dtype=self.depth)
            print(i, end='\r')
        self.data = data
        self.n_steps = len(files)


class Opt_preprocess(Opt):
    def __init__(self, folder, depth, format) -> None:
        super().__init__(folder, depth, format)


class Recon(object):
    def __init__(self, data: Opt):
        self.data = data
        self.theta = np.linspace(
                        0., 360., self.data.n_steps, endpoint=False
                        ) / 360. * (2 * np.pi)

    def find_center_single(self):
        try:
            center = find_center_vo(
                        self.data.data[:self.data.n_steps//2, :, :],
                        ind=self.line,
                        ratio=0.5)
        except NameError:
            print('Load data first via load_folder()')

        self.center = center
        print(f'center found at {self.center}')
        return center

    def recon_single(self, line):
        self.line = line
        self.find_center_single()

        self.recon = tom.recon(
                    self.data.data[:, self.line:self.line+1, :], self.theta,
                    center=self.center,  # np.mean(center),
                    sinogram_order=False, algorithm='art')
