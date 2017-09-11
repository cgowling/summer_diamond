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


      
    

# Main Function
if __name__ == '__main__':
    # Create main app  

#    def on_create_template():
#        print("communicating")     
      
 #   def on_output(i, value):
        #final = content[i][]
#        print("also communicting")
#        print(i,value)

             
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    myApp = QApplication(sys.argv)
    # Create a label and set its properties
    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile('testing2.qml'))
    window = engine.rootObjects()[0]

   # window.createTemplate.connect(on_create_template)
    window.show()


    sys.exit(myApp.exec_())