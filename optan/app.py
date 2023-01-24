#!/usr/bin/env python

"""Following tomography acquisition with OPTac software, you
can load, process, correct and analyze (to certain extend) your
tomographs with OPTan.
"""

__author__ = 'David Palecek'
__credits__ = ['Teresa M Correia', 'Rui Guerra']
__license__ = 'GPL'

import sys
import os
from time import gmtime, strftime
import json
import numpy as np
from PIL import Image

from PyQt5 import QtCore, QtWidgets
from .gui.optan_ui import Ui_MainWindow
import pyqtgraph as pg
import tomopy

__author__ = 'David Palecek'
__credits__ = ['Teresa M Correia', 'Rui Guerra']
__license__ = 'GPL'

# config #
#########
pg.setConfigOption('background', 'd')
pg.setConfigOption('foreground', 'k')


class Gui(QtWidgets.QMainWindow):
    def __init__(self, init_values_file):
        super(Gui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.init_file = init_values_file
        self.toggle_lines = False
        self.min_idx = 0
        self.max_idx = 0

        # loaoding
        self.ui.folder_load_btn.clicked.connect(self.folder_load_btn)
        self.ui.deg_collected_list.addItems(['180', '360'])
        self.ui.deg_collected_list.currentIndexChanged.connect(
            self._update_deg_collected
            )
        self.ui.folder_load_go_btn.clicked.connect(self._folder_load_go)

        # averaging
        self.ui.avg_frames.stateChanged.connect(self._update_avg_frames)
        self.ui.avg_sweeps.stateChanged.connect(self._update_avg_sweeps)

        # toggle roi
        self.ui.min_idx.valueChanged.connect(self._update_min_idx)
        self.ui.max_idx.valueChanged.connect(self._update_max_idx)
        self.ui.toggle_lines.toggled.connect(self._update_toggle_idx)

        # sliders
        self.ui.slider_sweep.valueChanged.connect(self._update_sweep_slider)
        self.ui.slider_step.valueChanged.connect(self._update_step_slider)
        self.ui.slider_frame.valueChanged.connect(self._update_frame_slider)
        self.ui.slider_saturation.valueChanged.connect(self._update_sat_slider)

        self.ui.exit_btn.clicked.connect(self.exec_exit_btn)

        try:
            f = open(init_values_file, 'r')
            init_values = json.loads(f.read())
            self._load_gui_values(init_values)
        except FileNotFoundError:
            self._no_init_values()

    def replot(self):
        self.set_current_frame(self.csw, self.cst, self.cfr)
        self.update_data_idx((self.csw, self.cst, self.cfr))
        self.saturate_frame()
        self.update_frame_roi()

    def _update_sweep_slider(self):
        self.csw = self.ui.slider_sweep.value()-1
        self.ui.csw.display(self.csw+1)
        self.replot()

    def _update_step_slider(self):
        self.cst = self.ui.slider_step.value()-1
        self.ui.cst.display(self.cst+1)
        self.replot()

    def _update_frame_slider(self):
        self.cfr = self.ui.slider_frame.value()-1
        self.ui.cfr.display(self.cfr+1)
        self.replot()

    def _update_sat_slider(self):
        self.sat = self.ui.slider_saturation.value()
        self.saturate_frame()
        self.replot()

    def saturate_frame(self):
        try:
            mx = np.amax(self.current_frame)
            self.current_frame = np.clip(
                                    self.current_frame,
                                    0,
                                    int(mx/self.sat))
            print(mx)
        except:
            pass

    def update_slider_ranges(self):
        self.ui.slider_sweep.setRange(1, self.n_sweeps)
        self.ui.slider_step.setRange(1, self.n_steps)
        self.ui.slider_frame.setRange(1, self.frames_per_step)

    def _update_min_idx(self):
        self.min_idx = self.ui.min_idx.value()
        self.update_frame_roi()

    def _update_max_idx(self):
        self.max_idx = self.ui.max_idx.value()
        self.update_frame_roi()

    def _update_toggle_idx(self):
        self.toggle_lines = self.ui.toggle_lines.isChecked()
        self.update_frame_roi()

    def _update_avg_frames(self):
        self.avg_frames = self.ui.avg_frames.isChecked()

    def _update_avg_sweeps(self):
        self.avg_sweeps = self.ui.avg_sweeps.isChecked()

    def _update_deg_collected(self):
        """Either experiment collects 180 or full 360 degree
        angles.
        """
        self.degrees = int(self.ui.deg_collected_list.currentText())

    def _update_folder_path(self):
        """Update saving folder path from UI"""
        self.ui.folder_path.setText(self.folder)

    def _load_gui_values(self, d):
        try:
            print('reading values')
            # self.ui.motor_speed.setValue(d['motor_speed'])
            # self.ui.angle.setValue(d['angle'])
            # self.ui.motor_steps.setValue(d['motor_steps'])
            # self.ui.n_sweeps.setValue(d['n_sweeps'])
            # self.ui.frame_rate.setValue(d['frame_rate'])
            # self.ui.camera_port.setValue(d['camera_port'])
            # self.ui.frames2avg.setValue(d['frames_to_avg'])
            # self.ui.n_frames.setValue(d['n_frames'])
            # self.ui.accum_shots.setChecked(d['accum_shots'])
            self.ui.toggle_lines.setChecked(d['toggle_lines'])
            # self.ui.radon_idx.setValue(d['radon_idx'])
            self.ui.min_idx.setValue(d['min_idx'])
            self.ui.max_idx.setValue(d['max_idx'])
            self.ui.deg_collected_list.setCurrentIndex(d['degrees_collected'])
            # self.ui.motor_type_list.setCurrentIndex(d['motor_type_idx'])
            self.folder = d['folder_path']
            self._update_folder_path()
        except KeyError:
            self.append_history('Error reading values')
            self._no_init_values()

    def _save_gui_values(self):
        vals = {}
        # vals['motor_speed'] = self.motor_speed
        # vals['angle'] = self.angle
        # vals['motor_steps'] = self.motor_steps
        # vals['n_sweeps'] = self.n_sweeps
        # vals['frame_rate'] = self.frame_rate
        # vals['camera_port'] = self.camera_port
        # vals['frames_to_avg'] = self.frames_to_avg
        # vals['n_frames'] = self.n_frames
        # vals['accum_shots'] = self.accum_shots
        vals['toggle_lines'] = self.toggle_lines
        # vals['radon_idx'] = self.radon_idx
        vals['min_idx'] = self.min_idx
        vals['max_idx'] = self.max_idx
        vals['degrees_collected'] = self.ui.deg_collected_list.currentIndex()
        # vals['motor_type_idx'] = self.motor_type
        vals['folder_path'] = self.folder
        with open(self.init_file, 'w') as f:
            f.write(json.dumps(vals))

    def _no_init_values(self):
        # self.ui.motor_speed.setValue(500)
        # self.ui.angle.setValue(400)
        # self.ui.motor_steps.setValue(4)
        # self.ui.n_sweeps.setValue(1)
        # self.ui.frame_rate.setValue(24)
        # self.ui.camera_port.setValue(1)
        # self.ui.frames2avg.setValue(10)
        # self.ui.n_frames.setValue(10)
        # self.ui.accum_shots.setChecked(False)
        self.ui.toggle_lines.setChecked(False)
        # self.ui.radon_idx.setValue(10)
        self.ui.min_idx.setValue(0)
        self.ui.max_idx.setValue(250)
        self.ui.deg_collected_list.setCurrentIndex(0)
        # self.ui.motor_type_list.setCurrentIndex(0)
        self.folder = os.getcwd()
        self._update_folder_path()

    def _folder_load_go(self):
        """Loads data into a single tuple of nd arrays.
        TODO: take care of the size of the directory

        Experimental metadata defines the data shape
        1. number of frames taken per frame
        2. Steps per sweep
        3. Number of sweeps
        """
        self.load_metadata()
        self.raw_data = {}
        # loading
        for sweep in range(self.n_sweeps):
            self.raw_data['sw'+str(sweep)] = {}
            for step in range(self.n_steps):
                self.raw_data['sw'+str(sweep)]['st'+str(step)] = {}
                for frame in range(self.frames_per_step):
                    self.raw_data['sw'+str(sweep)]['st'+str(step)][str(frame)] = {}
                    fname = '_'.join(
                                [str(sweep), str(step), str(frame)])
                    self.raw_data[
                        'sw'+str(sweep)][
                            'st'+str(step)][
                                str(frame)] = self.load_single_frame(fname)
        self.append_history('Data loaded')
        self.set_current_frame()
        self.update_frame_roi()
        self.update_slider_ranges()
        # self.current_frame_display()

    def set_current_frame(self, sw=0, st=0, fr=0):
        self.raw_frame = np.rot90(
            self.raw_data['sw'+str(sw)]['st'+str(st)][str(fr)],
        )
        self.update_data_idx((0, 0, 0))

    def update_data_idx(self, tup):
        self.csw, self.cst, self.cfr = tup

    def update_frame_roi(self):
        if self.toggle_lines:
            self.current_frame = self.raw_frame[:,
                                        self.min_idx:self.max_idx]
        else:
            self.current_frame = self.raw_frame
        self.current_frame_display()

    def load_single_frame(self, fname):
        file_path = os.path.join(self.folder, fname+'.jpg')
        image = np.array(Image.open(file_path))
        # data = np.loadtxt(file_path)#, dtype=eval(self.dynamic_range))
        return image

    def load_metadata(self):
        file_path = os.path.join(self.folder, 'metadata.txt')
        with open(file_path, 'r') as f:
            self.metadata = json.load(f)
        self.n_sweeps = self.metadata['n_sweeps']
        self.n_steps = self.metadata['n_steps']
        self.frames_per_step = self.metadata['images_per_step']
        self.dynamic_range = self.metadata['dynamic_range']

    def folder_load_btn(self):
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(
                                self, "Select Directory"))
        if not folder:
            self.append_history('no change in data folder')
            return

        self.folder = folder
        self._update_folder_path()
        self.append_history('new data folder selected')

    ############
    # Plotting #
    ############
    def create_plots(self):
        '''defines defaults for each graph'''
        self.ui.frame_display.plotItem.setLabels(
            left='pixel Y',
            bottom='pixel X'
        )

    def current_frame_display(self):
        '''last frame plot in Align tab'''
        try:
            self.ui.frame_display.clear()
            img = pg.ImageItem(image=self.current_frame)
            self.ui.frame_display.plotItem.addItem(
                img,
                clear=True,
                pen='b'
            )
        except Exception as e:
            self.append_history(f'Error Plotting Frame, {e}')
        return

    ###########
    # Logging #
    ###########
    def append_history(self, message):
        self.ui.history.appendPlainText(message)

    def exec_exit_btn(self):
        '''
        will exit from gui. some safeguarding
         in case exit is called before stop
         '''
        self._save_gui_values()
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    init_values_file = os.path.join(os.getcwd(), 'lif.json')
    gui = Gui(init_values_file=init_values_file)
    gui.show()
    gui.create_plots()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
