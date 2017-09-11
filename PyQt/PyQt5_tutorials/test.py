#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 10:54:15 2017

@author: jdn93577
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 




class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()

      
    def initUI(self):# constructor
        
    
        def createDropdown(text,menuName, menu, position):
            self.menuName = QLabel(text)
            self.menu = QComboBox()
            self.menu.addItem("pass")
            self.menu.addItem("other")
            self.menu.currentIndexChanged.connect(self.preProcessSelection)
                    
            grid.addWidget(self.menuName,position,0)
            grid.addWidget(self.menu,position,1)
            return
        
          
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        grid = QGridLayout() #creates an empty grid with spacing 10 (gaps) between boxes
        grid.setSpacing(10)
        
        createDropdown("pre-processing", "prepName","prep",1)
        self.setLayout(grid)
        
        
        self.setGeometry(300, 300, 300, 200)# this sets up window don't do for each button 
        self.setWindowTitle('Create plugin template')    
        self.show() 
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())