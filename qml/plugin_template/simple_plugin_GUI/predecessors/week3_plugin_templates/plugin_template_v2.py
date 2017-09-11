#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:11:16 2017

@author: jdn93577
"""
   
import sys

from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
import shutil 

# Main Function
if __name__ == '__main__':
    # Create main app
    
    def on_create_template():
      # create module stuff in here
      print('creating')
      with open('modname_qml.py', 'a+') as f:
        shutil.copyfile('intro.py','modname_qml.py')
      f.close
        
      
      
      
      
      
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    myApp = QApplication(sys.argv)
    # Create a label and set its properties
    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile('plugin_template_v2.qml'))
    window = engine.rootObjects()[0]


    window.create_template.connect(on_create_template)

    window.show()


    sys.exit(myApp.exec_())