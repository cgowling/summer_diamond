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
from template import Template  #!!!!!!! moved this to  a different folder trying to organise !!!!! template_content
#from collected_info import CollectedInfo

#plugin_info = CollectedInfo()
current_template = Template()

#class pluginTemplateGenerator:
  
global plugin_info
plugin_info = {}      
    

if __name__ == '__main__':
 
    def on_plugin_info( label, value):
      
      global plugin_info
      plugin_info[str(label)]= value 
      #print plugin_info
  
    def on_createTemplate():# note as the dictionary elemetns are only created once editing has finished if the user skips something that is called later it will crash  precreate a dictionary that already hass a ll labels ?? 
      print 'creating template... '
      current_template.write_template(plugin_info)
      print 'done'
          
             
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    myApp = QApplication(sys.argv)
    # Create a label and set its properties
    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile('Main.qml'))
    window = engine.rootObjects()[0]
    

    window.pluginInfo.connect(on_plugin_info)
    window.createTemplate.connect(on_createTemplate)


    window.show()


    sys.exit(myApp.exec_())
