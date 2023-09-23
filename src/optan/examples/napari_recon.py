import os
import numpy as np
import napari

folder = 'C:\\Users\\David Palecek\\Documents\\Python_projects\\optan\\optan'
exp_folder = '\\nbs\\'

os.chdir(''.join([folder, exp_folder]))
cut = 10

recon = np.load('recon4x_cont.npy')

viewer = napari.view_image(recon[:, cut:-cut, cut:-cut])
napari.run()
