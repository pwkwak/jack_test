#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: MessagePassingChatApp
# Author: Martin Braun
# Description: A chat app that uses message passing
# Generated: Thu Feb  1 10:34:35 2018
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

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.digital import packet_utils
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sys
import tutorial


class chat_app(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "MessagePassingChatApp")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("MessagePassingChatApp")
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

        self.settings = Qt.QSettings("GNU Radio", "chat_app")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.msg_str = msg_str = "Hello World!123123"
        self.QPSK = QPSK = digital.constellation_calcdist(([1+1j, -1+1j, 1-1j, -1-1j]), ([0, 1, 3, 2]), 4, 1).base()

        ##################################################
        # Blocks
        ##################################################
        self.tutorial_my_qpsk_demod_cb_0 = tutorial.my_qpsk_demod_cb(True)
        self.tutorial_chat_sanitizer_0 = tutorial.chat_sanitizer("UserName", "")
        self.tutorial_chat_receiver_0 = tutorial.chat_receiver()
        self._msg_str_tool_bar = Qt.QToolBar(self)
        self._msg_str_tool_bar.addWidget(Qt.QLabel("msg_str"+": "))
        self._msg_str_line_edit = Qt.QLineEdit(str(self.msg_str))
        self._msg_str_tool_bar.addWidget(self._msg_str_line_edit)
        self._msg_str_line_edit.returnPressed.connect(
        	lambda: self.set_msg_str(str(str(self._msg_str_line_edit.text().toAscii()))))
        self.top_layout.addWidget(self._msg_str_tool_bar)
        self.digital_crc32_async_bb_1 = digital.crc32_async_bb(False)
        self.digital_crc32_async_bb_0 = digital.crc32_async_bb(True)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((QPSK.points()), 1)
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.byte_t, "tsb_tag")
        self.blocks_repack_bits_bb_1 = blocks.repack_bits_bb(2, 8, "tsb_tag", True, gr.GR_LSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, 2, "tsb_tag", False, gr.GR_LSB_FIRST)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, "tsb_tag")

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.digital_crc32_async_bb_0, 'in'))    
        self.msg_connect((self.digital_crc32_async_bb_0, 'out'), (self.tutorial_chat_receiver_0, 'in'))    
        self.msg_connect((self.digital_crc32_async_bb_1, 'out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))    
        self.msg_connect((self.tutorial_chat_sanitizer_0, 'out'), (self.digital_crc32_async_bb_1, 'in'))    
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_repack_bits_bb_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.blocks_repack_bits_bb_1, 0), (self.blocks_tagged_stream_to_pdu_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.tutorial_my_qpsk_demod_cb_0, 0))    
        self.connect((self.tutorial_my_qpsk_demod_cb_0, 0), (self.blocks_repack_bits_bb_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "chat_app")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_msg_str(self):
        return self.msg_str

    def set_msg_str(self, msg_str):
        self.msg_str = msg_str
        Qt.QMetaObject.invokeMethod(self._msg_str_line_edit, "setText", Qt.Q_ARG("QString", str(self.msg_str)))
        self.tutorial_chat_sanitizer_0.post_message(self.msg_str)

    def get_QPSK(self):
        return self.QPSK

    def set_QPSK(self, QPSK):
        self.QPSK = QPSK
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.QPSK.points()))


def main(top_block_cls=chat_app, options=None):

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
