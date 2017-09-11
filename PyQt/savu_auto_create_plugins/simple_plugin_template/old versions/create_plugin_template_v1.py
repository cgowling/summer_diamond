#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 10:12:15 2017

@author: jdn93577
"""

import sys
import PyQt5.QtWidgets as pw
import PyQt5.QtGui as pg


class Example(pw.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.dictionary = None
        self._setup_dictionary()
        self.initUI()
        
    def _setup_dictionary(self):
        self.dictionary = {}
        self.dictionary['mod'] = {'name': None, 'edit': None}
        
        
    def createTextBox(self, label, entry, position,):
        entry['name'] = pw.QLabel(label)
        entry['edit'] = pw.QLineEdit()
        pg.grid.addWidget(entry['name'] , position, 0)
        pg.grid.addWidget(entry['edit'], position, 1)     
        return #self.labelNameEdit.text()
      
    def createDropdown(self, text, menuName, menu, position):
        self.menuName = pw.QLabel(text)
        self.menu = pw.QComboBox()
        self.menu.addItem("pass")
        self.menu.addItem("other")
        self.menu.currentIndexChanged.connect(self.preProcessSelection)               
        pg.grid.addWidget(self.menuName,position,0)
        pg.grid.addWidget(self.menu,position,1)
        return
        
    def initUI(self):# constructor        
        
        pw.QToolTip.setFont(pg.QFont('SansSerif', 10))
        
        pg.grid = pw.QGridLayout() #creates an empty grid with spacing 10 (gaps) between boxes
        pg.grid.setSpacing(10)
        
        self.createTextBox("Plugin template name:", self.dictionary['mod'],1)     
        #self.modNameEdit.setToolTip('Input the name of the module you want to create. It must be of the form: plugin_template.py, i.e all lowercase and underscores instead of spaces with .py at the end')
        
        
#        self.createTextBox("Your name:","userName","userNameEdit",2)
#        
#        self.createTextBox("Your e-mail:","Email","emailEdit",3 )
#      
#        self.createDropdown("Pre-processing:","prepLabel","prep",4)
#        
#        self.createTextBox("Filter frames:","filterFrameNo","filterFrameNoEdit",5)
#         
#        self.createDropdown("Post-processing:","postpLabel","postp",6)
#        
#        self.createTextBox("Number of input data sets:","inputNo","inputNoEdit",7)
#
#        self.createTextBox("Number of output data sets:","outputNo","outputNoEdit",8)
        
        
        qbtn = pw.QPushButton('Create plugin template', self)       
        qbtn.clicked.connect(self.CreateModule)
        qbtn.setToolTip('This is a creates a plugin template as a .py file ')	
  
        pg.grid.addWidget(qbtn, 9,0)
        
        self.setLayout(pg.grid)
        
        
        self.setGeometry(300, 300, 300, 200)# this sets up window don't do for each button 
        self.setWindowTitle('Create plugin template')    
        self.show() 
        
        
        
    def preProcessSelection(self,i):
        pass 
      
    def postProcessSelection(self,i):
        pass 
       

    
    def CreateModule(self): 
        y = self.dictionary['mod']['edit'].text()
        f = open(y, 'w+')# creates ablank .py file i.e a new module. in the folder that it is run in 
        # w+ means read and write 
        f.write("#Copyright 2014 Diamond Light Source Ltd.\n#Licensed under the Apache License, Version 2.0 (the 'License');\n# you may not use this file except in compliance with the License.\n# You may obtain a copy of the License at\n#\n#     http://www.apache.org/licenses/LICENSE-2.0\n#\n# Unless required by applicable law or agreed to in writing, software\n# distributed under the License is distributed on an 'AS IS' BASIS,\n# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n# See the License for the specific language governing permissions and\n# limitations under the License.\n# $Id: dezing_filter.py 467 2016-02-16 11:40:42Z kny48981 $")
        f.write("""... module:: plugin_template\n:platform: Unix\n:synopsis: A template to create a plugin\n.. moduleauthor:: Developer Name <email@address.ac.uk>\n""")
        
      

        
if __name__ == '__main__':
    
    app = pw.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    