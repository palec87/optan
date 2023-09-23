#!/usr/bin/env python

"""
After OPT acquisition this scripts allows to run corrections and
save data in a new folder.
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2
from pathlib import Path
import gc
import json

import sys
import os
sys.path.insert(1, os.path.abspath(
    'C:\\Users\\David Palecek\\Documents\\Python_projects\\optac\\optac\\src\\optac\\'))
sys.path.insert(1, os.path.abspath(
    'C:\\Users\\David Palecek\\Documents\\Python_projects\\optan\\optan'))

from helpers.corrections import Correct
from helpers.img_processing import (
    img_to_int_type
)

os.chdir('C:\\Users\\David Palecek\\Documents\\Python_projects\\optan')
from src import optan


folder_base = Path('C:/Users/David Palecek/Documents/UAlg/my_opt/Data')
fcorr = '230919-13-37-10'
fdata = '230919-13-47-22'

folder_corr = folder_base.joinpath(fcorr)
folder_exp = folder_base.joinpath(fdata)

dhot = cv2.imread(str(folder_corr.joinpath('hot_pixels13-37-10.tiff')),
                  cv2.IMREAD_UNCHANGED)
ddark = cv2.imread(str(folder_corr.joinpath('dark_field13-39-53.tiff')),
                   cv2.IMREAD_UNCHANGED)
dflat = cv2.imread(str(folder_corr.joinpath('flat_field13-40-35.tiff')),
                   cv2.IMREAD_UNCHANGED)

do_dark = True
do_flat = True
do_hot = True
do_int = True

save_after_hot = True

################
# end of setup #
################
# correction class
corr = Correct(hot=dhot, std_mult=7, dark=ddark, bright=dflat)

# initiate optan
exp = optan.Optan()
exp.set_file_format('tiff')
exp.load_folder(folder_exp)
exp.average_raw_data()
print('data loading and averaging done.')

# extract data from the optan
# I suppose optan could load corr class too (matter of organization)
data = img_to_int_type(exp.data, np.int16)
print(f'data casted to {data.dtype}.')

if do_dark:
    for i, img in enumerate(data):
        data[i] = corr.correct_dark(img)
    print('Dark correction done')

if do_flat:
    for i, img in enumerate(data):
        data[i] = corr.correct_bright(img)
    print('Flat correction done')

if do_hot:
    for i, img in enumerate(data):
        print(i, end='\r')
        data[i] = corr.correct_hot(img)
    print('Hot correction done')

# saving
if save_after_hot:
    folder_save = folder_base.joinpath(fdata+'_corr')
    if os.path.isdir(folder_save) is False:
        os.mkdir(folder_save)

    for i, img in enumerate(data):
        cv2.imwrite(str(folder_save.joinpath(f'{i:03d}.tiff')), img)

    # dictionary of additional info
    info = {'dark-corr': do_dark,
            'flat-corr': do_flat,
            'hot-corr': do_hot,
            }
    with open(folder_save.joinpath("info.json"), "w") as f:
        json.dump(info, f)

    print('saving done')

gc.collect()

if do_int:
    data_icorr = corr.correct_int(data, use_bright=False,
                                  mode='integral_bottom')
    folder_save = folder_base.joinpath(fdata + '_corr_int')
    if os.path.isdir(folder_save) is False:
        os.mkdir(folder_save)

    for i, img in enumerate(data_icorr):
        cv2.imwrite(str(folder_save.joinpath(f'{i:03d}.tiff')), img)

    info = {'dark-corr': do_dark,
            'flat-corr': do_flat,
            'hot-corr': do_hot,
            'do_int': do_int,
            }
    with open(folder_save.joinpath("info.json"), "w") as f:
        json.dump(info, f)
    
    print('saving done')


# integrated intensity
d1 = np.mean(data_icorr, axis=(1, 2))
d2 = np.mean(data, axis=(1, 2))

fig, ax = plt.subplots(1, 2, figsize=(14, 4))
ax[0].plot(d2, label='fluctuating data')
ax[0].plot(d1, label='int corrected')
ax[0].set_xlabel('img number')
ax[0].set_ylabel('Norm. integrated int over img')
ax[0].legend()

ax[1].plot(corr.stack_int)
ax[1].set_xlabel('img number')
ax[1].set_ylabel('lamp fluct. (mean counts over correction area)')
plt.show()
