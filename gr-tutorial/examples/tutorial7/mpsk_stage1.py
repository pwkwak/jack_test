#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Mpsk Stage1
# Generated: Tue Feb 13 21:37:51 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from rms_agc import rms_agc  # grc-generated hier_block
import sip


class mpsk_stage1(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Mpsk Stage1")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Mpsk Stage1")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "mpsk_stage1")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.samp_per_sym = samp_per_sym = 4
        self.bps = bps = 500e3
        self.decimation = decimation = int(samp_rate/(bps*samp_per_sym))
        self.transition_bw = transition_bw = samp_rate/(2*decimation*5)
        self.nfilts = nfilts = 64
        self.tw2 = tw2 = bps/(2*decimation)
        self.tw = tw = 50000
        self.timing_loop_bw = timing_loop_bw = 6.28/100.0
        self.taps = taps = firdes.low_pass(1,samp_rate,samp_rate/(2*decimation), transition_bw)
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(samp_per_sym), 0.35, 11*samp_per_sym*nfilts)
        self.qpsk3 = qpsk3 = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([3, 1, 0, 2]), 4, 2, 2, 1, 1).base()
        self.numtap = numtap = 2
        self.excess_bw = excess_bw = 0.35
        self.cutoff_freq2 = cutoff_freq2 = bps/(2*decimation)
        self.cutoff_freq = cutoff_freq = 0.35*bps
        self.channel_freq = channel_freq = 2400039000
        self.center_freq = center_freq = 2.3995e9
        self.arity = arity = 4

        ##################################################
        # Blocks
        ##################################################
        self._tw_range = Range(0, samp_rate/decimation, 10, 50000, 200)
        self._tw_win = RangeWidget(self._tw_range, self.set_tw, "tw", "counter_slider", float)
        self.top_layout.addWidget(self._tw_win)
        self._numtap_range = Range(1, 100, 1, 2, 200)
        self._numtap_win = RangeWidget(self._numtap_range, self.set_numtap, "numtap", "counter_slider", float)
        self.top_layout.addWidget(self._numtap_win)
        self._cutoff_freq_range = Range(0, samp_rate/decimation, 10, 0.35*bps, 200)
        self._cutoff_freq_win = RangeWidget(self._cutoff_freq_range, self.set_cutoff_freq, "cutoff_freq", "counter_slider", float)
        self.top_layout.addWidget(self._cutoff_freq_win)
        self._channel_freq_range = Range(2.4e9 - samp_rate/2, 2.4e9 + samp_rate/2, 100, 2400039000, 200)
        self._channel_freq_win = RangeWidget(self._channel_freq_range, self.set_channel_freq, "channel_freq", "counter_slider", float)
        self.top_grid_layout.addWidget(self._channel_freq_win, 2,2,1,1)
        self._tw2_range = Range(0, bps/decimation, 10, bps/(2*decimation), 200)
        self._tw2_win = RangeWidget(self._tw2_range, self.set_tw2, "tw2", "counter_slider", float)
        self.top_layout.addWidget(self._tw2_win)
        self._timing_loop_bw_range = Range(0.0, 0.2, 0.01, 6.28/100.0, 200)
        self._timing_loop_bw_win = RangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, "Time: BW", "slider", float)
        self.top_layout.addWidget(self._timing_loop_bw_win)
        self.rms_agc_0 = rms_agc(
            alpha=1e-2,
            reference=0.5,
        )
        self.qtgui_time_sink_x_2_0_0_1 = qtgui.time_sink_c(
        	1024, #size
        	int(samp_rate/decimation), #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_2_0_0_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_2_0_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_2_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_2_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2_0_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_2_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_2_0_0_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_2_0_0_1.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_2_0_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2_0_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_2_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_2_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_2_0_0_1_win, 3,0,1,2)
        self.qtgui_time_sink_x_2_0_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_2_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_2_0_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_2_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_2_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_2_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_2_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_2_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_2_0_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_2_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_2_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_2_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_2_0_0_0_win, 1,0,1,2)
        self.qtgui_time_sink_x_2_0 = qtgui.time_sink_c(
        	1024, #size
        	bps, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_2_0.set_update_time(0.10)
        self.qtgui_time_sink_x_2_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_2_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_2_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2_0.enable_autoscale(False)
        self.qtgui_time_sink_x_2_0.enable_grid(False)
        self.qtgui_time_sink_x_2_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_2_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_2_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_2_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_2_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_2_0_win = sip.wrapinstance(self.qtgui_time_sink_x_2_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_2_0_win, 5,0,1,2)
        self.qtgui_freq_sink_x_1_0_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	int(samp_rate/decimation), #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_1_0_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1_0_0_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0_0_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_0_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_0_0_win, 2,0,1,1)
        self.qtgui_freq_sink_x_1_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	bps, #bw
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_freq_sink_x_1_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0.enable_grid(False)
        self.qtgui_freq_sink_x_1_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_0_win, 4,0,1,1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_1_win, 0,0,1,1)
        self.qtgui_const_sink_x_1_0_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1_0_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1_0_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_1_0_0_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_1_0_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_0_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_0_0_0_win, 2,1,1,1)
        self.qtgui_const_sink_x_1_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_const_sink_x_1_0.set_update_time(0.10)
        self.qtgui_const_sink_x_1_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1_0.enable_autoscale(False)
        self.qtgui_const_sink_x_1_0.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_1_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_0_win = sip.wrapinstance(self.qtgui_const_sink_x_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_0_win, 4,1,1,1)
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1.enable_grid(False)
        
        if not True:
          self.qtgui_const_sink_x_1.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_win, 0,1,1,1)
        self.low_pass_filter_0_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, bps, cutoff_freq, tw, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, cutoff_freq, tw, firdes.WIN_HAMMING, 6.76))
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(decimation, (taps), channel_freq-center_freq, samp_rate)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(samp_per_sym, 0.1, (rrc_taps), nfilts, nfilts/2, 0.05, 2)
        self.digital_lms_dd_equalizer_cc_0_0 = digital.lms_dd_equalizer_cc(numtap, 0.03, 2, qpsk3)
        self.digital_fll_band_edge_cc_0 = digital.fll_band_edge_cc(samp_per_sym, 0.350, 45, 0.10)
        self.digital_costas_loop_cc_0_0_0_0 = digital.costas_loop_cc(2*3.16/100, 4, False)
        self._cutoff_freq2_range = Range(0, bps/decimation, 10, bps/(2*decimation), 200)
        self._cutoff_freq2_win = RangeWidget(self._cutoff_freq2_range, self.set_cutoff_freq2, "cutoff_freq2", "counter_slider", float)
        self.top_layout.addWidget(self._cutoff_freq2_win)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0.0,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(0.707 + 0.707j, ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1, ))
        self.blocks_file_source_0_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/ascl/sbandtest/text/carrier_freq_2.4GHz/fc_2_3995/500kbps/samp_rate_2M", True)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_gr_complex*1, "output23", False)
        self.blocks_file_sink_1.set_unbuffered(False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0_0, 0), (self.blocks_throttle_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_const_sink_x_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_time_sink_x_2_0_0_0, 0))    
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_file_sink_1, 0))    
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.rms_agc_0, 0))    
        self.connect((self.digital_costas_loop_cc_0_0_0_0, 0), (self.digital_lms_dd_equalizer_cc_0_0, 0))    
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    
        self.connect((self.digital_lms_dd_equalizer_cc_0_0, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.digital_lms_dd_equalizer_cc_0_0, 0), (self.qtgui_const_sink_x_1_0, 0))    
        self.connect((self.digital_lms_dd_equalizer_cc_0_0, 0), (self.qtgui_freq_sink_x_1_0, 0))    
        self.connect((self.digital_lms_dd_equalizer_cc_0_0, 0), (self.qtgui_time_sink_x_2_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_costas_loop_cc_0_0_0_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.digital_fll_band_edge_cc_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_freq_sink_x_1_0_0_0, 0))    
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_time_sink_x_2_0_0_1, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_const_sink_x_1_0_0_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_1_0_0_0, 1))    
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_const_sink_x_1_0, 1))    
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_freq_sink_x_1_0, 1))    
        self.connect((self.low_pass_filter_0_0, 0), (self.qtgui_time_sink_x_2_0, 1))    
        self.connect((self.rms_agc_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "mpsk_stage1")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_decimation(int(self.samp_rate/(self.bps*self.samp_per_sym)))
        self.set_taps(firdes.low_pass(1,self.samp_rate,self.samp_rate/(2*self.decimation), self.transition_bw))
        self.set_transition_bw(self.samp_rate/(2*self.decimation*5))
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff_freq, self.tw, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1_0_0_0.set_frequency_range(0, int(self.samp_rate/self.decimation))
        self.qtgui_time_sink_x_2_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_2_0_0_1.set_samp_rate(int(self.samp_rate/self.decimation))

    def get_samp_per_sym(self):
        return self.samp_per_sym

    def set_samp_per_sym(self, samp_per_sym):
        self.samp_per_sym = samp_per_sym
        self.set_decimation(int(self.samp_rate/(self.bps*self.samp_per_sym)))
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.samp_per_sym), 0.35, 11*self.samp_per_sym*self.nfilts))

    def get_bps(self):
        return self.bps

    def set_bps(self, bps):
        self.bps = bps
        self.set_decimation(int(self.samp_rate/(self.bps*self.samp_per_sym)))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.bps, self.cutoff_freq, self.tw, firdes.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_1_0.set_frequency_range(0, self.bps)
        self.qtgui_time_sink_x_2_0.set_samp_rate(self.bps)
        self.set_cutoff_freq(0.35*self.bps)
        self.set_tw2(self.bps/(2*self.decimation))
        self.set_cutoff_freq2(self.bps/(2*self.decimation))

    def get_decimation(self):
        return self.decimation

    def set_decimation(self, decimation):
        self.decimation = decimation
        self.set_taps(firdes.low_pass(1,self.samp_rate,self.samp_rate/(2*self.decimation), self.transition_bw))
        self.set_transition_bw(self.samp_rate/(2*self.decimation*5))
        self.qtgui_freq_sink_x_1_0_0_0.set_frequency_range(0, int(self.samp_rate/self.decimation))
        self.qtgui_time_sink_x_2_0_0_1.set_samp_rate(int(self.samp_rate/self.decimation))
        self.set_tw2(self.bps/(2*self.decimation))
        self.set_cutoff_freq2(self.bps/(2*self.decimation))

    def get_transition_bw(self):
        return self.transition_bw

    def set_transition_bw(self, transition_bw):
        self.transition_bw = transition_bw
        self.set_taps(firdes.low_pass(1,self.samp_rate,self.samp_rate/(2*self.decimation), self.transition_bw))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.samp_per_sym), 0.35, 11*self.samp_per_sym*self.nfilts))

    def get_tw2(self):
        return self.tw2

    def set_tw2(self, tw2):
        self.tw2 = tw2

    def get_tw(self):
        return self.tw

    def set_tw(self, tw):
        self.tw = tw
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff_freq, self.tw, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.bps, self.cutoff_freq, self.tw, firdes.WIN_HAMMING, 6.76))

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps
        self.freq_xlating_fir_filter_xxx_0.set_taps((self.taps))

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_qpsk3(self):
        return self.qpsk3

    def set_qpsk3(self, qpsk3):
        self.qpsk3 = qpsk3

    def get_numtap(self):
        return self.numtap

    def set_numtap(self, numtap):
        self.numtap = numtap

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_cutoff_freq2(self):
        return self.cutoff_freq2

    def set_cutoff_freq2(self, cutoff_freq2):
        self.cutoff_freq2 = cutoff_freq2

    def get_cutoff_freq(self):
        return self.cutoff_freq

    def set_cutoff_freq(self, cutoff_freq):
        self.cutoff_freq = cutoff_freq
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff_freq, self.tw, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.bps, self.cutoff_freq, self.tw, firdes.WIN_HAMMING, 6.76))

    def get_channel_freq(self):
        return self.channel_freq

    def set_channel_freq(self, channel_freq):
        self.channel_freq = channel_freq
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.channel_freq-self.center_freq)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.freq_xlating_fir_filter_xxx_0.set_center_freq(self.channel_freq-self.center_freq)

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity


def main(top_block_cls=mpsk_stage1, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
