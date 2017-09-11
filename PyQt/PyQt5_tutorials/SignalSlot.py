e#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:30:27 2017

@author: jdn93577
"""
#creates a slider 
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider, 
    QVBoxLayout, QApplication)


class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        lcd = QLCDNumber(self) # gets number from slider ??
        sld = QSlider(Qt.Horizontal, self)# creates a horizontal slider 

        vbox = QVBoxLayout() # vertical box layout
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox) 
        sld.valueChanged.connect(lcd.display)# when slider value changes connect this to lcd display output 
        
        self.setGeometry(400, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())