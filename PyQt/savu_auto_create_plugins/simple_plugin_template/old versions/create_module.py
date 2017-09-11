#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 10:12:15 2017

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
    
        def createTextBox(label,labelName, labelNameEdit, position,):
            self.labelName = QLabel(label)
            self.labelNameEdit= QLineEdit()
            y = self.labelNameEdit.text()
            grid.addWidget(self.labelName , position, 0)
            grid.addWidget(self.labelNameEdit, position, 1)
            return y
          
        def createDropdown(text,menuName, menu, position):
            self.menuName = QLabel(text)
            self.menu = QComboBox()
            print(self.menu)
            self.menu.addItem("pass")
            self.menu.addItem("other")
            self.menu.currentIndexChanged.connect(self.preProcessSelection)
                    
            grid.addWidget(self.menuName,position,0)
            grid.addWidget(self.menu,position,1)
            return
        
        
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        grid = QGridLayout() #creates an empty grid with spacing 10 (gaps) between boxes
        grid.setSpacing(10)
        
        createTextBox("Plugin template name:", "modName","modNameEdit",1)     
#        self.modNameEdit.setToolTip('Input the name of the module you want to create. It must be of the form: plugin_template.py, i.e all lowercase and underscores instead of spaces with .py at the end')
        
        
        createTextBox("Your name:","userName","userNameEdit",2)
        
        createTextBox("Your e-mail:","Email","emailEdit",3 )
      
        createDropdown("Pre-processing:","prepLabel","prep",4)
        
        createTextBox("Filter frames:","filterFrameNo","filterFrameNoEdit",5)
         
        createDropdown("Post-processing:","postpLabel","postp",6)
        
        createTextBox("Numnber of input data sets:","inputNo","inputNoEdit",7)

        createTextBox("Numnber of output data sets:","outputNo","outputNoEdit",8)
        
        
        qbtn = QPushButton('Create plugin template', self)       
        qbtn.clicked.connect(self.CreateModule)
        qbtn.setToolTip('This is a creates a plugin template as a .py file ')	
  
        grid.addWidget(qbtn, 9,0)
        
        self.setLayout(grid)
        
        
        self.setGeometry(300, 300, 300, 200)# this sets up window don't do for each button 
        self.setWindowTitle('Create plugin template')    
        self.show() 
        
        
        
    def preProcessSelection(self,i):
        print('hello')
      
    def postProcessSelection(self,i):
        pass 
      
      

    
    def CreateModule(self):
       
      #y = self.modNameEdit.text() # how to get into file name accounting for ""
        y = y if len(y.split('.py')) > 1 else y + '.py' # if  already has the .py wont add anything if it does then it will leave it 
        f = open(y, 'w+')# creates ablank .py file i.e a new module. in the folder that it is run in 
        # w+ means read and write 
        f.write("#Copyright 2014 Diamond Light Source Ltd.\n#Licensed under the Apache License, Version 2.0 (the 'License');\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n#     http://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an 'AS IS' BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.\n# $Id: dezing_filter.py 467 2016-02-16 11:40:42Z kny48981 $")

        
      

        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    