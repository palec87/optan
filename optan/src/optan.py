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
from PIL import Image
import matplotlib.pyplot as plt
from skimage.transform import iradon, iradon_sart
import cv2
import tomopy as tom


class Optan():
    def __init__(self, folder=None) -> None:
        self.n_sweeps = None
        self.n_steps = None
        self.images_per_step = None
        self.data = None  # derived from raw data with operations, 3d nd.array
        self.data_list = []  # annotation if data list of arrays
        self.raw_data = None  # organized into a dict
        self.file_format = None
        self.image_format = None

        # this should be another class Recon
        self.theta = None
        self.sino = None
        self.center = None
        self.recon = None
        self.recon_log = {}
        self.formats = ['jpg', 'jpeg', 'tiff', 'bmp']
        if folder is not None:
            try:
                self.set_folder(folder)
            except FileNotFoundError:
                print('setting folder to None, use .set_folder(path) to\
                    init existing folder')
                folder = None
        else:
            folder = None

        # for each of these atributes, there is a method
        # to set a value by a user
        self.metadata_attr = [
            'n_sweeps',
            'n_steps',
            'images_per_step',
            'file_type'
            'image_format',
            ]

    def set_folder(self, path: str) -> None:
        """Set folder path, where the data is.

        Args:
            path (str): OS dependent path

        Raises:
            FileNotFoundError: raised if path does
            not exist
        """
        if os.path.exists(path):
            self.folder = path
        else:
            raise FileNotFoundError('Non-existent path.')

    def average_raw_data(self, sweeps='all', frames='all'):
        # preallocation
        self.data = np.zeros((self.n_steps, *self.current_image.shape))
        if sweeps == 'all':
            if frames == 'all':
                arr = np.zeros(
                        (self.n_sweeps * self.images_per_step,
                         *self.current_image.shape),
                )
                for i in range(self.n_steps):
                    for j in range(self.n_sweeps):
                        for k in range(self.images_per_step):
                            arr[k*(j+1), :] = self.single_frame_from_raw((j, i, k))
                    self.data[i, :] = np.mean(arr, axis=0)
                self.data_list = []
            elif frames == 'none':
                raise NotImplementedError
            else:
                try:
                    iterator = iter(frames)
                except TypeError as te:
                    print(te, frames, 'is not iterable')

                arr = np.zeros(
                            (self.n_sweeps * len(iterator),
                             *self.current_image.shape),
                            )
                for i in range(self.n_steps):
                    for j in range(self.n_sweeps):
                        for k in range(len(iterator)):
                            arr[k*(j+1), :] = self.single_frame_from_raw((j, i, iterator[k]))
                    self.data[i, :] = np.mean(arr, axis=0)
                self.data_list = []

        elif sweeps == ' none':
            raise NotImplementedError

    def find_center(self, idx: int):
        """
        Wrapper for the tomopy.find_center_vo() method.
        Finds pixel(column) which corresponds to the rotational
        axis

        Args:
            idx (int): row for finding the rotation axis
        """
        self.center = tom.find_center_vo(self.data, idx)

    def recon_data(self, imin, imax, algorith='fbp'):
        """
        Wrapper for the tomopy.recon method with option to
        select only some rows for reconstruction imin:imax

        Without GPU, speed is an issue, use just few rows
        unless necessary. Count several seconds per row

        Args:
            imin (int): starting row
            imax (int): end row
            algorith (str, optional): list of algos in tomopy docs.
                Defaults to 'fbp'.
        """
        self.recon_log = {'imin': imin, 'imax': imax, 'algo': algorith}
        if self.theta is None:
            self.theta = np.linspace(
                            0., 360.,
                            self.n_steps, endpoint=False
                            ) / 360. * (2 * np.pi)
        # preallocation for the full sinogram
        if self.data is None:
            print('No sinogram, calculatig one')
            self.calc_sinogram()
        
        self.recon = tom.recon(self.data[:, imin:imax, :],
                               theta=self.theta,
                               center=self.center,
                               algorithm=algorith)

    def get_method_list(self):
        """
        List all the methods which you can apply to the Optan
        object.

        Returns:
            list: list of method names
        """
        method_list = [
            attr for attr in dir(self) if callable(getattr(self, attr)) and attr.startswith('__') is False]
        print(method_list)
        return method_list

    def get_instance_attributes(self, with_values=False):
        """
        List all attributes of the Optan object. If you
        them with their respective values, set with_value=True

        Args:
            with_values (bool, optional): If values are printed
                too. Defaults to False.
        """
        if with_values:
            print(self.__dict__)
        else:
            print(self.__dict__.keys())

    def load_folder(self, folder=None):
        """
        Load folder containing Optac experimental data including
        metadata

        Args:
            folder (str, optional): OS dependent path to the data
                folder. Defaults to None.
        """
        if folder:
            self.folder = folder
        self.load_metadata()
        self.load_files()

    def load_files(self):
        """
        Loading experimental data into a dictionary.
        Dictionary solves issues if you do more sweeps or if
        more frames per step are acquired.

        Convention is dict['swNUMBER']['stNUMBER']['NUMBER'] for
        sweep step and frame_per_step

        After loading, current_image is initialized as [sw0][st0][0]
        """
        self.raw_data = {}
        # loading
        for sweep in range(self.n_sweeps):
            self.raw_data['sw'+str(sweep)] = {}
            for step in range(self.n_steps):
                self.raw_data['sw'+str(sweep)]['st'+str(step)] = {}
                for frame in range(self.images_per_step):
                    self.raw_data['sw'+str(sweep)]['st'+str(step)][str(frame)] = {}
                    fname = '_'.join(
                                [str(sweep), str(step), str(frame)])
                    self.raw_data[
                        'sw'+str(sweep)][
                            'st'+str(step)][
                                str(frame)] = self.load_single_frame(fname)
        self.current_image = self.raw_data['sw0']['st0']['0']

    def load_metadata(self):
        """
        Loading metadata, versions of experiments might not
        be backwards compatible, so some attributes might need
        to be set manually, via methods or even directly:
        """
        file_path = os.path.join(self.folder, 'metadata.txt')
        with open(file_path, 'r') as f:
            self.metadata = json.load(f)
        for attr in self.metadata_attr:
            if attr not in self.metadata.keys():
                print('missing metadata')
                continue
            setattr(self, attr, self.metadata[attr])
        print()

    def rotate_frames_90(self, direction='clock'):
        """
        Wrapper for numpy rot90 method, here applied for 3D data.
        So that the axis of rotation is (1,2), and direction is either clock
        anticlock

        Args:
            direction (str, optional): Either clock or anticlock. 
                Defaults to 'clock'.

        Raises:
            AttributeError: if direction is misspelled
        """
        if direction == 'clock':
            self.data = np.rot90(self.data, k=1, axes=(1, 2))
        elif direction == 'anticlock':
            self.data = np.rot90(self.data, k=-1, axes=(1, 2))
        else:
            raise AttributeError('Options are either clock or anticlock')

    def load_single_frame(self, fname):
        """
        Loading single file
        TODO: check if works for both 8 and 16 bit images

        Args:
            fname (str): basename without suffix

        Raises:
            ValueError: if the fileformat is not supported

        Returns:
            nd.array: loaded image
        """
        if self.file_format is None:
            raise ValueError('File format not defined. Use set_file_format()')
        file_path = os.path.join(self.folder, fname + '.' + self.file_format)
        image = np.array(Image.open(file_path))
        return image

    def set_file_format(self, value: str) -> None:
        """
        sets file format of the data images. It should be
        part of experimental metadata

        Args:
            value (str): one of jpg, jpeg, tiff, bmp

        Raises:
            ValueError: If format none of the above
        """
        if value not in self.formats:
            raise ValueError('Not supported file format. See .formats')
        self.file_format = value

    def show_image_raw(self, index: tuple):
        """Display current image from the raw data

        Args:
            index (tuple): tuple of sweep idx, step idx, and image per
            frame idx
        """
        self.current_image = self.single_frame_from_raw(index)
        plt.imshow(self.current_image)
        plt.show()

    def show_image_data(self, idx: int):
        """If raw data processed to data, idx (step) of the
        dataset is shown

        Args:
            idx (int): step of the sweep

        Raises:
            NotImplementedError: if data is a list of arrays,
            this method is not implemented yet.
        """
        if self.data_list == []:
            self.current_image = self.data[idx]
        else:
            raise NotImplementedError

        plt.imshow(self.current_image)
        plt.show()

    def show_image_radon(self, idx=0):
        plt.imshow(self.recon[idx])
        plt.title('Reconstruction')
        plt.show()

    def show_image_sino(self, idx: int):
        plt.imshow(self.sino[:, idx, :])
        plt.title(f'Sinogram at pixel: {idx}')
        plt.show()

    def single_frame_from_raw(self, index: tuple):
        tup = self._index_tuple_to_str(index)
        return self.raw_data[tup[0]][tup[1]][tup[2]]

    def _index_tuple_to_str(self, index: tuple):
        """Converts index into dictionary keys of the \
            raw data

        Args:
            index (tuple): sweep, step, frame_per_step

        Returns:
            tuple: of strings: e.g. ('sw9', 'st6', '8')
        """
        return ('sw' + str(index[0]),
                'st' + str(index[1]),
                str(index[2]))

    # def iradon(self, index: int):
    #     # preallocation for the full sinogram
    #     if self.sino is None:
    #         print('No sinogram, calculatig one')
    #         self.calc_sinogram()

    #     self.theta = np.linspace(0., 360., self.n_steps, endpoint=False)
    #     img = self.sino[:, index, :].transpose()
    #     self.iradon = iradon(
    #                     img,
    #                     theta=self.theta,
    #                     filter_name='ramp')

    def calc_sinogram(self):
        """
        If more frames_per step I take the first.

        TODO: there should be processed data attribute,
        which will be preferential source for sino than
        the raw data
        """
        self.sino = np.zeros(
            (self.n_steps,
             self.current_image.shape[1],
             self.current_image.shape[0]),
        )
        if self.data is None:
            self.fill_sino_from_raw()
        else:
            self.fill_sino_from_data()

    def fill_sino_from_raw(self):
        """
        Create sinogram from the raw data, meaning parsing the
        dictionary of images
        """
        for i in range(self.n_steps):
            print(i, end='\r')
            self.sino[i, :] = self.raw_data['sw0']['st' + str(i)]['0']

        self.data = self.sino.copy()

    def fill_sino_from_data(self):
        """
        If data created from the raw data, either a sino
        is a copy of the 3D matrix, or if data is a list of 3D matrices
        I take the first element of that list.
        """
        if self.data_list == []:
            self.sino = self.data.copy()
        else:
            print('Taking first array for sinogram')
            self.sino = self.data[0]


import types
__all__ = [name for name, thing in globals().items()
           if not (name.startswith('_') or isinstance(thing, types.ModuleType))]
