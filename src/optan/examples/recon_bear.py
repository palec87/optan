#! \bin\env\python
import os
import json
import cv2
import numpy as np

import time
import threading

from tomopy.recon.rotation import find_center_vo
import tomopy as tom


def fill_matrix2(arr, img_idx, metadata, invert=True):
    for i in range(metadata['n_steps']):
        name = '0_' + str(i) + '_' + str(img_idx) + ENDING
        threadProcess = threading.Thread(name='simplethread',
                                         target=helper,
                                         args=[i, name, arr, invert])
        threadProcess.daemon = True
        threadProcess.start()


def helper(i, name, arr, invert):
    print(i, name, end='\r')
    if invert:
        img, mx = get_image(name, NBITS)
        arr[i, :] = mx-img
    else:
        arr[i, :] = get_image(name, NBITS)[0]


def get_image(name, nbits):
    if ENDING == '.jpg':
        img = cv2.imread(name)
        img = img[:, :, 0]
    elif ENDING == '.tiff':
        if nbits == 8:
            img = cv2.imread(name)
        else:
            img = cv2.imread(name, cv2.IMREAD_UNCHANGED)
    else:
        img = np.loadtxt(name)
    return img[:, :, 0], np.amax(img[:, :, 0])


def binx(idx, bin_factor, arr_in, arr_out):
    arr_out[idx] = arr_in[idx].reshape(
                                arr_in.shape[1]//bin_factor,
                                bin_factor,
                                arr_in.shape[2]//bin_factor,
                                bin_factor,
                            ).mean(3).mean(1)


def recon_thread(idx, center, arr, arr_out):
    arr_out[idx] = tom.recon(arr[:, idx:idx+1, :],
                             THETA,
                             center=center,
                             sinogram_order=False,
                             algorithm='art').squeeze()


def main():
    folder = 'C:\\Users\\David Palecek\\Documents\\UAlg\\my_opt\\Data'
    exp_folder = '\\230315-16-45-27\\'
    global NBITS
    NBITS = 8
    global IDX
    ibeg = 50
    iend = 500
    binning = 4

    os.chdir(''.join([folder, exp_folder]))

    f = open('metadata.txt', "r")
    metdat = json.loads(f.read())
    file_list = os.listdir()

    print('METADATA')
    print(metdat)

    global ENDING
    if file_list[0][-3:] == '.gz':
        ENDING = '.gz'
        img = np.loadtxt(file_list[0])
    elif file_list[0][-4:] == '.jpg':
        ENDING = '.jpg'
        img = cv2.imread(file_list[0], cv2.IMREAD_UNCHANGED)
    elif file_list[0][-4:] == 'tiff':
        ENDING = '.tiff'
        # img = cv2.imread(file_list[0])
        img = cv2.imread(file_list[0], cv2.IMREAD_UNCHANGED)

    full_scan = np.zeros((metdat['n_steps'], img.shape[0], img.shape[1]))

    #############
    n_steps = metdat['n_steps']
    beg = time.perf_counter()
    fill_matrix2(full_scan, 0, metadata=metdat, invert=True)
    end = time.perf_counter()
    print('Loading took:', np.round(end-beg, 2), 's')

    #############
    # binning ###
    #############
    print('Running binning')
    if binning == 0:
        data = full_scan.copy()
    else:
        binned = np.zeros((full_scan.shape[0],
                           full_scan.shape[1]//binning,
                           full_scan.shape[2]//binning), dtype=np.int16)

        beg = time.perf_counter()
        for i in range(n_steps):
            threadProcess = threading.Thread(
                                name='simplethread',
                                target=binx,
                                args=[i, binning, full_scan, binned],
                            )
            threadProcess.daemon = True
            threadProcess.start()
        end = time.perf_counter()
        print('Binning took:', np.round(end-beg, 2), 's')

        data = binned.copy()

    IDX = data.shape[1] // 2

    # settings for tomopy
    global THETA
    THETA = np.linspace(
                0., 360.,
                n_steps, endpoint=False
                ) / 360. * (2 * np.pi)
    print('full shape:', full_scan.shape)
    print('data shape:', data.shape)
    center = []
    for i in range(int((iend-ibeg)/100)):
        center.append(find_center_vo(data[:n_steps//2, :, :],
                                     ind=ibeg+i*100+10,
                                     ratio=0.5))
    print(np.argmax(data.sum(axis=(0, 2))))
    center.append(find_center_vo(data[:n_steps//2, :, :],
                                 smin=-50, smax=50,
                                 ind=np.argmax(data.sum(axis=(0, 2))),
                                 ratio=0.5))
    # center = find_center_vo(data[:n_steps//2, :, :], ind=IDX, ratio=0.5)
    print('center estimate:', center, np.mean(center))

    r1 = tom.recon(data[:, IDX:IDX+1, :], THETA, center=np.mean(center),
                   sinogram_order=False, algorithm='art')

    CENTER = center[-1]
    ##########
    print('Running FULL reconstruction')
    beg = time.perf_counter()
    dim = iend-ibeg
    data_recon = np.zeros((data.shape[1], *r1.squeeze().shape))
    threads = [None] * dim
    for i in range(dim):
        print(i, end='\r')
        threads[i] = threading.Thread(target=recon_thread,
                                      args=[i+ibeg, CENTER, data, data_recon])
        threads[i].start()

    for i in range(len(threads)):
        threads[i].join()
    end = time.perf_counter()
    print('Reconstruction took:', np.round(end-beg, 2), 's')

    # rescaling and saving as uint8
    mx, mn = np.amax(data_recon), np.amin(data_recon)
    if mn < 0:
        print('rescaling', mn, mx)
        recon_int = np.asarray((data_recon - mn)*254/(mx-mn), dtype=np.uint8)

    print('Saving')
    to_save = recon_int[ibeg:iend]
    np.save('recon4x', to_save)


if __name__ == '__main__':
    main()
