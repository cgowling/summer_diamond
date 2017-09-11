#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 13:37:15 2017

@author: jdn93577
"""

import sys

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine


global plugin_info
plugin_info = {}      
    

if __name__ == '__main__':
 
  
  
    def on_communicating():
      print 'communicating' 
     
    def on_plugin_info(n, label, value):
      global plugin_info
      plugin_info[label]= value 
      
    def on_create_template():
      global plugin_info
      print plugin_info
      
    
             
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    myApp = QApplication(sys.argv)
    # Create a label and set its properties
    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile('Core.qml'))
    window = engine.rootObjects()[0]
    
    window.communicating.connect(on_communicating) 
    window.pluginInfo.connect(on_plugin_info)
    window.createTemplate.connect(on_create_template)

    window.show()


    sys.exit(myApp.exec_())
